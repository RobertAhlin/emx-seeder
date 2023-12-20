# emx-seeder
Tool to seed an predict rider placement for upcoming races.

# CRISP-DM

![CRISP-DM ilustration](readmefiles/crisp-dm.png)

The CRoss Industry Standard Process for Data Mining (CRISP-DM) is a process model that serves as the base for a data science process. It has six sequential phases:

1. Business understanding – What does the business need?
2. Data understanding – What data do we have / need? Is it clean?
3. Data preparation – How do we organize the data for modeling?
4. Modeling – What modeling techniques should we apply?
5. Evaluation – Which model best meets the business objectives?
6. Deployment – How do stakeholders access the results?

# Business understanding
In the motorsport of Enduro. There are several security aspects to consider. A lot can be managed by good knowledge and keep to the regulation by the event management. But one aspect is the riders themselves. According to the Swedish Enduro Regulations, if a driver is caught, according to the regulations, he must let a faster driver pass. When driving fast on narrow paths in the forest it can be hard to do this safe. And it's up to the slower rider to make let the faster driver pass in a safe way. Of course, there are drivers who during the competition become very competitive and do not want to let anyone pass. In order to minimize the amount of passes needed to be done. Riders are often seeded, with the fastest rider starting first. Seeding riders is always a hard thing to do and often creates irritation among some drivers who think they are faster than they are. Today's seeding system is often up to the "person in charge of timing" and the skills and knowledge of how to seed is very different, therefore seeding can be off. If a ranking system of riders can be handels via ML and AI. The seeding system can be correct.

## Hypothesis
* 1 - We know that overtakes while riding enduro in forests on narrow trails can be hard and dangerous. In order to avoid as much overtakes as possible, the start field of riders needs to be seeded.
* 2 - There are manually seeding systems done in excel today, thay require a lot laying hand on manually to fix them to be good.

# Data understanding
The dataset is sourced from a timing solution at [https://live.emx-timing.se]. From all the races called "Vintercupen 2023". It's an enduro competition series that include six races with different classes.

# Data preparation
The competitions took place at FMKC Skövde, Tidaholms MK, Töreboda MK, Tibro MK, Carlsborgs MK and Falköpings MK. The data can be expanded by adding results from earlier years. But for this project the results from year 2023 will be good enough.
Each row represents a rider with data like Placement, Class, StartNo., Name, Club, Brand, LapTimes, Laps, TotalTime. The data is in Swedish, but I think any english speaking person will still understand the data.
To collect the data I first tried using Pandas to collect data from a table at a specified URL. As that was not successful, I also tried using Beatuifulsoup. That didn't work either because of the tables where generated by JavaScript. I think there are solutions to handle that but I didn't want to spend that amount time to test and try so I decided to manually copy the tables into commadelimited CSV-files and made some manual cleaning of unwanted colums. But I choosed to keep some data I know I didn't want, in order to use Jupyter Notebook to load the data into dataframes and clean the data and save to new csv-files.


## Business Requirements
As a Data Analyst and awesome with predicions from my Predictive Analytics course at Code Institute. I can help motorsport, and specially Enduro management to seed riders for upcoming races. Also, individual riders should be able to view their results and how they are trending by they results.

* **Project Terms & Jargon**
	* A client is a person that manage events for motorsport. In this case for Enduro competitions.
	* A rider is an indiviual that is participating in an event.

* 1 - The client is interested in seeding riders that has signed up for races, based on their previous results, to get a start list with hopefully the fastest rider first and the slowest last. This to minimize the amount of overtakes the riders have to do.
* 2 - The rider want to follow up on their results to see the trend. If they are getting faster or slower compared to the other riders.


## Use ML to rank a rider from a prediction of how well the rider can perform.
* **Business Requirement 1:** Predict seeding from ranking based on historical results.
	* We will inspect the data available from previous events.
	* Based on lap times, and dropping the slowest lap from each competition, get a "real" average time for each rider.
	* Be able to provide a start list with names of riders and compare the names of riders to sort out a seeded list.
    * We want to predict riders result based on old results.

* **Business Requirement 2:** Data Analysing
	* We want a rider to be able to look up themself or any other rider to present a diagram of results and see a trend line.
	* We want a rider to be able to compare themself to other riders. Upp to 5 max.

* **Bonus**
	* For fun, made it possible to se the chance of not finish a race (DNF) depening on the brand on motorcycle. Based in historical data of riders DNF.


# Modeling

It was hard to understand what models to use for this project. I ended up using Pandas and Matplotlib.
I tried using Scikit-learn library, XGBoost, Linear Interpolation, K-Nearest Neighbors (KNN) and Multiple Imputation by Chained Equations (MICE).

# Evaluaton
With Pandas and Matplotlib I felt that I had control over what was happening. Using other models just seem to mess up the data and the outcome was not as I expected.
I tried various plots but nothing really made sense to the Business Requirement. But still fun to try and test to learn.

# Work progress

## Starting up.
1. Installed Jupyterlab, Pandas, Matplotlib and Seaborn - pip3 install jupyterlab pandas matplotllib seaborn
2. Installed Jupyter Notebook - pip3 install notebook
3. Set c.NotebookApp.allow_remote_access = True in jupyter_notebook_config.py
4. Installed required librarys along the way they were needed.

Launch Notebook with: jupyter notebook --NotebookApp.token='' --NotebookApp.password=''
Launch Streamlit app: streamlit run app.py

Codeanywhere workspace got really slow and at one time it went offline and I wasn't able to start the Jupyter Notebook again. Just got 403 error. After half a day trying to solve it, I switched to VS Code. So that was also a couple of hours learning how to set that up.

### Jupyter Notebook

The work of taking care of, cleaning and sorting data was made using Jupyter Notebooks.

# Deployment

## IDE and hosting.
- Github - For version control and hosting work.
- Codeanywhere - Started working in the Codeanywhere IDE. But soon I got frustrated with it being slow and have issues so choosed not to continue with it.
- Visual Studio Code - Installed it on my computer and learned how to connect it to both github and heroku.
- Heroku - to make final deployment and run the Streamlit application.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick project summary
* Quick project summary
	* Summary
	* App Structure
	* Key Functionalities
	* Main Data Used
	* Features
	* Next Steps


### Page 2: Seeding Riders
* Before the analysis, we knew we wanted this page to answer business requirement 1. 
* After data analysis, it should be a possibility to downlaod a file with seeded riders: 
	* State business requirement 1
	* Able to upload a commadelimited csv-file with rider participating in an upcoming event. File columns must be: 'Place of event,Year,#(StarNo.),Namn(Name),Klubb(Club),Märke(Brand),Klass(Class),'
	* Process the file data
	* Download a new csv-file containing seeded riders.
	* Visually see the seeded riders on the page.

### page 3: Riders rank 2023
* State business requirement 2:
	* Select a Klubb (Swedish for Club)
	* Select one or more riders
	* Plot a line chart for selected riders to se their ranks during competitions

### Page 3: Brand DNF Chance
* Bonus:
	* Select a brand from used motorcycle brands during competition and see how likely they will get a DNF.


### Page 4: About
* Descriptions about this project.

## Credits

- https://www.datascience-pm.com/crisp-dm-2/ - for the image of CRISP-DM
- https://chat.openai.com/ - ChatGPT to get help to fix issues and get advice on how to use models.
