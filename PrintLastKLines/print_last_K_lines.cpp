#include <bits/stdc++.h>
using namespace std;

void printLastKLines(const string filename, const int K) {
    ifstream file(filename);

    string arr[K];
    int size = 0;

    while (file.peek() != EOF) {
        getline(file, arr[size%K]);
        size++;
    }

    int start = size > K ? (size % K) : 0;
    int count = min(K, size);

    for (int i = 0; i < count; i++) {
        cout << arr[(start + i) % K] << endl;
    }
} 

int main() {
    string filename = "in.txt";
    const int K = 5;
    printLastKLines(filename, K);
    return 0;
}