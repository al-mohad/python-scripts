

def main():
    print('Tests')
    check_YesNo()


def check_YesNo():
    answer = ''
    kontinue = input("Do you want to continue? ")
    while kontinue != 'no':
        if kontinue == 'yes':
            print('Ok let\'s continue')
            break
        else:
            print('Invalid answer')
            check_YesNo()
            break
    else:
        print('Done')


main()
