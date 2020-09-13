#include <bits/stdc++.h>
using namespace std;

void reverseNullTerminatedStr(char *str) {
    char* end = str;
    char tmp;

    if (str) {
        while (*end) { /* find end of teh string */
            ++end;
        }
        --end; /* set one char back, since the last char is null */

        /* swap char from start to end
         * until pointers meet in middle */
        while (str < end) {
            cout << str << " " << end << endl;
            tmp = *str;
            *str++ = *end;
            *end-- = tmp;
        }
    }
    cout << str << endl;
}

int main() {
    char str[] = "HELLO WORLD";
    reverseNullTerminatedStr(str);
}