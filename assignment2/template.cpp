#include <iostream>

using namespace std;

template <typename T1, typename T2>
T1 funct(T1 b, T2 a){
    cout << a;
    cout << b;
    return b+a;
}

int main(){
    cout <<funct("hello", 5);
    return 0;
}
