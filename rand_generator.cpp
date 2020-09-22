#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
static ll RND_VAL = 33;
const ll NUM_ONE = 12367;
const ll NUM_TWO = 78;
const ll MOD_VAL = 1000;

ll gettime() {
    time_t now = time(NULL);
    stringstream ss;
    ss << now;
    string now_s = ss.str();
    long long int now_l = 0;
    stringstream sss(now_s);
    sss >> now_l;
    return now_l;
}

ll rand_generator() {
    RND_VAL = (((gettime() * NUM_ONE) / NUM_TWO) ^ MOD_VAL) + RND_VAL;
    return RND_VAL %= MOD_VAL;
}

int main() {
    int itr = 100;
    for (int i = 0; i < itr; i++) {
        ll n = rand_generator();
        cout << n << endl;
    }
    return 0;
}