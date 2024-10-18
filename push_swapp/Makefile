# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cde-paiv <cde-paiv@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/10/03 17:58:50 by cde-paiv          #+#    #+#              #
#    Updated: 2024/10/03 17:58:50 by cde-paiv         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME	= push_swap

FLAGS	= -Wall -Werror -Wextra -g
CC		= cc $(FLAGS)

LIBFT	= libft/libft.a

SRCS = push_swap.c check_errors.c init_stack.c push_a_to_b.c push_funcs.c \
		rotate_funcs.c swap_funcs.c push_back.c reverse_r_funcs.c set_cost.c \

OBJS	= $(SRCS:.c=.o)

%.o: %.c
	$(CC) -c $^

all: $(NAME)

$(NAME): $(OBJS) $(LIBFT)
	$(CC) $(OBJS) $(LIBFT) -o $(NAME)


$(LIBFT):
	cd libft && $(MAKE)

clean:
	rm -f $(OBJS)

fclean: clean
	cd libft && $(MAKE) fclean
	rm -f $(NAME)

re: fclean all

.PHONY = all clean fclean re
