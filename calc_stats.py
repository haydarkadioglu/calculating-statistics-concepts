def mode(vector):
    """
    :type vector: list
    """

    vector.sort()

    rep_try = 0
    rep_num_list = []
    rep_num = 0
    mode_nums = []
    

    for i in range(0, len(vector)):

        if vector[i] == vector[i - 1]:
            rep_num = rep_num + 1
        else:
            rep_try = rep_num + 1
            rep_num = 0

            if len(rep_num_list) == 0:
                rep_num_list.append(rep_try)
            else:
                if rep_num_list[0] < rep_try:
                    rep_num_list[0] = rep_try
                    

    for i in range(0, len(vector)):

        if vector[i] == vector[i - 1]:
            rep_num = rep_num + 1
        else:
            rep_try = rep_num + 1
            rep_num = 0

            if len(rep_num_list) == 0:
                pass
            else:
                if rep_num_list[0] == rep_try:
                    rep_num_list[0] = rep_try
                    mode_nums.append(vector[i - 1])

    mode_nums.sort()
    ret = f"(Mode: {mode_nums}, Repeat: {rep_num_list[0]})"  
    return ret


def mean(vector):
    """
    :type vector: list
    """
    len_vect = len(vector)
    if len_vect <= 1:
        return vector
    else:
        return sum(vector)/len_vect


def median(vector):
    """
    :type vector: list
    """
    vector.sort()
    len_vect = len(vector)
    if len_vect % 2 == 1:
        return int(vector[len_vect // 2])
    else:
        temp_val = len_vect // 2
        return (vector[temp_val - 1] + vector[temp_val]) / 2


def sd(vector):
    """
    :type vector: list
    """
    stan_dev = 0.0
    len_vect = len(vector)
    if len_vect <= 1:
        return stan_dev
    else:
        mean_loc = mean(vector)
        for an in vector:
            stan_dev += (float(an) - mean_loc) ** 2
        stan_dev = (stan_dev / (len_vect - 1)) ** 0.5
        return stan_dev


def variance(vector):
    """
    :type vector:list
    """
    return sd(vector) ** 2


def skewness(vector):
    """
    :type vector:list
    """
    return 3*(mean(vector) - median(vector)) / sd(vector)


def kurtosis(vector):
    """
    :type vector:list
    """
    len_vect = len(vector)
    mean_loc = mean(vector)
    sd_loc = sd(vector)
    kurt = 0.0
    if len_vect <= 1:
        return kurt
    else:
        for an in vector:
            kurt += ((float(an) - mean_loc ) / sd_loc)** 4
        kurt = (kurt / len_vect) - 3
        return kurt

