def permutation(data, n, ans, lst):
    if n == 0:
        lst.append(ans)
    for i in range(len(data)):
        new_data = data[:i] + data[i + 1:]
        permutation(new_data, n - 1, ans + data[i], lst)
    return lst


data = '01234567'
n = 5
if len(data) >= n and sorted(list(set(data))) == sorted(list(data)):
    lst = permutation(data, n, "", [])
    print(lst)
    count = 0
    for ans in lst:
        if '1' not in ans and ans[0] != '0':
            for i in range(len(ans)):
                if ans[i] in ans[:i] + ans[i + 1:]:
                    break
            else:
                for i in range(len(ans) - 1):
                    if int(ans[i]) % 2 == int(ans[i + 1]) % 2:
                        break
                else:
                    count += 1
                    print(ans, count)
else:
    print('Данные не корректны')
