# Project Name - Build-your-mind
Our app “Build your Mind” consists of an app that helps people to know their political positioning in terms of political parties in Spain.

This app has a main function:
  - It is a survey with a wide range of questions that would position you in a map showing you the political party that corresponds more to your principles based on your opinions and those of the spanish politicians. 

Furthermore, it will inform of news, conferences, meetings of interest through notifications in order to be up to date, and provide a feedback question regarding the event, the user may respond to update their map. 

# INSTALLATION
To be able to run our program, make sure you have the following things installed:

  - Python programming language - It will work in all versions between 3.6 and 3.8. 
  - Libraries - In order to run our program, we make use of the following 3 libraries: matplotlib, tk and statistics  
        To download the library make the following steps:
        1. Once in Pycharm, go to preferences
        2. Then, click python interpreter and click the "+" buttom
        3. Once then, put write the following:
    ```matplotlib ``` 
    ```statistics ```
    ```tk ```
  
  Now that we have the required libraries set up, copy the code in a file you create and run the program

# USAGE
Once the user enters our platform, they will be welcomed to Build your mind and they will be given a brief explanation about our app.
After this, the user will be asked whether to start the initial test or weekly test:    
 
The user will now have to enter their choice. If the choice is to start the initial test; their choice will be  validated and the user will be asked 60 different questions:


1) There will be questions for Y.axis (Authoritatian vs. Libertarian) 
    - **An example**: I’d always support my country, whether it was right or wrong or our race has many superior qualities, compared with other races.
    - **User Input**: The answer will be chosen from a range 1-5 from Completely Disagree to Completely Agree.  
    - **Output**: Here the affirmations are authoritarian, meaning, “Strongly disagree” goes towards Libertarian and “Strongly agree” goes towards Authoritarian. All of this is going to move the position in the graph
  


2) There will be questions for X.axis (Right vs. Left)
     - **An example**: Economic globalization is inevitable, and for me it is ok that it serves primarily the interest of trans-national corporations rather than humanity or Controlling inflation is more important than controlling unemployment.
    - **User Input**: The answer will be chosen from a range 1-5 from Completely Disagree to Completely Agree.  
    - **Output**: Here the affirmations are authoritarian, meaning, “Strongly disagree” goes towards Right and “Strongly agree” goes towards Left. All of this is going to move the position in the graph
  



3) Once you finish all the questions; **Output**:
    - First, the user will be shown the graph with their political position and will be given the digit for the x.axis and the digit for the y.axis (from -2 to 2)
    - Another window will be displayed asking for these values and it will give you a number for a chosen area.   
    - Once you have that area digit, you click on it and it will show which political parties are appropiate for you.

4) Finally, the user will be asked to create a username and password to login








Additionally, if the initial choice was a weekly test:If the choice is to start the initial test:
- First, the user will be asked to enter a key if they want to continue or to enter to quit
- After this, the user will be asked to choose a date.  
 - The user will be given the test and will be asked to enter the results for the x axis and y axis.
 - Finally, a new window will be displayed and the procedure that was explained above will be carried out. 



# SOME EXTRA INFORMATION ABOUT THE CODE
In order to carry out our objective, we have used different tools:
1. CSV: We will tell the user that as a database we will use CSV which will store all his data.
 2. GUI and matplot to create the graphs


 

# CREDITS
The authors for this project are:   
Ana Hidalgo
Cristina Díez
Bea Wahle
Juan Cano and
Olivia Hernández  
