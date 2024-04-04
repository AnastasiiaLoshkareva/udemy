# This code use try-except-else-finally structer to handle errors and exceptions
def handle_exceptions(my_lst,item):
    try:
        index = my_lst.index(item)
    except:
        print(f'in the list there is no item = {item}')
    else:
        print(f'In the list there is an item = {item} with index = {index}')
    finally:
        print('This text will be printed always regardless the result')

#call function for a certain list and a certain item
my_lst = [1,2,3,4]
item = 5
handle_exceptions(my_lst,item)

if __name__ == '__main__':
    main()
