#include <iostream>
#include <cmath>

using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	// Quadratic function
	float a,b,c,determinant,root1,root2,real,imag;
	cout<<"Enter coefficients a,b and c of the quadratic equation \n"<<endl;
	cin>>a;
	cin>>b;
	cin>>c;
	
	// calculating determinant.....
	determinant=b*b-4*a*c;
	if(determinant>=0){
		root1=(-b+sqrt(determinant))/(2*a);
		root2=(-b-sqrt(determinant))/(2*a);
		
		cout<<"Square roots are"<<root1<<" "<<root2;
	}
	
	else{
		real=-b/2*a;
		imag=sqrt(-determinant)/(2*a);
		cout<<"Square roots are:"<<real<< "+"<<imag<< "i" <<real<< "-" <<imag<<  "i" <<endl;
	}
	return 0;
}
