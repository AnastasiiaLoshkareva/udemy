# Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:
# seq = ['soup','dog','salad','cat','great'] - should be filtered down to: ['soup','salad']

seq = ['soup','dog','salad','cat','great']

#formatting into list to get result from filter function 
result_lst = list(filter(lambda word:word[0]=='s',seq))
print(result_lst)


if __name__ == '__main__':
    main()
