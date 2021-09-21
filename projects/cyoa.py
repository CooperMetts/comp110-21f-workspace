"""NBA Superstar quiz."""

player: str 
points: int   


def greeting() -> None:
    global player
    print("Hello! What is your name?")
    player = input("Enter your name here: ")
    print(f"Hello, {player}, it's nice to meet you!")
    print("This program has two fun quizzes. The first one asks ten questions that gauge which current NBA superstar you are most like. The second quiz does the same thing but with former NBA superstars.") 


def current() -> None: 
    lebron_count: int = 0
    steph_count: int = 0 
    giannis_count: int = 0 
    harden_count: int = 0 
    global points
    global player
    while points < 10:
        answer_one: str = ""
        answer_two: str = ""
        answer_three: str = ""
        answer_four: str = ""
        answer_five: str = ""
        answer_six: str = ""
        answer_seven: str = ""
        answer_eight: str = ""
        answer_nine: str = ""
        answer_ten: str = ""
        if points == 0: 
            print("Which do you prefer: \n A. Tacos \n B. Popcorn \n C. Smoothie \n D. Chicken wings")
            answer_one = input("Type the letter of your answer: ")

            if answer_one == "A": 
                lebron_count = lebron_count + 1
            else:
                if answer_one == "B": 
                    steph_count = steph_count + 1
                else: 
                    if answer_one == "C":
                        giannis_count = giannis_count + 1
                    else: 
                        if answer_one == "D":
                            harden_count = harden_count + 1

        if points == 1:
            print("What type of basketball player are you: \n A. Facilitator \n B. Shooter \n C. Paint beast \n D. All-around scorer")
            answer_two = input("Type the letter of your answer: ")

            if answer_two == "A":   
                lebron_count = lebron_count + 1
            else: 
                if answer_two == "B": 
                    steph_count = steph_count + 1
                else: 
                    if answer_two == "C": 
                        giannis_count = giannis_count + 1
                    else: 
                        if answer_two == "D": 
                            harden_count = harden_count + 1

        if points == 2: 
            print("If you were in the NBA, what would be your top priority: \n A. Winning championships \n B. Money \n C. Loyalty \n D. Playing with your friends")
            answer_three = input("Type the letter of your answer: ")

            if answer_three == "A":
                lebron_count = lebron_count + 1 
            else: 
                if answer_three == "B":
                    steph_count = steph_count + 1
                else: 
                    if answer_three == "C": 
                        giannis_count = giannis_count + 1
                    else: 
                        if answer_three == "D": 
                            harden_count = harden_count + 1

        if points == 3: 
            print("If you were in the NBA, what would you do with your time off: \n A. Read the first page of a book \n B. Stay at home with family \n C. More basketball \n D. Go to the strip club")
            answer_four = input("Type the letter of your answer: ")

            if answer_four == "A": 
                lebron_count = lebron_count + 1 
            else: 
                if answer_four == "B":
                    steph_count = steph_count + 1 
                else: 
                    if answer_four == "C": 
                        giannis_count = giannis_count + 1 
                    else: 
                        if answer_four == "D": 
                            harden_count = harden_count + 1

        if points == 4: 
            print("If you weren’t a basketball player, what would you be: \n A. Football player \n B. Golfer \n C. McDonald's employee \n D. Rapper")
            answer_five = input("Type the letter of your answer: ")

            if answer_five == "A":
                lebron_count = lebron_count + 1 
            else: 
                if answer_five == "B": 
                    steph_count = steph_count + 1
                else: 
                    if answer_five == "C":
                        giannis_count = giannis_count + 1 
                    else: 
                        if answer_five == "D": 
                            harden_count = harden_count + 1

        if points == 5: 
            print("Would you prefer to play for a big or small market team: \n A. Doesn't matter \n B. Big \n C. Small \n D. Wherever my friends are")
            answer_six = input("Type the letter of your answer: ")

            if answer_six == "A":
                lebron_count = lebron_count + 1 
            else:
                if answer_six == "B": 
                    steph_count = steph_count + 1
                else:
                    if answer_six == "C":
                        giannis_count = giannis_count + 1
                    else:
                        if answer_six == "D":
                            harden_count = harden_count + 1

        if points == 6:
            print("Of the following NBA players, which is your least favorite: \n A. Lance Stephenson \n B. Patrick Beverly \n C. Mario Hezonja \n D. Giannis Antetokounmpo")
            answer_seven = input("Type the letter of your answer: ")

            if answer_seven == "A": 
                lebron_count = lebron_count + 1
            else:
                if answer_seven == "B":
                    steph_count = steph_count + 1
                else: 
                    if answer_seven == "C":
                        giannis_count = giannis_count + 1
                    else: 
                        if answer_seven == "D":
                            harden_count = harden_count + 1

        if points == 7:
            print("Of the following NBA players, which is your most favorite: \n A. Carmelo Anthony \n B. Klay Thompson \n C. Khris Middleton \n D. Kevin Durant")
            answer_eight = input("Type the letter of your answer: ")

            if answer_eight == "A":
                lebron_count = lebron_count + 1
            else: 
                if answer_eight == "B":
                    steph_count = steph_count + 1
                else: 
                    if answer_eight == "C":
                        giannis_count = giannis_count + 1
                    else: 
                        if answer_eight == "D":
                            harden_count = harden_count + 1

        if points == 8: 
            print("If you could play on any team in the NBA, which would it be: \n A. LA Lakers \n B. Golden State Warriors \n C. Milwaukee Bucks \n D. Brooklyn Nets")
            answer_nine = input("Type the letter of your answer: ")

            if answer_nine == "A":
                lebron_count = lebron_count + 1
            else: 
                if answer_nine == "B":
                    steph_count = steph_count + 1
                else: 
                    if answer_nine == "C":
                        giannis_count = giannis_count + 1
                    else: 
                        if answer_nine == "D":
                            harden_count = harden_count + 1

        if points == 9: 
            print("What is your least favorite team in the NBA: \n A. San Antonio Spurs \n B. Cleveland Cavaliers \n C. Miami Heat \n D. Golden State Warriors")
            answer_ten = input("Type the letter of your answer: ")

            if answer_ten == "A":
                lebron_count = lebron_count + 1
            else: 
                if answer_ten == "B":
                    steph_count = steph_count + 1
                else: 
                    if answer_ten == "C":
                        giannis_count = giannis_count + 1
                    else: 
                        if answer_ten == "D": 
                            harden_count = harden_count + 1

            if lebron_count > steph_count and lebron_count > giannis_count and lebron_count > harden_count:
                print(f"{player}, your current NBA superstar is Lebron James because you answered {lebron_count} questions the way Lebron would have.")

            if steph_count > lebron_count and steph_count > giannis_count and steph_count > harden_count:
                print(f"{player}, your current NBA superstar is Steph Curry because you answered {steph_count} questions the way Steph would have.")

            if giannis_count > lebron_count and giannis_count > steph_count and giannis_count > harden_count:
                print(f"{player}, your current NBA superstar is Giannis Antetokounmpo because you answered {giannis_count} questions the way Giannis would have.")

            if harden_count > lebron_count and harden_count > steph_count and harden_count > giannis_count:
                print(f"{player}, your current NBA superstar is James Harden because you answered {harden_count} questions the way James would have.")

        points = points + 1


def former() -> None:
    jordan_count: int = 0
    garnett_count: int = 0
    iverson_count: int = 0
    shaq_count: int = 0
    global points
    global player
    while points < 10:
        answer_one: str = ""
        answer_two: str = ""
        answer_three: str = ""
        answer_four: str = ""
        answer_five: str = ""
        answer_six: str = ""
        answer_seven: str = ""
        answer_eight: str = ""
        answer_nine: str = ""
        answer_ten: str = ""
        if points == 0: 
            print("Which do you prefer: \n A. Steak \n B. PB&J \n C. Lasagna \n D. Mac & cheese")
            answer_one = input("Type the letter of your answer: ")
        else: 
            if answer_one == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_one == "B": 
                    garnett_count = garnett_count + 1
                else: 
                    if answer_one == "C":
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_one == "D":
                            shaq_count = shaq_count + 1

        if points == 1: 
            print("What type of basketball player are you: \n A. All-around \n B. Traditional big-man \n C. Offensive juggernaut \n D. Paint beast")
            answer_two = input("Type the letter of your answer: ")

            if answer_two == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_two == "B":
                    garnett_count = garnett_count + 1
                else: 
                    if answer_two == "C":
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_two == "D":
                            shaq_count = shaq_count + 1

        if points == 2:
            print("If you were in the NBA, what would be your top priority: \n A. Winning championships \n B. Playing with friends \n C. Loyalty \n D. Money") 
            answer_three = input("Type the letter of your answer: ")

            if answer_three == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_three == "B": 
                    garnett_count = garnett_count + 1
                else: 
                    if answer_three == "C":
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_three == "D":
                            shaq_count = shaq_count + 1

        if points == 3: 
            print("If you were in the NBA, what would you do with your time off: \n A. More basketball \n B. Play video games \n C. Rap \n D. Make commercials")
            answer_four = input("Type the letter of your answer: ")

            if answer_four == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_four == "B": 
                    garnett_count = garnett_count + 1
                else: 
                    if answer_four == "C":
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_four == "D":
                            shaq_count = shaq_count + 1

        if points == 4: 
            print(" If you weren’t a basketball player, what would you be: \n A. Baseball player \n B. Buisness man \n C. Rapper \n D. Sports analyst")
            answer_five = input("Type the letter of your answer: ")

            if answer_five == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_five == "B": 
                    garnett_count = garnett_count + 1
                else: 
                    if answer_five == "C": 
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_five == "D":
                            shaq_count = shaq_count + 1

        if points == 5: 
            print("Would you prefer to play in a big or small market: \n A. Doesn't matter as long as I can win \n B. Doesn't matter as long as I'm playing with my friends \n C. Small market \n D. Big market")
            answer_six = input("Type the letter of your answer: ")

            if answer_six == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_six == "B":
                    garnett_count = garnett_count + 1
                else: 
                    if answer_six == "C": 
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_six == "D":
                            shaq_count = shaq_count + 1

        if points == 6: 
            print("Of the following NBA players, which is your least favorite: \n A. Isaiah Thomas -- bad boy Pistons one \n B. Lebron James \n C. Kobe Bryant \n D. Hakeem Olajuwon")
            answer_seven = input("Type the letter of your answer: ")

            if answer_seven == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_seven == "B":
                    garnett_count = garnett_count + 1
                else: 
                    if answer_seven == "C": 
                        iverson_count = iverson_count + 1
                    else:
                        if answer_seven == "D":
                            shaq_count = shaq_count + 1

        if points == 7: 
            print("Of the following NBA players, which is your most favorite: \n A. Scottie Pippen \n B. Paul Pierce \n C. Dikembe Mutombo \n D. Kobe Bryant") 
            answer_eight = input("Type the letter of your answer: ")

            if answer_eight == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_eight == "B":
                    garnett_count = garnett_count + 1
                else: 
                    if answer_eight == "C":
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_eight == "D":
                            shaq_count = shaq_count + 1

        if points == 8:
            print("If you could play on any team in the NBA, which would it be: \n A. Chicago Bulls \n B. Boston Celtics \n C. Philadelphia 76ers \n D. LA Lakers")
            answer_nine = input("Type the letter of your answer: ")

            if answer_nine == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_nine == "B":
                    garnett_count = garnett_count + 1
                else: 
                    if answer_nine == "C":
                        iverson_count = iverson_count + 1
                    else: 
                        if answer_nine == "D":
                            shaq_count = shaq_count + 1

        if points == 9: 
            print("What is your least favorite team in the NBA: \n A. Detroit Pistons \n B. Miami Heat \n C. LA Lakers \n D. Houston Rockets")
            answer_ten = input("Type the letter of your answer: ")

            if answer_ten == "A":
                jordan_count = jordan_count + 1
            else: 
                if answer_ten == "B":
                    garnett_count = garnett_count + 1
                else: 
                    if answer_ten == "C":
                        iverson_count = iverson_count + 1
                    else:
                        if answer_ten == "D":
                            shaq_count = shaq_count + 1

            if jordan_count > garnett_count and jordan_count > iverson_count and jordan_count > shaq_count:
                print(f"{player}, your former NBA superstar is Michael Jordan because you answered {jordan_count} questions the way Mike would have.")

            if garnett_count > jordan_count and garnett_count > iverson_count and garnett_count > shaq_count: 
                print(f"{player}, your former NBA superstar is Kevin Garnett because you answered {garnett_count} questions the way Kevin would have.")

            if iverson_count > jordan_count and iverson_count > garnett_count and iverson_count > shaq_count:
                print(f"{player}, your former NBA superstar is Allen Iverson because you answered {iverson_count} questions the way Allen would have.")

            if shaq_count > jordan_count and shaq_count > garnett_count and shaq_count > iverson_count:
                print(f"{player}, your former NBA superstar is Shaquille O'Neal because you answered {shaq_count} questions the way Shaq would have.")

        points = points + 1


def main() -> None:
    greeting()
    print("Would you like to take a quiz to find out which current or former NBA superstar you are? Or would you like to exit the experience?")
    greet_answer: str = input("A. Current \n B. Former \n C. Exit \n Enter your answer here: ")
    global points
    global player
    points = 0
    if greet_answer == "A":
        current()
    else: 
        if greet_answer == "B":
            former()
        else: 
            print(f"Ok. Good bye. Your total adventure points are {points}.")


if __name__ == "__main__":
    main()
