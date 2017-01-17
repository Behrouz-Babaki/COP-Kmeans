#include <iostream>
#include "kmeans.hpp"

using std::cout;
using std::endl;

void test_func(int& a, int& b) {
  a = 10;
  b = 20;
  return;
}

int main(void) {
  cout << "Hello World!" << endl;
  int x = 0, y  = 1;
  test_func(x, y);
  cout << x << " " << y << endl;
  return 0;
}
