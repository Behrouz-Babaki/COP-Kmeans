.PHONY: main test clean

CXX = g++
CPP_FILES := $(wildcard src/*.cpp)
OBJ_FILES  := $(patsubst src/%.cpp,obj/%.o,$(CPP_FILES))

obj/%.o: src/%.cpp
	$(CXX) -c $< -o $@

main: $(OBJ_FILES)
	$(CXX) $^ -o bin/main

test: main
	@./bin/main

clean:
	@rm -rf *~ src/*~  obj/* bin/*
