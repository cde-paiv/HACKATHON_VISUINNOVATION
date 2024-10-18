/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_funcs.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/07 14:03:21 by cde-paiv          #+#    #+#             */
/*   Updated: 2024/10/07 14:03:21 by cde-paiv         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
//  Remove o topo da pilha b.
static void delete_b(t_info *info)
{
    t_stack *temp;

    temp = info->stack_b;
    while (temp->next != info->top_b && temp->next != NULL)
        temp = temp->next;
    if (temp->next == NULL)
    {
        info->stack_b = NULL;
        info->top_b = NULL;
        return ;
    }
    temp->next = NULL;
    info->top_b = temp;
}
// Move o topo da pilha b para a pilha a.
void    push_a(t_info *info)
{
    t_stack *temp;

    temp = info->stack_a;
    if (info->stack_b == NULL)
        return ;
    if (temp == NULL)
    {
        info->stack_a = info->stack_b;
        info->stack_a->prev = NULL;
        info->top_a = info->stack_a;
    }
    else 
    {
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = info->top_b;
        temp->next->prev = temp;
        info->top_a = info->top_b;
    }
    delete_b(info);
    ft_putstr_fd("pa\n", 1);
}
// Remove o topo da pilha a
static void delete_a(t_info *info)
{
    t_stack *temp;

    temp = info->stack_a;
    while (temp->next != info->top_a)
        temp = temp->next;
    temp->next = NULL;
    info->top_a = temp;
}
// Move o topo da pilha a para a pilha b
void    push_b(t_info *info)
{
    t_stack *temp;

    temp = info->stack_b;
    if (info->stack_a == NULL)
        return ;
    if (temp == NULL)
    {
        info->stack_b = info->top_a;
        info->stack_b->prev = NULL;
        info->top_b = info->stack_b;
    }
    else
    {
        while (temp->next != NULL)
            temp = temp->next;
        temp->next = info->top_a;
        temp->next->prev = temp;
        info->top_b = info->top_a;
    }
    delete_a(info);
    ft_putstr_fd("pb\n", 1);
}