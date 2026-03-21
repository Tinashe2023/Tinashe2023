/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include<stdio.h>

int main()
{
    float x,y,z,p;
    printf("Enter value of x:");
    scanf("%f",&x);
    printf("Enter value of y:");
    scanf("%f",&y);
    printf("Enter value of z:");
    scanf("%f",&z);
    p=2*y+3*(x-z);
    printf("p=%f",p);
    
    return 0;
    
}

