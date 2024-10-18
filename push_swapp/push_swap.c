/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/08 15:44:19 by cde-paiv          #+#    #+#             */
/*   Updated: 2024/10/08 15:44:19 by cde-paiv         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void    free_stacks(t_info *info)
{
    t_stack *temp;

    while (info->stack_a)
    {
        temp = info->stack_a;
        info->stack_a = temp->next;
        free(temp);
    }
}

void    final_sort(t_info *info)
{
    t_stack *temp;
    int i;

    i = 0;
    temp = info->top_a;
    find_max(info);
    while (temp->value != info->max)
    {
        i++;
        temp = temp->prev;
    }
    if (i <= (info->len_a / 2))
    {
        while (info->stack_a->value != info->max)
            rotate_a(info, 0);
    }
    else
    {
        while (info->stack_a->value != info->max)
            reverse_rotate_a(info, 0);
    }
}

void    push_swap(t_info *info)
{
    int z;

    z = 0;
    if (info->len_a > 2)
    {
        while (z++ < (info->len_a - 3))
            bigger_stacks(info);
        case3(info);
        while (info->stack_b)
            push_back(info);
    }
    final_sort(info);
    free_stacks(info);
}

int main(int argc, char **argv)
{
    t_info  info;
    int *input;

    input = NULL;
    if (argc < 2)
        return (0);
    if (check_error(argv) < 0)
    {
        ft_putstr_fd("error\n", 2);
        return (1);
    }
    input = check_for_duplicates(input, argv, argc -1);
    if (is_ordenated(argc - 1, input))
        return (0);
    init_stacks(&info);
    create_stacks(input, argc - 1, &info);
    free(input);
    init_index(&info);
    push_swap(&info);
    return (0);
}