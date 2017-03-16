---
layout:     post
header-img: "img/terrorism.jpg"
title:      "Global Terrorism Analysis"
subtitle:   "An interactive tool for visual analysis of global terrorism."
repository: "Terrorism_Analysis"
date:       2017-02-24 12:00:00
author:     "Xianzhi Cao, Master student of Data Science, New York University"
goal:		16
partners:   
  - partner: "New York University - Center for Data Science"
---
Contributors
------------

[![The Center for Data Science - New York University]({{ site.url }}/img/partners/nyu.png)](http://cds.nyu.edu/)

**Prof. Greg Watson - New York University**  
Adjunct Professor Data Science, Center for Data Science  
Senior Research Scientist at Oak Ridge National Laboratory  

**Xianzhi Cao - New York University**  
Master's student - Center for Data Science  

**Caroline Roper - New York University**  
Master's student - Center for Data Science


Introduction
------------

This project aims to provide users with an interactive tool to better understand the pattern of global terrorism attacks.

Our project visualizes the Global Terrorism Database from various perspectives and allows the user to explore the data by customizing our visualizations to meet their needs. Terrorism is an increasing concern despite recent progress along other development goals. The Global Terrorism Database provides a rich resource of information about how terrorism has changed over time and differs by region or country. Our project seeks to make the insights from the data discoverable to all.
This project is part of the United Nations’ ICT4SD (Information and Communications Technology for Sustainable Development) program in the OICT department.

***

Get Started
-----------------

On this page we present you a static version of how this tool looks like. However, in order to customize and interact with all the visualizations, it is recommended to use Jupyter Notebook with related packages installed.

**Dependencies**  
- Python 3.3+  
    
**Mandatory dependencies**  
- Numpy  
- Pandas  
- Matplotlib  
- Seaborn  
- Scipy  
- Basemap  
- Folium  
- Jupyter Notebook  
- Ipywidgets  
- Json  

We have presented a detailed user manual for users lacking the above dependencies.  
- [GTA User Manual](https://docs.google.com/document/d/1KNxP-8Ccey1tM1sOBJRB7VyB3rjtPe2gbDFlHtD_iCk)

***

Dataset
------------
The dataset used for this study is Global Terroriam Database (GTD). The Global Terrorism Database (GTD) is an open-source database including information on terrorist events around the world from 1970 through 2015 (with annual updates planned for the future).
- Contains information on over 150,000 terrorist attacks  
- Includes information on more than 75,000 bombings, 17,000 assassinations, and 9,000 kidnappings since 1970  
- Includes information on at least 45 variables for each case, with more recent incidents including information on more than 120 variables  
- Over 4,000,000 news articles and 25,000 news sources were reviewed to collect incident data from 1998 to 2015 alone  
  
<blockquote><i>National Consortium for the Study of Terrorism and Responses to Terrorism (START). (2016). <i>Global Terrorism Database</i>. Retrieved from https://www.start.umd.edu/gtd </i> </blockquote>


The GTD was designed to gather a wide variety of etiological and situational variables pertaining to each terrorist incident. Depending on availability of information, the database records up to 120 separate attributes of each incident, including approximately 75 coded variables that can be used for statistical analysis. These are collected under eight broad categories, as identified in the GTD Codebook, and include, whenever possible:  
  
 <b>1) GTD ID and Date: </b>  
 - Eventid: Incidents from the GTD follow a 12‐digit Event ID system. 
 - Year, Month, Day, Approximate Date
 - Extended Incident: whether the duration of an incident extended more than 24 hours or not.
  
 <b>2) Incident Information: </b>  
 - Incident Summary: A brief narrative summary of the incident, noting the “when, where, who, what, how, and why.”
 - Inclusion Criteria
 
 <b>3) Incident Location: </b>
 - Country, region, state/province, city, vicinity, Location Description.
 - Latitude and longitude
 - Geocoding specificity
 
 <b>4) Attack Information: </b>
 - Attack Type: 8 categories + unknown. 
    <blockquote><i>"Assassination, Hijacking, Kidnapping, Barricade Incident, Bombing/Explosion, Armed Assault, Unarmed Assault, Facility/Infrastructure Attack, and Unknown".</i></blockquote>
 - Suicide Attack
 
 <b>5) Weapon Information: </b>
 - Weapon Type: 13 categories.
 - Several sub weapon types.
 
 <b>6) Target/Victim Information: </b>
 - Target/Victim Type: 22 categories
 - Several specific target/victim information, including names, nationalities, etc.
 
 <b>7) Perpetrator Information: </b>
 - Perpetrator Group Name: the name of the group that carried out the attack
 - Several sub-group information, including number, claim, motive, etc.
 
 <b>8) Casualties and Consequences: </b>
 - Total Number of Fatalities, including Number of US Fatalities and Number of Perpetrator Fatalities
 - Total Number of Injured, including Number of U.S. Injured and Number of Perpetrators Injured
 - Property Damage, including damage extend, values and comments
 - Total Number of Hostages/ Kidnapping Victims, including US Hostages or Kidnapping Victims, kidnapping hours, countries, total ransom mmount demanded, and number released/escaped/rescued
 
 <b>9) Additional Information and Sources: </b>
  - Additional relevant details about the attack, including International‐ Logistical, International‐ Miscellaneous, and sources.
   
***

Analysis
------------

[![Statistical Overview]({{ site.url }}/img/demo_static/lineplot.png)](https://github.com/ICT4SD/ICT4SD.github.io/blob/master/img/demo_static/lineplot.png)


To analyze the data, we will start with some descriptive statistics of the data. As, the boxplot in the next page suggests (Fig. 1) that among all the middle eastern countries Egypt faced conflicts for longest span of time, whereas countries such as Bahrain, Qatar, and United Arab Emirates faced conflicts for shortest period of time.

<table border="1">
<tr>
  <td></td>
  <td><b>Country</b></td>
  <td><b>Frequency of Conflicts</b></td>
</tr>
<tr>
  <td>1</td>
  <td>Bahrain</td>
  <td>24</td>
</tr>
<tr>
  <td>2</td>
  <td>Egypt</td>
  <td>536</td>
</tr>
<tr>
  <td>3</td>
  <td>Iran</td>
  <td>219</td>
</tr>
<tr>
  <td>4</td>
  <td>Iraq</td>
  <td>5891</td>
</tr>
<tr>
  <td>5</td>
  <td>Israel</td>
  <td>2724</td>
</tr>
<tr>
  <td>6</td>
  <td>Jordan</td>
  <td>2</td>
</tr>
<tr>
  <td>7</td>
  <td>Kuwait</td>
  <td>40</td>
</tr>
<tr>
  <td>8</td>
  <td>Lebanon</td>
  <td>1070</td>
</tr>
<tr>
  <td>9</td>
  <td>Qatar</td>
  <td>1</td>
</tr>
<tr>
  <td>10</td>
  <td>Saudi Arabia</td>
  <td>107</td>
</tr>
<tr>
  <td>11</td>
  <td>Turkey</td>
  <td>4581</td>
</tr>
<tr>
  <td>12</td>
  <td>United Arab Emirates</td>
  <td>1</td>
</tr>
<tr>
  <td>13</td>
  <td>Yemen (North Yemen)</td>
  <td>1450</td>
</tr>
</table>

<b>Table 1</b>: List of countries and their frequency of conflicts

Also if we list the countries according to the frequency of violence faced in this time period, the result (Table 1) shows countries such as Iraq and Turkey are the most frequent to such conflicts, whereas Qatar and United Arab Emirates have faced least amount of conflicts.

The basic intuition from the statistics should be, the places which saw largest number of violence and for longest period of time should count largest number of casualties. However, if we plot the co-ordinates (longitude and latitude) of each conflict area against the number of estimated deaths (Fig. 2), the map suggests apart from countries which are more prone to conflicts (such as Iraq) some of the other countries (such as Kuwait) with less number of conflicts also faced large number of casualties.

[![Choropleth Map]({{ site.url }}/img/demo_static/choro.png)](https://github.com/ICT4SD/ICT4SD.github.io/blob/master/img/demo_static/choro.png)


For this project, we are interested in the hypothetical relation between the duration of conflicts (the number of days one conflict lasts) and the countries as well as the relation between the number of casualties and the countries. So, the research questions we intend to find out are:

- <b>RQ1:</b> Are some of the countries in middle-east more prone to long term conflicts than short-term skirmishes, and
- <b>RQ2:</b> Are some of the middle-east countries are more prone to high casualty conflicts than other countries of the region?

So, the corresponding null hypothesis for the above two relations are respectively:

- <b>H1:</b> There is no significant difference between the countries on number of days each conflict lasts in each individual country.
- <b>H2:</b> There is no significant difference between the countries on number of casualties suffered in conflicts.

So, for this research design, the Duration and High_est are our outcome variables (DVs) whereas the Country is our independent variables (IV). Since we have more than one DV in this case, we will perform a multivariate analysis of variance (MANOVA) to test the significance of IV on predicting the DVs.


[![Heat Map]({{ site.url }}/img/demo_static/heat.png)](https://github.com/ICT4SD/ICT4SD.github.io/blob/master/img/demo_static/heat.png)



[![Bubble Chart]({{ site.url }}/img/demo_static/bubble.png)](https://github.com/ICT4SD/ICT4SD.github.io/blob/master/img/demo_static/bubble.png)


[![Dot Plot]({{ site.url }}/img/demo_static/dotplot.png)](https://github.com/ICT4SD/ICT4SD.github.io/blob/master/img/demo_static/dotplot.png)

Results
------------

We have tested the DVs to check for normality of the distribution. Unless the data is artificially generated by a particular, known distribution, it is often found that any reasonably effective distribution test will reject them. Nevertheless, it can be meaningful to use a goodness of fit statistic, like the KS statistic, to measure the deviation between the distribution of the data and any ideal distribution. Since the sample size of this dataset is larger than what Shapiro-Wilk test can handle (>5000), we have performed the two-sample Kolmogorov-Smirnov test, the result of which on both DVs are presented below:

For <i>High_est</i>:

    Two-sample Kolmogorov-Smirnov test
    data: high_est and m
    D = 0.82891, p-value = 0.4979
    alternative hypothesis: two-sided

For <i>Duration</i>:

    Two-sample Kolmogorov-Smirnov test
    data: duration and m
    D = 0.95362, p-value = 0.3231
    alternative hypothesis: two-sided

<b>Fig 3:</b> Two-sample Kolmogorov-Smirnov test result on both DVs

As, we can see in case of both DVs, the test statistics (<i>p-value</i>) is found to be non-significant, i.e., for both the DVs we fail to reject the null hypothesis which says the distribution of values for each DV is normal.
Next, we check for homogeneity of variance-covariance matrices. Homogeneity of variance-covariance is the multivariate version of the univariate assumption of homogeneity of variance and the bivariate assumption of homoscedasticity. In short, homogeneity of variance-covariance matrices concerns the variance-covariance matrices of the multiple dependent measures (two in this case) for each group. For example, for two dependent variables, it tests for two correlations and four covariances for equality across the groups. The result of testing this assumption is shown below:

    ---------------------------------------------
    armed4$country: Bahrain
             high_est duration
    high_est 0.7173913 0
    duration 0.0000000 0

    armed4$country: Egypt
              high_est duration
    high_est 188.582421 6.122154
    duration 6.122154 262.921464
    ---------------------------------------------
    armed4$country: Yemen (North Yemen)
              high_est duration
    high_est 971.07230 24.52792
    duration 24.52792 10.70436
    ---------------------------------------------

<b>Table 2:</b> Partial snapshot of variance-covariance matrices for individual countries

As the test results suggest, the variances for <i>High_est</i> and <i>Duration</i> are similar for some countries (e.g., Egypt), in some cases the variances are different. So, for this dataset we can interpret that homogeneity of variance-covariance may not hold true for all the countries.

Now that we have tested all the assumptions, next we will proceed for MANOVA. Since the variances and covariances across groups are not exactly similar in our case, we will go for a robust MANOVA. We have performed both Choi and Marden’s robust test as well as Munzel and Brunner’s test, the results of which are compared in the table as shown in the below section:

<table border="1">
  <tr>
    <td><i>mulrank()</i></td>
    <td><i>cmanova()</i></td>
  </tr>
  <tr>
    <td><pre>
    $test.stat
    [1] 1.322191

    $nu1  
    [1] 4.439797

    $p.value
             [,1]
    [1,] 0.255643
    $N
    [1] 33

    $q.hat
              [,1]      [,2]
    [1,] 0.4531680 0.4669421
    [2,] 0.4132231 0.4669421
    </pre>
    </td>
    <td>
    <pre>
    $test.stat
    [1] 16.8481

    $df
    [1] 6

    $p.value    
                [,1]
    [1,] 0.009858016
    </pre>
    </td>
  </tr>
</table>

<b>Table 3</b>: Comparison between the output of <i>mulrank()</i> and <i>cmanova()</i> function


From the output of the <i>mulrank()</i> function, we can see that we have a test statistic for the countries (<i>$test.stat</i>) as well as the corresponding <i>p-value</i> (<i>$p.value</i>). We can conclude that there is no significant main effect of the countries on the aspects of the either duration of conflicts or number of casualties involved, <i>F</i> = 1.32, <i>p</i> = 0.26. Therefore, we fail to reject our null hypothesis from the outcomes of Munzel and Brunner’s method.

However, the output of <i>cmanova()</i> shows a different result, here judging by the test-statistic and <i>p-value</i> (p>0.05) we can say the difference in countries involved has significant effect on the duration of the conflict.

For this experiment, we will go with the outcomes of Munzel and Brunner’s method and assume that outcome of the MANOVA test was non-significant, so we will not run any post-HOC test. So, in conclusion we fail to reject our both null hypotheses H1 and H2.

Limitations
------------

This research is not without limitations. One of the significant limitation of the dataset is that it does not contain data from Syria, the country which is seeing a prolonged civil war since March 2011. So findings of these study can significantly alter once the data from Syria is included in this study. Also from the research design perspective, a more practical approach would be to include other significant factors such as timing of the conflict (<i>Year</i>), the nature of surrounding area of the current conflict zone (up to a certain radius), etc. So, multiple analysis of co-variance (MANCOVA) would be a better experiment than MANOVA for this research design. Other than that, there is also need to see the change in nature of conflicts in terms of duration and casualties over time. So, a time series analysis will be a better alternative to extend this study, which the researcher expects to cover in future work.
Reference


References
------------

- Brams, S. J. (1997). Fair division: A new approach to the Spratly Islands controversy. International Negotiation, 2(2), 303-329.

- Brock, L. (1991). Peace through parks: the environment on the peace research agenda. Journal of Peace Research, 28(4), 407-423.

- Brundtland, G., Khalid, M., Agnelli, S., Al-Athel, S., Chidzero, B., Fadika, L., & Singh, M. (1987). Our common future. World Commission on Environment and Development. Oxford: Oxford University Press.

- Croicu, M., & Sundberg, R. (2015). UCDP Georeferenced Event Dataset Codebook Version 4.0. Journal of Peace Research, 50(4), 523-532.

- Croicu, M., & Sundberg, R. (2016). UCDP GED Codebook version 5.0, Department of
Peace and Conflict Research, Uppsala University

- Gleditsch, N. P. (1998). Armed conflict and the environment: A critique of the literature. Journal of peace research, 35(3), 381-400.

- Lonergan, S. (1997). Water resources and conflict: Examples from the Middle East. In Conflict and the Environment (pp. 375-384). Springer Netherlands.

- Sundberg, R., & Melander, E. (2013). Introducing the UCDP georeferenced event dataset. Journal of Peace Research, 50(4), 523-532.

- Wallensteen, P., & Sollenberg, M. (2001). Armed Conflict, 1989-2000. Journal of Peace Research, 38(5), 629-644.
