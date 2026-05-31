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
} t_args;

static void	ft_initflags(t_args *flags)
{
	flags->num_list = -1;
	flags->adaptative = 0;
	flags->simple = 0;
	flags->medium = 0;
	flags->complex = 0;
	flags->bench = 0;
}

static int	ft_check_flags(char *args, t_args *flags)
{
	size_t	strategies_overlap;
	int		valid_flags;

	if (!args || args[0] != '-' || args[1] != '-')
		return (0);
	if (ft_strncmp(args, "--adaptative", 12) == 0)
		flags->adaptative = 1;
	else if (ft_strncmp(args, "--simple", 8) == 0)
		flags->simple = 1;
	else if (ft_strncmp(args, "--medium", 8) == 0)
		flags->medium = 1;
	else if (ft_strncmp(args, "--complex", 9) == 0)
		flags->complex = 1;
	else if (ft_strncmp(args, "--bench", 7) == 0)
		flags->bench = 1;
	else
		return (0);
	strategies_overlap = flags->adaptative + flags->simple
						+ flags->medium + flags->complex;
	valid_flags = strategies_overlap + flags->bench;
	if (strategies_overlap > 1)
		return (0);
	if (flags->num_list == 0)
		flags->num_list = 1;
	return (1);
}

static int	ft_str_is_alfa(char *nums)
{
	if (*nums == '-')
		nums++;
	if (!*nums)
		return (1);
	while (*nums)
	{
		if (ft_isalpha(*nums))
			return (1);
		nums++;
	}
	return (0);
}

static void ft_free_matrix(char **nums)
{
	int i = 0;
	if (!nums)
		return ;
	while (nums[i])
		free(nums[i++]);
	free(nums);
}

static int	ft_check_num_list(char *args, char **nums_str, t_args *flags)
{
	char	**nums;
	char	*temp;
	int		i;

	if (!args || (args[0] == '-' && args[1] == '-'))
		return (0);
	nums = ft_split(args, ' ');
	if (!nums)
		return (0);
	i = 0;
	while(nums[i])
	{
		if (ft_str_is_alfa(nums[i]))
		{
			ft_free_matrix(nums);
			return (0);
		}
		i++;
	}
	ft_free_matrix(nums);
	if (flags->num_list == 1)
		return (0);
	temp = *nums_str;
	*nums_str = ft_strjoin(temp, args);
	free (temp);
	temp = *nums_str;
	*nums_str = ft_strjoin(temp, " ");
	free (temp);
	flags->num_list = 0;
	return (1);
}

char	**ft_parser_args(const char **arguments, t_args *flags)
{
	char	**args;
	char	*nums_str;
	char	**final_nums;

	args = (char**)arguments;
	nums_str = malloc(1);
	if (!nums_str)
		return (NULL);
	nums_str[0] = '\0';
	ft_initflags(flags);
	while (*args)
	{ 
		if (ft_check_flags(*args, flags) == 0
			&& ft_check_num_list(*args, &nums_str, flags) == 0)
		{
			free(nums_str);
			return (NULL);
		}
		args++;
	}
	final_nums = ft_split(nums_str, ' ');
	free (nums_str);
	return(final_nums);
}
