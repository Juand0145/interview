#ifndef HOLBERTON_H
#define HOLBERTON_H

#include <stdio.h>
#include <stdlib.h>

int _putchar(char c);
void error(void);
int digit_check(char *number);
void set_max_min(unsigned int digit_count1, unsigned int digit_count2,
unsigned int *max_digit, unsigned int *min_digit,
char **num1, char **num2, char *arg1, char *arg2);
char **create_double(unsigned int row_size, unsigned int column_size);
char *create_final(unsigned int size, char **calculation);
char *final_realloc(char *final, char **calculation);

/**
 * error - prints error message and exits program
 */
void error(void)
{
int i = 0;
char error[6] = "Error";

for (i = 0; error[i]; i++)
_putchar(error[i]);
_putchar('\n');
exit(98);
}

/**
 * digit_check - checks if number contains only digits and
 * counts number of digits
 * @number: array of characters to check if digits
 * Return: 0 on failure or number of digits in number
 */
int digit_check(char *number)
{
int i = 0;

for (i = 0; number[i]; i++)
{
if (number[i] < '0' || number[i] > '9')
return (0);
}
return (i);
}

#endif
