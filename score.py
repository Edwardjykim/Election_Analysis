score = int(input("What is your test score?"))

if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is an B.')
    else:
        if score >= 70:
            print('Your score is an C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
                