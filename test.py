name = input("Type your name here: ")
print("Welcome", name, "to this adventure. I hope you make it to the end.")

answer = input(
    "You are on a high school soccer team. You could commit to a decent college now, or wait one year to get better and commit to a better college. What do you want to do? Type Commit to commit now, or type wait.").lower()

if answer == "commit":
    answer = input("You decide to commit now to the University of Bryant, with a decent soccer team. You are the leading goalscorer for your team. You lead your team to the finals. Suddenly, a rep from Besitkas comes up to you and offers you a huge sum of money to join their team. Do you want to reject and hope that you win the finals and get noticed by a better team? Or do you want to accept and hope you win a finals there? Type Reject or Accept.").lower()
    if answer == "reject":

        answer = input("You stay with Bryant and you end up winning the championship. After the game, you get approached by a rep from Manchester City, the best team in the Premier League, who offers you 100k a week to join the team, which you accept immediately. When arriving at the facilities, you find out you are going to be a backup. Do you want to transfer to a team where you will be a starter? Or do you want to stay? Type Transfer or Stay.").lower()
        if answer == "transfer":
            answer = input("The only offer you get is from an unknown club in Finland. Do you want to transfer or stay with Man City. Type transfer or stay.")
            if answer == "transfer":
                print("You go to Finland, and in your first season. you get injured. You decide to call it quits from soccer with just over a million dollars.")
            elif answer == "stay":
                print

    elif answer == "accept":
        answer = input("You go to Turkey, and play there for 15 seasons, and you become the best player in league history, only to not win the championship each time. You have already made 10s of millions of dollars. Do you want to stay or transfer to another better team? Type stay or transfer.").lower()

        if answer == "stay":
            answer = input("You stay there for 15 more seasons, adding on to your existing records and breaking some new ones, but you still haven't won any. At this point it's been far too long to win another one, with all the young talent arriving each year. Do you want to transfer to a new team or retire? Type transfer or retire.").lower()
            
            if answer == "transfer":
                answer = input("You get an offer from Nottingham Forrest, who are the worst team in the Premier League, for a large sum of money. Do you accept or reject? Type accept or reject.").lower()
                if answer == "accept":
                    print("You finish your career off in peaceful Nottingham, where you are hailed everywhere you go. Your net worth is in the hundreds of millions of dollars, and you feel it is time to hang up the boots, even with no championship.")
                elif answer == "reject":
                    print("You get an offer from Arsenal. But when you get there, you find out you are going to be a reserve, with no playing time and no field action. They win a championship. But everyone knows you didn't have an impact on that championship. You got one, regardless. You retire with what everyone deems is a fake ring.")

            elif answer == "retire":
                print("Congrats, you have retired. You have broken many records, and solidifyed yourself as the greatest player in Turkish SuperLig History, however you never won a championship.")
        elif answer == "transfer":
            answer = input("You get an offer from Manchester United, for about 200k a year. However, you also get an ")
            
elif answer == "wait":
      print("You keep playing for your high school team, however, your 4th game in results to an ACL tear for you, putting you out of the entire season. You decide to find a regular career, better luck next time.")

else:
    print("Not a valid option, sorry.")