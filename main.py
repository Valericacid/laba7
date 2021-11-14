def merge(lists):
    lists_new = sum(lists, [])
    length = len(str(max(lists_new)))
    rang = 10
    for i in range(length):
        rang_len = [[] for k in range(rang)]
        for x in lists_new:
            figure = x // 10 ** i % 10
            rang_len[figure].append(x)
        lists_new = []
        for k in range(rang):
            lists_new = lists_new + rang_len[k]
    print(lists_new)

if __name__ == '__main__':
    lists = [1, 4, 5], [1, 3, 4], [2, 6]
    merge(lists)