my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = []
revers = my_str[::-1]
sub_str = [revers[revers.find(r_limit):revers.find(l_limit)]]
revers_sub = sub_str[::-1]
print(revers_sub)