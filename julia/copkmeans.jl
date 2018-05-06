
function l2_distance(x::Array{Float64,1}, y::Array{Float64,1})
    z = x - y
    return vecdot(z, z)
end

function read_data(datafile::String)
    return readdlm(datafile)
end

function read_constraints(consfile::String)
    ml = Array{Tuple{Int,Int},1}()
    cl = Array{Tuple{Int,Int},1}()
    constraints = readdlm(consfile)
    num_constraints = size(constraints)[1]
    for i in 1:num_constraints
        pair = tuple(convert(Array{Int, 1}, constraints[i, 1:2])...)
        label = Int(constraints[i, 3])
        if label == 1
            push!(ml, pair)
        else
            push!(cl, pair)
        end
    end
    return (ml, cl)
end

function transitive_closure(ml::Array{Tuple{Int, Int}, 1},
        cl::Array{Tuple{Int, Int}, 1},
        n::Int)
    ml_graph = Dict{Int, Set{Int}}()
    cl_graph = Dict{Int, Set{Int}}()
    for i in 1:n
        ml_graph[i] = Set{Int}()
        cl_graph[i] = Set{Int}()
    end
        
    function add_both(d::Dict{Int, Set{Int}}, i::Int, j::Int)
        push!(d[i], j)
        push!(d[j], i)
    end
        
    for (i, j) in ml
        add_both(ml_graph, i, j)
    end
    
    function dfs!(i::Int, graph::Dict{Int, Set{Int}},
            visited::Array{Bool, 1}, component::Array{Int, 1})
        visited[i] = true
        for j in graph[i]
            if !visited[j]
                dfs!(j, graph, visited, component)
            end
        end
        push!(component, i)
    end
    
    visited = fill(false, n)
    for i in 1:n
        if !visited[i]
            component = Array{Int,1}()
            dfs!(i, ml_graph, visited, component)
            for x1 in component
                for x2 in component
                    if x1 != x2
                        push!(ml_graph[x1], x2)
                    end
                end
            end
        end
    end
    
    for (i, j) in cl
        add_both(cl_graph, i, j)
        for y in ml_graph[j]
            add_both(cl_graph, i, y)
        end
        for x in ml_graph[i]
            add_both(cl_graph, x, j)
            for y in ml_graph[j]
                add_both(cl_graph, x, y)
            end
        end
    end
    
    for i in keys(ml_graph)
        for j in ml_graph[i]
            if j!=i && j in cl_graph[i]
                @printf "inconsistent constraints between %d and %d\n" i j
                throw(DomainError())
            end
        end
    end
    
    return ml_graph, cl_graph
end

function get_ml_info(ml::Dict{Int, Set{Int}}, dataset::Array{Float64,2})
    n, dim = size(dataset)
    flags = fill(true, n)
    groups = Array{Array{Int,1},1}()
    for i in 1:n
        if !flags[i]
            continue
        end
        group = collect(union(ml[i], Set(i)))
        push!(groups, group)
        for j in group
            flags[j] = false
        end
    end
    
    n_groups = length(groups)
    scores = fill(0.0, n_groups)
    centroids = fill(0.0, (n_groups, dim))
    
    for (j, group) in enumerate(groups)
        for i in group
            centroids[j,:] += dataset[i,:]
        end
        centroids[j,:] /= length(group)
        end
    end
    
    #DEBUG
    for j in groups
        for i in groups[j]
            println(size(centroids), i, j)
        end
    end
    
    scores = [sum(l2_distance(centroids[i,:], centroids[j,:]) for i in groups[j]) for j in 1:n_groups]
    return groups, scores, centroids
end

function closest_clusters(centers::Array{Array{Float64,1},1}, 
        datapoint::Array{Float64,1})
    distances = [l2_distance(center, datapoint) for center in centers]
    return sortperm(distances)
end

#  from scikit-learn (https://goo.gl/1RYPP5)
function tolerance(tol::Float64, dataset::Array{Float64, 2})
    n, dim = size(dataset)
    averages = [sum(dataset[i, d] for i in 1:n)/n for d in 1:dim]
    variances = [sum((dataset[i, d]-averages[d])^2 for i in 1:n)/n for d in 1:dim]
    return tol * sum(variances) / dim
    
end

function violate_constraints(data_index, cluster_index, 
        clusters, ml, cl)
    for i in ml[data_index]
        if clusters[i] != -1 &&  clusters[i] != cluster_index
            return true
        end
    end
    
    for i in cl[data_index]
        if clusters[i] == cluster_index
            return true
        end
    end
    
    return false
end

function compute_centers(clusters::Array{Int, 1},
    dataset::Array{Float64,2}, k::Int, 
        ml_info::Tuple{Array{Array{Int,1},1}, 
        Array{Float64,1}, 
        Array{Float64,2}})
    cluster_ids = Set(clusters)
    k_new = length(cluster_ids)
    id_map = Dict(zip(cluster_ids, 1:k_new))
    clusters = [id_map[x] for x in clusters]
    
    dim = size(dataset)[2]
    centers = fill(0.0, (k, dim))
    
    counts = fill(0.0, k_new)
    for (j, c) in enumerate(clusters)
        centers[c,:] += dataset[j,:]
        counts[c]+=1
    end
    
    for j in 1:k_new
        centers[j] /= counts[j]
    end
    
    if k_new < k 
        ml_groups, ml_scores, ml_centroids = ml_info
        current_scores = [sum(l2_distance(centers[clusters[i],:], 
                                          dataset[i,:]) 
                              for i in group) 
                              for group in ml_groups]
        group_ids = sort(1:length(ml_groups), 
                           by= x -> current_scores[x] - ml_scores[x],
                           rev=true) 
        for j in 1:(k-k_new)
            gid = group_ids[j]
            cid = k_new + j
            centers[cid,:] = ml_centroids[gid,:]
            for i in ml_groups[gid]
                clusters[i] = cid
            end
        end
    end
    return clusters, centers
end

function initialize_centers(dataset::Array{Float64,2}, 
        k::Int, method::String)
    n = size(dataset)[1]
    if method == "random"
        ids = randperm(n)
        return dataset[ids[1:k],:]
    elseif method = "kmpp"
        chances = fill(1.0, n)
        centers = Array{Array{Float64,1},1}()
        for _ in 1:k
            chances /= sum(chances)
            r = rand()
            acc = 0.0
            for (index, chance) in enumerate(chances)
                if acc + chance >= r
                    break
                end
                acc += chance
            end
            push!(centers, dataset[index,:])
            for index in 1:n
                point = dataset[index,:]
                cids, distances = closest_clusterst(centers, point)
                chances[index] = distances[cids[1]]
        end
        return centers
    end
end

function cop_kmeans(dataset::Array{Float64,2}, k::Int, 
        ml::Array{Tuple{Int, Int}, 1}=Array{Array{Int,1},1}(), 
        cl::Array{Tuple{Int, Int},1}=Array{Array{Int,1},1}(),
        initialization::String="kmpp", max_iter::Int=300, 
        tol::Float64=1e-4)
    
    n = size(dataset)[1]
    ml, cl = transitive_closure(ml, cl, n)
    ml_info = get_ml_info(ml, dataset)
    tol = tolerance(tol, dataset)
    
    centers = initialize_centers(dataset, k, initialization)
    for _ in 1:max_iter
        clusters_ = fill(-1, n)
        for i in 1:n
            d = dataset[i,:]
            indices, _  = closest_clusters(centers, d)
            counter = 0
            if clusters_[i] == -1
                found_cluster = false
                while (!found_cluster) && counter < len(indices)
                    index = indices[counter]
                    if !violate_constraint(i, index, clusters_, ml, cl)
                        found_cluster = true
                        clusters_[i] = index
                        for j in ml[i]
                            clusters_[j] = index
                        end
                    counter += 1
                    end
                end
                if !found_cluster
                    return nothing
                end
            end
        end
        clusters_, centers_ = compute_centers(clusters_, dataset, k, ml_info)
        shift = sum(l2_distance(centers[i,:], centers_[i]) for i in 1:k)
        if shift <= tol
            break
        end
        centers = centers_
    end
    return clusters_, centers_
end

data = read_data("examples/iris.data")
ml, cl = read_constraints("examples/iris.constraints")
;

cop_kmeans(data, 2, ml, cl)
