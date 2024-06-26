#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
topics_new = ["Celebrities", "Collecting Things", "Losing Things",
              "Feeling Bored", "Singing", "Memory", "Crowded Place",
              "Music", "Cakes", "Money", "Colour", "Social Media",
              "Sunglasses", "Advertisement", "Video Games"]
topics_old = ["Study", "Work", "Home and Accommodation", "Hometown",
              "Chatting", "Transport", "Noise", "Run", "Film",
              "Helping Others", "Fishing", "Clothes", "Map",
              "Musical instruments", "Tea and Coffee", "Robot"]
questions = ["""
Who is your favourite celebrity in your country?
What kind of famous people do you often see in the news?
Do you pay Attention to famous people in the news?
Do you believe that the news about famous people in the media is true?
Would you like to be a famous person in the news?

Why do some people like to collect things?
Where do they collect things?
Do you collect things?
Are there any things you keep from childhood?
Would you keep old things for a long time? Why?
Where do you usually keep things you need?

Do you often lose things?
What can we do to avoid losing things?
Why do some people tend to lose things more often than others?
What will you do if you find something lost by others?

Do you often feel bored?
When would you feel bored?
What do you do when you feel bored?
Do you think childhood is boring or adulthood is boring?

Do you like singing?Why?
Have you ever learned how to sing?
Who do you want to sing for?
Do you think singing can bring happiness to people?

Are you good at memorising things?
Have you ever forgoAen something that is important?
What do you need to remember in your daily life?
How do you remember important things?

Is the city where you live crowded?
Is there a crowded place near where you live?
Do you like crowded places?
Do most people like crowded places?
When was the last me when you were in a crowded place?

Do a lot of people like music?
What kind of music do you listen to?
Is it easy to learn music?
Do you have music lessons at school?

Do you like to eat cakes or other sweet foods?
Do you like to eat cakes as a child?
Can you make cakes?
Are there any traditional Chinese cakes?
Do you like to have desserts after meals?

Do you spend a lot of money?
How do you save money?
What do you think about payment apps or mobile payments?
Do you use a credit card to buy things?
Do you think cash will still be popular in the future?

What is your favourite colour?
What colour car would you like to buy?
What colours do your friends like most?
What colour makes you uncomfortable in your room?

When did you start using social media?
Do you think you spend too much time on social media?
Do your friends use social media?
What do people often do on social media?

Do you often wear sunglasses?
Do you spend a lot of money on sunglasses?
Do you give sunglasses as gifts?
Have you ever lost your sunglasses?

Is there an advertisement that made an impression on you when you were a child?
Do you see a lot of advertising on trains or other transport?
Do you like advertisements?
What kind of advertising do you like?

Do you play video games?
Would you watch others play video games?
Do you think people spend too much time playing video games?
Do you prefer playing video games alone or with others?
""", """
Are you a student or are you working right now?
What's your favourite subject?
Why did you choose this major? Who helped you to choose this major?
What was your first day at school like?
How much  time do you spend on studying every day?
What do you like most about your study?
Does your major/study live up to your expectation?
Which do you prefer, studying in the morning or in the afternoon?
Which do you prefer, studying alone or with others?
What kind of subjects are often considered as challenging?

Do you like your job?
What do you find most interesting about your work/job?
What is the most important quality of a co-worker/colleague?
Which matters to you more, the job itself or the people you work with?
Have you ever changed your work before?
Do you think you will change your job in the future?
What was your first day at work like?
What do you want your company to improve?
What kind of jobs are popular in China?
Would you like to go to another country to work?

Do you live in an apartment or house?
Do you like your apartment or house?
What is your house or apartment like?
What views can you see through the windows?
What kind of apartment or house do you want to have in the future?
Which part of your country are you from?

Where are you from?
How long have you been living there?
Is your hometown a big city or a small city?
Do you like your hometown?
Are there anything you dislike about your hometown?
Has your hometown changed over the years? What are the changes?

Do you like chatting with friends?
What do you usually chat about with friends?
Do you prefer to chat with a group of people or with only one friend?
Do you prefer to communicate face-to-face or via social media?
Do you argue with friends?
What kind of clothes do you like to wear?

How do you go to work/school?
What's the most popular means of transport in your hometown?
How far is it from your home to school/work?
Do you think people will drive more in the future?

Do you lik to stay in a place with a lot of noise?
Do you think there is too much noise in today's world?
Is making noise one of people's rights?

Do you go running a lot?
Where do you usually go running?
What do you think of running as a form of exercise?

What films do you like?
Did you often watch films when you were a child?
Did you ever go to the cinema alone as a child?
Do you often go to the cinema with your friends?
Do you think going to the cinema is a good way to spend time with friends?

Do you usually help people around you?
How do you usually help people around you, such as neighbors, family, and friends?
Do your parents teach you to help others?
Did your parents help you a lot when you were young?

Is fishing popular in your country?
Do you like eating fish?
Have you ever been to a place where there were lots of fish around you?
Have you seen any movies with lots of fish?

What kind of clothes do you like to wear?
Do you prefer to wear comfortable and casual clothes or smart clothes?
Do you like wearing T-shirts?
Do you spend a lot of time choosing clothes?

Do you often use maps?
Do you use paper maps?
How often do you use maps on your phone?
Do you have maps at home?

Have you ever learned to play a musical instrument?
What musical instrument do you enjoy listening to the most?
Do you think children should learn to play an instrument at school?
Do you think music education is important to children?

Do people like tea and coffee nowadays?
Do you prefer to use tea or coffee to serve your guests?
When was the last time you had a cup of coffee?
Do you usually buy your coffee in a coffee shop?

Are robots important?
Would robots affect people's lives?
Have you ever watched a movie about robots?
Should we let a robot drive for us for long journeys?
What can robots do for you at home?
"""]

ques = questions[0].split('\n')[1:-1]
print(topics_new[0])
i = 1
for each in ques:
    if each == '':
        print(topics_new[i])
        i += 1
    else:
        print(each)

ques = questions[1].split('\n')[1:-1]
print(topics_old[0])
i = 1
for each in ques:
    if each == '':
        print(topics_old[i])
        i += 1
    else:
        print(each)
