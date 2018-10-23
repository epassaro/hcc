#include <iostream>
#define POW 3

long pow(int x){

    for (int i=2; i<POW; i++){
        x *= x;
    }

return x;

}

long sum(int x){

    int sum = 0;
    for (int i=1; i<=x; i++){
        sum += pow(i);
        std::cout << i << "^" << POW << " = " << pow(i) << std::endl;
    }

return sum;

}


int main() {

    int n;

    std::cout << "Enter 'n': ";
    std::cin >> n;
    std::cout << std::endl;
    std::cout << std::endl << "Sum of ^" << POW << " = " << sum(n) << std::endl;

return 0;

}
