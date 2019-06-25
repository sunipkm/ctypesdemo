#include <stdio.h>
extern inline void add_noret ( double * c , double a , double b )
{
	( * c ) = a + b ;
	printf ( "In C:\nFunction took %lf, %lf as input values and %p as output destination, where the C code put the value %lf.\n" , a , b , ( void * ) c , ( * c ) ) ;
	return ;
}

extern inline double add_ret ( double a , double b )
{
	double c = a + b ;
	printf ( "In C: Inputs -> %lf, %lf; returns %lf.\n" , a , b , c ) ;
	return c ;
}