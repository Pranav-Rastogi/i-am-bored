import random


ideas = [["Go on a walk", "Challenge yourself to leave your cell phone in your purse or pocket. Admire the view. Stop and smell the roses."],
		 ["Organize something", "Don't tackle a huge organizational project like your closet. Instead, choose something small and manageable."],
		 ["Do your laundry", "You'll thank me later when you have clean clothes to wear."],
		 ["Visit unroll.me", "Visit Unroll.me and unsubscribe from all those emails you never read nor want to get."],
		 ["Do sit-ups", "Fit body, here you come!"],
		 ["Watch music videos", 'Here are some of my favorites to get you started:\n\t"AfterHours" by Troyboi\n\t"Work from home" by Fifth Harmony\n\t"Look What you made me do" by Taylor Swift\n\t"High Rated Gabru" by Guru Randhawa'],
		 ["Strengthen your brain", "Sign up for a Lumosity account and play a couple of brain games"],
		 ["Change up your décor scheme", "Restyle your study table. Put your lamp in a new place."],
		 ["Call an old friend", "Call an old friend you haven't talked to in forever. Catch up or leave a friendly message.",],
		 ["Update your résumé", " Even if you're not in the market for a new job, make sure it's up to date. Add in some recent accomplishments."],
		 ["Try your hand at painting", "Find a paint-by-numbers print you like, put your Picasso hat on, and start painting."],
		 ["Take a bath", "Why not? Let yourself relax!"],
		 ["Set up an online dating profile", "Set up an online dating profile for a website or app you've never tried before."],
		 ["Research places to volunteer", "The next time you start to feel bored, head to one of the places that sounded interesting and rewarding to you."],
		 ["Download the Bitmoji app", "Make your personalized emoji, and then send all your friends fun cartoon texts."],
		 ["Plan a party", "Need a reason?\n\thttp://www.mydomaine.com/reasons-to-throw-a-party"],
		 ["Take a power nap", "Adult napping has many health benefits. Catch up on your z's now."],
		 ["Read up on current events", "Figure out what is happening in the world right now. Go to TheSkimm or The New York Times and get caught up on the news."],
		 ["Get lost on Pinterest", "Pinterest is full of ideas"],
		 ["Watch TV", "It's perfectly okay to unwind in front of the television."],
		 ["Do a puzzle", "Do a puzzle. Or a crossword! They are free in virtually every newspaper in India"],
		 ["Make lists", "List your goals, what you look for in a partner, languages you wish to learn, places you wish to visit, etc. Refer to these lists in the future."],
		 ["Go to the library", "Find a section of books that you enjoy, check out a few, and take them home to read."],
		 ["Learn how to tie a necktie and bow tie", "Impress the gentleman in you with your skills the next time you go to a wedding."],
		 ["Sign up for a class", "Improv, calligraphy, hip-hop, tennis-commit to attending at least five sessions before you give up."],
		 ["Go through the photos on your phone", "Delete anything that you don't need."],
		 ["Teach yourself the army alphabet", "Its official name is the NATO phonetic alphabet. You've heard it: Alpha, Bravo, Charlie, Delta, Echo..."],
		 ["Learn how to give a proper foot massage", "Surprise a loved one to practice the technique."],
		 ["Organize the apps on your phone", "Delete any that you have not used in the past four months."],
		 ["Play a game", "Pull out an old-school board game, pack of cards, or your computer and play a game."],
		 ["Google adorable baby animal photos", "Whether you're into teacup pigs, baby penguins, or young lions, find pictures and overload on cuteness."],
		 ["Figure out a way to make more money", "1. Become a tutor\n2. Sell your junk\n3. Do odd jobs\n4. Invest in domain names\n5. Design something and sell it on Etsy\n6. Give driving lessons"],
		 ["Update your gadgets", "Make sure you're using the latest operating system on your computer and that your smartphone is up to date"],
		 ["Drink a full glass of water", "Dehydration can make you sluggish. If you're tired and bored, pour a glass of water and drink it."],
		 ["Update your personal finances", "Check your savings and checking accounts. Where can you cut back and save more?"]
]


choice = 'y'
while(choice=='y'):
	print("\n")
	i = random.randint(0, len(ideas)-1)
	print(ideas[i][0])
	print(ideas[i][1])
	print("Do you want another suggestion? (y/n): ", end='')
	choice = input()
