# emx-seeder
Tool to seed an predict rider placement for upcoming races.

* **Project Terms & Jargon**
	* A client is a person that manage events for motorsport. In this case for Enduro competitions.
	* A rider is an indiviual that are participating in an event.

## Business Requirements
As a Data Analyst and awesome with predicions from my Predictive Analytics course at Code Institute. I can help motorsport, and specially Enduro management to seed riders for upcoming races. Also, individual riders should be able to view their results and how they are trending by they results.

* 1 - The client is interested in seeding riders that has signed up for races, based on their previous results, to get a start list with hopefully the fastest rider first and the slowest last. This to minimize the amount of overtakes the riders have to do.
* 2 - The rider want to follow up on their results to see the trend. If they are getting faster or slower compared to the other riders.
* 3 - The rider want to see how they are performing in their class for each competition based on placement.



## Hypothesis and how to validate?
* 1 - We know that overtakes while riding enduro in forests on narrow trails can be hard and dangerous. In order to avoid as much overtakes as possible, the start field of riders needs to be seeded.
* 2 - There are manally seeding systems done in excel today, thay require a lot laying hand on manually to fix them to be good.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1:** Data Visualization and Correlation study
	* We will inspect the data available fromo previous events.
	* Based on lap times, and dropping the fastest and slowest lap from each competition, get a "real" average time for each rider.
	* Be able to provide a start list with names of riders and compare the names of riders to sort out a seeded list.
    * We want to predict riders result based on old results.

* **Business Requirement 2:** Cluster and Data Analysis
	* We want a rider to be able to look up themself or any other rider to present a diagram of results and see a trend line.
	* We want a rider to be able to compare themself to other riders. Upp to 5 max.



Starting up.
1. Installed Jupyterlab, Pandas, Matplotlib and Seaborn - pip3 install jupyterlab pandas matplotllib seaborn
2. Installed Jupyter Notebook - pip3 install notebook
3. Set c.NotebookApp.allow_remote_access = True in jupyter_notebook_config.py
4. Installed BeautifulSoup
5. Installed Selenium

Launch Notebook with: jupyter notebook --NotebookApp.token='' --NotebookApp.password=''

Codeanywhere workspace got offline and wasn't able to start the Jupyter Notebook again. Just got 403 error. Switched to VS Code.
