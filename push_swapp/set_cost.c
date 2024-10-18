/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   cost.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/07 19:41:55 by cde-paiv          #+#    #+#             */
/*   Updated: 2024/10/07 19:41:55 by cde-paiv         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
// transforma números negativos em positivos.
int ft_abs(int i)
{
    if (i < 0)
        return (i * (-1));
    return (i);
}
// encontra o maior valor de índice dentro da pilha a.
int fin_max_index(t_info *info)
{
    t_stack *temp;
    int max;

    temp = info->stack_a;
    max = temp->index;
    while (temp)
    {
        if (temp->index > max)
            max = temp->index;
        temp = temp->next;
    }
    return (max);
}
// calcula o custo de inserir um valor maior que o índice index_b na pilha a.
static int  insert_big_value(t_info *info, int index_b)
{
    t_stack *temp;
    int i;

    temp = info->top_a;
    i = 0;
    while (temp->index != (index_b - 1))
    {
        i++;
        temp = temp->prev;
        if (!temp)
        {
            index_b--;
            temp = info->top_a;
            i = 0;
        }
    }
    i++;
    if (i <= (info->len_a - info->len_b) / 2)
        return (i);
    else
        return (i - (info->len_a - info->len_b));
}
// calcula o custo de mover um elemento da pilha b para a posição correta na pilha a.
static int  check_cost_a(t_info *info, int index_b)
{
    t_stack *temp;
    int i;
    int max;

    temp = info->top_a;
    i = 0;
    max = fin_max_index(info);
    if (index_b > max)
        return (insert_big_value(info, index_b));
    while (temp->index != (index_b + 1))
    {
        i++;
        temp = temp->prev;
        if (!temp)
        {
            index_b++;
            temp = info->top_a;
            i = 0;
        }
    }
    if (i <= ((info->len_a - info->len_b) / 2))
        return (i);
    else
        return (i - (info->len_a - info->len_b));
}
// calcula os custos de mover elementos da pilha b para a pilha a.
void    set_cost(t_info *info)
{
    t_stack *temp;
    int i;

    temp = info->top_b;
    if (info->len_b == 0)
        info->len_b = info->len_a - 3;
    i = 0;
    while (i++ <= (info->len_b / 2))
    {
        temp->cost_a = check_cost_a(info, temp->index);
        temp->cost_b = (i - 1);
        temp = temp->prev;
    }
    temp = info->stack_b;
    i = 0;
    while (i++ < info->len_b / 2)
    {
        temp->cost_a = check_cost_a(info, temp->index);
        temp->cost_b = (i) * (-1);
        temp = temp->next;
    }
}
