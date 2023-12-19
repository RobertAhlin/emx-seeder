# emx-seeder
Tool to seed an predict rider placement for upcoming races.

## Dataset Content
The dataset is sourced from a timing solution at [https://live.emx-timing.se]. From all the races called "Vintercupen 2023". It's an enduro competition serie that include six races with different classes.
They took place at FMKC Skövde, Tidaholms MK, Töreboda MK, Tibro MK, Carlsborgs MK and Falköpings MK.
Each row represents a rider with data like Placement, Class, StartNo., Name, Club, Brand, LapTimes, Laps, TotalTime.

* **Project Terms & Jargon**
	* A client is a person that manage events for motorsport. In this case for Enduro competitions.
	* A rider is an indiviual that are participating in an event.

## Business Requirements
As a Data Analyst and awesome with predicions from my Predictive Analytics course at Code Institute. I can help motorsport, and specially Enduro management to seed riders for upcoming races. Also, individual riders should be able to view their results and how they are trending by they results.

* 1 - The client is interested in seeding riders that has signed up for races, based on their previous results, to get a start list with hopefully the fastest rider first and the slowest last. This to minimize the amount of overtakes the riders have to do.
* 2 - The rider want to follow up on their results to see the trend. If they are getting faster or slower compared to the other riders.


## Hypothesis
* 1 - We know that overtakes while riding enduro in forests on narrow trails can be hard and dangerous. In order to avoid as much overtakes as possible, the start field of riders needs to be seeded.
* 2 - There are manually seeding systems done in excel today, thay require a lot laying hand on manually to fix them to be good.


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
	* For fun, made it possible to se the change of not finish a race (DNF) depening on the brand on motorcycle. Based in historical data of riders DNF.


## Starting up.
1. Installed Jupyterlab, Pandas, Matplotlib and Seaborn - pip3 install jupyterlab pandas matplotllib seaborn
2. Installed Jupyter Notebook - pip3 install notebook
3. Set c.NotebookApp.allow_remote_access = True in jupyter_notebook_config.py
4. Installed required librarys along the way they were needed.

Launch Notebook with: jupyter notebook --NotebookApp.token='' --NotebookApp.password=''
Launch Streamlit app: streamlit run app.py

Codeanywhere workspace got offline and wasn't able to start the Jupyter Notebook again. Just got 403 error. After half a day I switched to VS Code. So that was also a couple of hours learning how to set that up.


## ML Business Case

### Predict Churn
#### Classification Model
* We want an ML model to predict if a prospect will churn based on historical data from the customer base, which doesn't include tenure and total charges since these values are zero for a prospect. The target variable is categorical and contains 2-classes. We consider a **classification model**. It is a supervised model, a 2-class, single-label, classification model output: 0 (no churn), 1 (yes churn)
* Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
* The model success metrics are
	* at least 80% Recall for Churn, on train and test set 
	* The ML model is considered a failure if:
		* after 3 months of usage, more than 30% of newly onboarded customers churn (it is an indication that the offers are not working or the model is not detecting potential churners)
		* Precision for no Churn is lower than 80% on train and test set. (We don't want to offer a free discount to many non-churnable prospects)
* The model output is defined as a flag, indicating if a prospect will churn or not and the associated probability of churning. If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently, there is no approach to predict churn on prospects
* The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
	* Train data - target: Churn; features: all other variables, but tenure, total charges and customerID

### Predict Tenure
#### Regression Model
* We want an ML model to predict tenure levels, in months, for a prospect expected to churn. A target variable is a discrete number. We consider a **regression model**, which is supervised and uni-dimensional.
* Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
* The model success metrics are
	* At least 0.7 for R2 score, on train and test set
	* The ML model is considered a failure if:
		* after 12 months of usage, the model's predictions are 50% off more than 30% of the time. Say, a prediction is >50% off if predicted 10 months and the actual value was 2 months.
* The output is defined as a continuous value for tenure in months. It is assumed that this model will predict tenure if the Predict Churn Classifier predicts 1 (yes for churn). If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently, there is no approach to predict the tenure levels for a prospect.
* The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
	* Train data - filter data where Churn == 1, then drop the Churn variable. Target: tenure; features: all other variables, but total charges and customerID


#### Classification Model
* Before the analysis, we visualized a Regressor pipeline to predict Churn; however, the performance didn’t meet the requirement (at least 0.7 for R2 score, on train and test set)
* We used a technique to convert the ML task from Regression to Classification. We discretized the target into 3 ranges: <4 months, 4-20 months and +20 months. 
* The classification pipeline can detect a prospect that would likely churn in less than four months and a prospect that would likely churn in more than 20 months.
* A target variable is categorical and contains 3 classes. We consider a **classification model**, which is supervised and uni-dimensional.
* Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
* The model success metrics are
	* At least 0.8 Recall for <4 months, on train and test set
	* The ML model is considered a failure if:
		* after 3 months of usage, more than 30% of customers that were expected to churn in <4 months do not churn
* The output is defined as a class, which maps to a range of tenure in months. It is assumed that this model will predict tenure if the Predict Churn Classifier predicts 1 (yes for churn). If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently, there is no approach to predict the tenure levels for a prospect.
* The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
	* Train data - filter data where Churn == 1, then drop the Churn variable. Target: tenure; features: all other variables, but total charges and customerID


### Cluster Analysis
#### Clustering Model
* We want an ML model to cluster similar customer behaviour. It is an unsupervised model.
* Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
* The model success metrics are
	* at least 0.45 for the average silhouette score
	* The ML model is considered a failure if the model suggests from more than 15 clusters (might become too difficult to interpret in practical terms)
* The output is defined as an additional column appended to the dataset. This column represents the cluster's suggestions. It is a categorical and nominal variable, represented by numbers, starting at 0.
* Heuristics: Currently, there is no approach to grouping similar customers
* The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
	* Train data - features: all variables, but customerID, TotalCharges, Churn, and tenure 


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

