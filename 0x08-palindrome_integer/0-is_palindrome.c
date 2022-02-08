#include "palindrome.h"
/**
 * is_palindrome - function that checks whether or not
 * a given unsigned integer is a palindrome.
 * @n:  is the number to be checked
 * Return: 1 if n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n)
{
unsigned long rem, num, rev = 0;
num = n;

while (n > 0)
{
rem = n % 10;
rev = rev * 10 + rem;
n /= 10;
}
if (rev == num)
return (1);
else
return (0);
}
