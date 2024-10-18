/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_funcs.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/05 02:17:47 by cde-paiv          #+#    #+#             */
/*   Updated: 2024/10/05 02:17:47 by cde-paiv         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
// Troca os dois elementos do topo da pilha a
void    swap_a(t_info *info)
{
    t_stack *temp;
    int swapv;
    int swapi;

    temp = info->stack_a;
    while (temp->next != info->top_a)
        temp = temp->next;
    swapv = temp->value;
    swapi = temp->index;
    temp->value = info->top_a->value;
    temp->index = info->top_a->index;
    info->top_a->value = swapv;
    info->top_a->index = swapi;
    ft_putstr_fd("sa\n", 1);
}

// Troca os dois elementos do topo da pilha b
void    swap_b(t_info *info)
{
    t_stack *temp;
    int swapv;
    int swapi;

    temp = info->stack_b;
    while (temp->next != info->top_b)
        temp = temp->next;
    swapv = temp->value;
    swapi = temp->index;
    temp->value = info->top_b->value;
    temp->index = info->top_b->index;
    info->top_b->value = swapv;
    info->top_b->index = swapi;
    ft_putstr_fd("sb\n", 1);
}

//Troca os dois elementos do topo de ambas as pilhas a e b simultaneamente
void    swap_s(t_info *info)
{
    swap_a(info);
    swap_b(info);
    ft_putstr_fd("ss\n", 1);
}