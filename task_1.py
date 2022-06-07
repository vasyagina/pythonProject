def my_code(wlib):
    for key, value in wlib.items():
        if type(wlib[key]) == str:
            print(key + ": ", value, sep =' \n \t')
        else:
            my_code(value)

lib1 = {'first': 'first_value', 'second': 'second_value'}
lib2= { '1': { 'child': '1/child/value' }, '2': '2/value'}

my_code(lib1)
my_code(lib2)
