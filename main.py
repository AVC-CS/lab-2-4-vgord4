def main():

    og_str = 'Python Programming'
    ##################################################
    # Comlete your code here
    ##################################################

    sub1 = og_str.split()[0]
    sub2 = og_str.split()[1]
    merged_str = (sub2 + " " + sub1)

    print(sub2)
    print(sub1)
    print(merged_str)

    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
