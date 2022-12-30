name = input("Type your name here: ")
print("Welcome", name, "to this adventure. I hope you make it to the end.")

answer = input("You are on a high school soccer team. You could commit to a decent college now, or wait one year to get better and commit to a better college. What do you want to do? Type Commit to commit now, or type wait.").lower()

if answer == "commit":
    answer = input("You decide to commit now to the University of Bryant, with a decent soccer team. You are the leading goalscorer for your team. You lead your team to the finals. Suddenly, a rep from Besitkas comes up to you and offers you a huge sum of money to join their team. Do you want to reject and hope that you win the finals and get noticed by a better team? Or do you want to accept and hope you win a finals there? Type Reject or Accept.").lower()
    if answer == "reject":

        answer = input("You stay with Bryant and you end up winning the championship. After the game, you get approached by a rep from Manchester City, the best team in the Premier League, who offers you 100k a week to join the team, which you accept immediately. When arriving at the facilities, you find out you are going to be a backup. Do you want to transfer to a team where you will be a starter? Or do you want to stay? Type Transfer or Stay.").lower()
        if answer == "transfer":
            answer = input("An offer you get is from an unknown club in Finland. Do you want to transfer or find another team. Type transfer or find.").lower()
            if answer == "transfer":
                print("You go to Finland, and in your first season. you get injured. You decide to call it quits from soccer with just over a million dollars.")
            elif answer == "find":
                answer = input("After waiting for a long time, you get an offer from Lyon. With no other choices, you go there. As you arrive at the facilities, you find out that Lyon is in last place and is in shambles. With no money, no other options, and no way to go, you have two choices, to retire, and go back to Bryant and pursue a major, or stay in Lyon and deal with it. What do you want to do? Type retire or stay").lower()
                if answer == "retire": 
                    print("You had a short lived career. You won't be known for anything soccer related, but you live a good life after getting your major at Bryant, out of the spotlight.")
                elif answer == "stay": 
                    print("Just like that, Lyon get relegated and you have nothing to do but be part of the collapse. You are known in history as part of the worst team in Ligue 1 history. After the season is over you retire shamefully.")
        elif answer == "stay":
            answer = input("You stay on the bench for about 75% of the season, but the top tier striker, Erling Haaland, gets injured. You get your chance to shine, but you have to follow in some very tough footsteps. You do good for yourself, but in the final game that decides whether you win a championship or not, it comes down a penalty. You have the final shot, it is 4-4. If you make this, the trophy is yours, but if you miss, the trophy goes to Liverpool. Do you want to hit the ball left or right?").lower()
            if answer == "left":
                print("The goalkeeper goes right, and you score. Congrats, you have won your first trophy. As your career goes on, you score more goals and get more championships, not just in the premier league, but in the champions league and the world cup as well. As you retire, you are highly regarded as one of the greatest players of all time.")
            elif answer == "right":
                answer = input("The goalkeeper goes right and it gets blocked. Liverpool have won this time. As time passes, you start to win championships, in the world cup and in the champions league, but you can't seem to win one in the premier league. You could stay one more year, with one more chance, or you could retire. Type stay or retire").lower()
                if answer == "stay":
                    print("You stay for one more year, and you get that trophy you have been wanting. You retire peacefully, officially completing your career.")
                elif answer == "retire":
                    print("You retire without that one league win that you wanted, but still overall an amazing career.")
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
            answer = input("You get an offer from Manchester United, for about 200k a year. However, you also get an offer from Galatasary, the best team in the SuperLig, for about only 75k a year. Do you want to go to Man United or Galatasary? Type England for Man United or Turkey for Galatasary.").lower()
            if answer == "england":
                print("You go to Manchester United and you play there for 10 seasons, however they get relegated in the middle of your time there. Defeated, you decide to retire, with lots of money but no championship.")
            elif answer == "turkey":
                  answer = input("You go to Galatasary, and immediately become a starter. You make it to the final game of the season, against your old team, Besiktas, and the winner of this game will win the finals. Fast forward to the end of the game. The 90th minute with 1 minute of stoppage time. It is 3-3. You're running with the ball, inside the opponents penalty box, and then you get fouled, resulting in a penalty. You can shoot the ball left or right. Where do you want to shoot?").lower()
                  if answer == "left":
                    print("The goalkeeper has gone right, and the ball goes in as the final whistle has blown. Congrats, you just won your first trophy! After all that stress, you decide to retire as the hero of the Turkish SuperLig.")
                  elif answer == "right":
                    print("The goalkeeper has gone right. But his hands can't properly get a touch on your shot, and the ball goes in as the final whistle has blown. Congrats, you just won your first trophy! After all that stress, you decide to retire as the hero of the Turkish SuperLig.")
elif answer == "wait":
      print("You keep playing for your high school team, however, your 4th game in results to an ACL tear for you, putting you out of the entire season. You decide to find a regular career, better luck next time.")
else:
    print("Not a valid option, sorry.")