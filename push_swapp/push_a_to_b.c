/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_a_to_b.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/08 12:27:48 by cde-paiv          #+#    #+#             */
/*   Updated: 2024/10/08 12:27:48 by cde-paiv         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
// move os elementos do topo da pilha b para a
static void push_base(t_info *info, int i)
{
    while (i >= 0)
    {
        reverse_rotate_a(info, 0);
        i--;
    }
    push_b(info);
}
// move os elementos do topo da pilha a para b
static void push_top(t_info *info, int i)
{
    while (i-- > 0)
        rotate_a(info, 0);
    push_b(info);
}
// calcula o pivô básico, para dividir o conjunto em partes.
static void get_pivot_1(t_info *info)
{
    t_stack *temp;
    int min;
    int max;

    temp = info->stack_a;
    while (temp)
    {
        if (temp->prev == NULL)
        {
            min = temp->index;
            max = temp->index;
        }
        else
        {
            if (temp->index < min)
                min = temp->index;
            else if (temp->index > max)
                max = temp->index;
        }
        temp = temp->next;
    }
    info->pivot = (min + max) / 2;
}
// lida com a divisão em blocos, ajustando o pivô dependendo do tamanho da pilha.
static void get_pivot(t_info *info)
{
    static int  blocks;
    static int  i;
    static int  div;

    div = 1;
    if (i == 0)
    {
        if (info->len_a >= 100 && info->len_a < 500)
            blocks = 5;
        else if (info->len_a >= 500)
            blocks = 11;
        else
            blocks = 1;
    }
    if (blocks != 1 && i < info->len_a)
    {
        if (i >= (info->len_a / blocks) * div)
        {
            div++;
            info->pivot = (info->len_a / blocks) * div;
        }
    }
        else
             get_pivot_1(info);
        i++;
}
// decide qual operação realizar quando a pilha é grande.
void    bigger_stacks(t_info *info)
{
    t_stack *temp;
    int i;
    int j;

    i = 0;
    j = 0;
    get_pivot(info);
    temp = info->stack_a;
    while (temp->index > info->pivot)
    {
        temp = temp->next;
        i++;
    }
    temp = info->top_a;
    while (temp->index > info->pivot)
    {
        temp = temp->prev;
        j++;
    }
    if (j <= i || (j - 1) <= i)
        push_top(info, (j));
    else
        push_base(info, (i));
}