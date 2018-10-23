/* Definir una clase que represente números complejos, implementando
constructores, un método que devuelva el conjugado, el módulo, y
sobrecargar los operadores +, - y *. Implementar una función print
que muestre al complejo como a + b i. */

#include <iostream>
#include <math.h>
using namespace std;

class Complex{

    public:   

        float a, b;

        Complex(float x, float y){
            a = x;
            b = y;
        }

        Complex operator + (Complex);
        Complex operator - (Complex);      
        Complex operator * (Complex);        


        void print();
        void module();
        void conjugate();
};


Complex Complex::operator+ (Complex v){
    
    Complex suma(a,b);

    suma.a = a + v.a;
    suma.b = b + v.b;

    return (suma);
}


Complex Complex::operator- (Complex v){
    
    Complex resta(a,b);

    resta.a = a - v.a;
    resta.b = b - v.b;

    return (resta);
}


Complex Complex::operator* (Complex v){
    
    Complex mult(a,b);

    mult.a = a*v.a - b*v.b;
    mult.b = a*v.b + b*v.a;

    return (mult);
}


void Complex::print(){
    if (b == 0) {
        cout << a << endl;

    } else if (b < 0) {
        cout << a << " " << b << "*i" << endl;

    } else { 
        cout << a << " +" << b << "*i" << endl;
    
    }
            
    return;
}

void Complex::module(){
    cout << sqrt(a*a + b*b) << endl;
    return;
}

void Complex::conjugate(){ 
    b = -b;
    return;
}


int main(){

    Complex z(1,-1);   
    z.print();
    
    z.conjugate();
    z.print();
    
    z.conjugate();
    z.print();

    z.module();
    
    Complex w(2,2);
    (z + w).print();
    (z - w).print();
    (z * w).print();


    return 0;

}
