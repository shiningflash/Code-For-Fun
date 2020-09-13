/* shallow copy may cause run-time errors */
/* deep copy is widely used in real life */

#include <bits/stdc++.h>
using namespace std;

struct Test {
    char *ptr;
};

void shallow_copy(Test &src, Test &dest) {
    dest.ptr = src.ptr;
}

void deep_copy(Test &src, Test &dest) {
    dest.ptr = (char*)malloc(strlen(src.ptr) + 1);
    strcpy(dest.ptr, src.ptr);
}

int main() {
    char c1[] = "HELLO!";
    char c2[] = "HEY!";

    Test src;
    src.ptr = c1;
    Test dest;
    dest.ptr = c2;
    
    shallow_copy(src, dest);
    cout << src.ptr << " " << dest.ptr << endl;

    deep_copy(src, dest);
    cout << src.ptr << " " << dest.ptr << endl;

    return 0;
}