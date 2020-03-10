import pandas


def read_exce():
    # df = pandas.read_excel('CASETA.xlsx', index_col=[0, 1, 2], skiprows=1, sheet_name='DANUBIO', )
    df = pandas.read_excel('CASETA.xlsx', usecols="B", skiprows=1, sheet_name='DANUBIO', )
    values = df.values

    # print(values)
    for row in values:
        print(len(row))
        for element in row:
            # print(element, end=' ')
            print(element)
        print()
    # print(df)

    # df = pandas.read_excel('CASETA.xlsx', sheet_name='DANUBIO')
    # df = df.head()

    # df2 = df.to_dict()

    # df2 = df.to_csv()

    # for key,val in df2.items():
    #     print(f"K:{key}, Val{val}\n")

    # print(df2)

if __name__ == '__main__':
    read_exce()

    # a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    # for i in range(len(a)):
    #     for j in range(len(a[i])):
    #         print(a[i][j], end=' ')
    #     print()

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()