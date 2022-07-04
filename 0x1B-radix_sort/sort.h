#ifndef SORT_H
#define SORT_H

#include <stdio.h>
#include <stdlib.h>

void print_array(const int *array, size_t size);
void radix_sort(int *array, size_t size);
int digit_counting(int *array, size_t size);
int get_divisor(int current_digit);
void insert_into_holder(int value, int divisor, int *holder, unsigned int i);

#endif