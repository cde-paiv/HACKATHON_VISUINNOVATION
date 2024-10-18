/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_r_funcs.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/07 18:52:04 by cde-paiv          #+#    #+#             */
/*   Updated: 2024/10/07 18:52:04 by cde-paiv         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
// Move o último elemento da pilha a para o topo, realizando uma rotação reversa.
void    reverse_rotate_a(t_info *info, int rrr)
{
    t_stack *temp;

    temp = info->stack_a;
    info->stack_a = info->stack_a->next;
    info->stack_a->prev = NULL;
    temp->next = NULL;
    temp->prev = info->top_a;
    info->top_a->next = temp;
    info->top_a = temp;
    if (!rrr)
        ft_putstr_fd("rra\n", 1);
}
//  Move o último elemento da pilha b para o topo, realizando uma rotação reversa.
void    reverse_rotate_b(t_info *info, int rrr)
{
    t_stack *temp;

    temp = info->stack_b;
    info->stack_b = info->stack_b->next;
    info->stack_b->prev = NULL;
    temp->next = NULL;
    temp->prev = info->top_b;
    info->top_b->next = temp;
    info->top_b = temp;
    if (!rrr)
        ft_putstr_fd("rrb\n", 1);
}
// Realiza a rotação reversa simultânea das pilhas a e b.
void    reverse_rotate_r(t_info *info)
{
    reverse_rotate_a(info, 1);
    reverse_rotate_b(info, 1);
    ft_putstr_fd("rrr\n", 1);
}
