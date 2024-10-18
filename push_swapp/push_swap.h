/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/03 17:59:00 by cde-paiv          #+#    #+#             */
/*   Updated: 2024/10/03 17:59:00 by cde-paiv         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "libft/libft.h"

typedef struct s_stack
{
	int				value;
	int				index;
	int				cost_a;
	int				cost_b;
	struct s_stack	*prev;
	struct s_stack	*next;
}	t_stack;

typedef struct s_info
{
	t_stack	*stack_a;
	t_stack	*stack_b;
	int		len_a;
	int		len_b;
	int		pivot;
	t_stack	*top_a;
	t_stack	*top_b;
	int		max;
}	t_info;

int	check_number(char *argv);
int	check_error(char **argv);
int	*check_for_duplicates(int *input, char **argv, int list_size);
int	is_ordenated(int input_len, int *input);
void	init_stacks(t_info *info);
void	create_stacks(int *a, int list_size, t_info *info);
void	find_max(t_info *info);
void	init_index(t_info *info);
void	case3(t_info *info);
void    swap_a(t_info *info);
void    swap_b(t_info *info);
void    swap_s(t_info *info);
void    push_a(t_info *info);
void    push_b(t_info *info);
void    rotate_a(t_info *info, int rr);
void    rotate_b(t_info *info, int rr);
void    rotate_r(t_info *info);
void    reverse_rotate_a(t_info *info, int rrr);
void    reverse_rotate_b(t_info *info, int rrr);
void    reverse_rotate_r(t_info *info);
int ft_abs(int i);
int fin_max_index(t_info *info);
void    set_cost(t_info *info);
void    bigger_stacks(t_info *info);
void    push_back(t_info *info);

#endif