# fin-bytes

## Inspiration
While going through college, we noticed a severe lack of engagement among students regarding financial responsibilities and their fiscal futures. While there's loads of budgeting apps out there that make managing money easier, the process of creating a more financially stable future is one that still remains unclear, due to the vast and confusing ocean of resources present on the internetWe want to make investing more accessible, equitable, and inclusive, and we wish to do that by making the process of learning how to invest easier. 

## What it does
We wish to engage users by sending a packet of helpful and personalized information to their inboxes every week. By taking into account their experience and interests, we design a newsletter with introductory information, relevant and current news articles, and a special quiz catered just for you!

## How we built it
We created a simple website using TypeForm to get responses, and then saved the data in a Firebase database. We used News API to get news articles related to specific interests based on the user. We then cleaned this data, and used GPT 3.5 to scan through it and display the 5 most relevant and popular articles to the user. In addition, we used GPT 3.5 to create weekly snippets of information depending on the user's experience and interests, along with a quiz at the end. The three sections were joined together, and then emailed to each user individually to ensure personalized and intuitive information. 

## Challenges we ran into
Our first challenge was faced when we took a while to understand how to import the data from the Google sheet from the TypeForm to a database. We didn't know the best format to do this in, and later automate the process. We eventually found a workaround using gspread, turned the file to a csv, and then ran through the entries and uploaded them to firebase. 

The second challenge was prompt engineering Open AI, since it often made hallucinations, and returned unnecessary or irrelevant information. This was more of a trial and error process, and eventually we nailed a near perfect rompt. 

Finally, our last challenge was piecing everything together, since all of our files were working individually, but we needed to create a solid pipeline for it to be a one step process. While our code could still do with some cleaning up, we eventually figured out a way to get the program to work. 

## Accomplishments that we're proud of
I think being able to combine all these different functions that neither one of us had known how to deal with earlier - from not even knowing how to use APIs to using 3 of them in the same project, and building a front and back-end with just two people in the team, was a massive success. The glee we felt at seeing the emails pop up on our phones was unparalleled. 

## What we learned
That a project is actually much more different in real life than the ideation stage. We didn't even consider the possibility of creating a database, or having to use a separate API just to get the data from the forms. In addition, there is a lot of scope for optimization to be done to make our code leaner and faster. Scalability would have to include completely redoing our code with a cheaper LLM and more efficient ways of handling data as well. 

## What's next for Fin Bytes
Our short term goals would be to improve the formatting of our emails, and expand the various options we offer in terms of interests for investing. We'd also like to make the news article extraction more robust, and possibly also summarize the 5 articles that are displayed. 

In the long run, we want to create a personalized chatbot on our website where users can ask questions about concepts that they're unsure of. Additionally, we'd like to convert the quizzes to more fun and engaging playable formats, and keep track of each user's data and history, to ensure continuous challenges and learning. 
