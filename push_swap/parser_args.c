# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include "libft.h"

typedef struct{
	int	num_list;
	int	adaptative;
	int	simple;
	int	medium;
	int	complex;
	int	bench;
} t_args

static void	ft_init_arguments(void);
{
	arguments.num_list = -1;
	arguments.adaptative = 0;
	arguments.simple = 0;
	arguments.medium = 0;
	arguments.complex = 0;
	arguments.bench = 0;
}

static int	ft_check_flags(char *args)
{
	size_t	strategies_overlap;

	if (!args)
		return (0);
	if (ft_strncmp(*args, "--adaptative", 12) == 0)
		arguments.adaptative = 1;
	if (ft_strncmp(*args, "--simple", 8) == 0)
		arguments.simple = 1;
	if (ft_strncmp(*args, "--medium", 8) == 0)
		arguments.medium = 1;
	if (ft_strncmp(*args, "--complex", 9) == 0)
		arguments.complex = 1;
	if (ft_strncmp(*args, "--bench", 7) == 0)
		arguments.bench = 1;
	strategies_overlap = arguments.adaptative + arguments.simple
						+ arguments.medium + arguments.complex;
	valid_flags = strategies_overlap + arguments.bench;
	if (strategies_overlap > 1)
		return (0);
	if (valid_flags == 0)
		return (0);
	return (1);
}

static int	ft_check_num_list(char *args, char *nums_str)
{
	c	if (!args)
		return (0);
	si empieza con -- return (0);
	else crear un char ** y llenarlo con un split por espacios 
	mientras haya parámetros:
		si ! (empieza con '-' y/o todos los caracteres restantes son numeros es válido)
			no es valido return (NULL);
	hacer un join de args con nums_str;
	poner la flag de num en 1
	"1"
	"0 1 2 3 4"
	if ( )
	return (1);
}

int	**ft_parser_args(const char **arguments)
{
	char	**args;
	char	*nums_str;
	int		**nums;

	ft_init_arguments();
	**args = **arguments;
	while (*args)
	{ 
		if (ft_check_flags(*args) == 0 && ft_check_num_list(*args, &nums_str) == 0)
			return (NULL);
		(*args)++;
	}
	**args = **arguments;
	return(ft_parser_nums(*args))
}
