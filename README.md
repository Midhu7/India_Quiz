# India_Quiz
A Quiz website using Django

## Key Features
1. Random question set of 5 questions
  Every time a user attempts the quiz, the questions shown will be a random set of questions from the Question Model. For the prototype, only 5 questions are used for each quiz.Questions can be added to the quiz from the Django Admin by creating a superuser.
2. User Authentication
  A user has to sign up or login to the platform to attempt the quiz and the results of every attempt will be stored in Attempt Model.
3. A Public Leaderboard
  Even an unregistered user gets access to the view the leaderboard. Every user in the platform is given a rank based on their highest score in the quiz.

##Database Modelling
1. Question  model
  Model to store all questions with their options
2. Answer Model
  Model to store answers to corresponding questions
3. Attempt Model
  Model to store details of each attempt by each user, including the number of correct and wrong answer, total score, etc.
4. Highscore Model
  Model to store the highscore of every user. Each user will have one and only one highscore.
  
Database used : SQLite3
