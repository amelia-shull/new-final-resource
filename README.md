# Info 370 Project Proposal
## Amelia Shull, Kateka Seth, Sean Meharry, Kyle Simpson

## Domain
*Our final project will be researching food resources for children.*

Food insecurity is a huge problem for the United States. More than 1 in 7 families experienced food insecurity at some point in 2012 (Hunger in America). Children who facing hunger are more likely to struggle in school, experience developmental impairments, and have more social and behavior problems (Feeding America). Some studies have also shown that child food insecurity and paradoxically lead to child obesity (Olson). However, there are many resources available to help combat food insecurities. There are food banks, meal programs, and grocery programs. For children specifically, there are school breakfast, lunch, and snack programs in place across the country. 

## Research Question
Our primary research question is whether we can determine if food resources provided to students are allocated more heavily to areas where said food is the least needed. For example, school districts bringing in more money from property tax might have more money to spend on food resources for their students, but they might also have the least need for said resources.

## Hypothesis
Our null hypothesis is that there is no prediction for the food resources that students are recieve based on proportionally distributed to areas where the resources are most needed.

## The Data
Our data is pulled from the United States Department of Agriculture (USDA). It over 275 features for all counties in all states. It includes both county level and state level data on the various features. The version we will be using was last updated March 27, 2018, although most features seems to be from 2010-2015. The features we will mostly be looking at are the ones related to children: “Children, low access to store 2010 and 2015”, “Child food insecurity”, and the various food programs available to them. The data set contains information about SNAP participation (Supplemental Nutrition Assistance Program), the national school lunch program, and WIC (supplements for women, infants, and children). Other features we are considering looking at are farmer’s market percentage along with fast food restaurant percentage to try and assess the healthiness of available food options.

## Methods
We plan on using KNN, Decision Trees, & ADA Boost to test our hypothesis. We chose this methods because they are highly used and generalizable machine learning methods that align well with our idea of using regression to understand the many continuous variables presented in our dataset. Their popularity will also help us research various ways of improving their prediction accuracy and troubleshooting any errors that arise while trying to train them.

## Audience
We think our audience is anyone that has decision making powers regarding school funding for food resources. This includes, but is not limited to, PTA board, public school boards, local government employees, & zoning officers. The reason we think these people are critical to our investigation is that if we find a statistically significant link then it would be wise for these people to that into consideration for their planning, fundraising, and overall decision making. More specifically, we think that public school boards might find that things like opening up your food resources to local school district children could greatly alleviate the problem, if one is found. Often, these types of decisions are made based on budgeting and politics regarding keeping money inside their own district, since the money was created by revenue in their district. If these same decisions were instead made based off of statistical significance they might be able to reduce their budget and help more kids.

## Technical Description
We will be creating a static HTML page using markdown to avoid spending our time on creating the page rather than the visuals and data that back it up. Some of the issues I forsee us having are the abundance of features to choose from. Dengue fever had quite a few, but most of them were semi-related to each other and could be semi-explained through rational behind mosquitos. The dataset is also in several different files so data wrangling to get the data we need might end up taking a bit of work. However, with this dataset and our research question we have many unknowns and not much knowledge to go off of before we dive in. Although our lack of biases could help us. 

## Citations
- Kirkpatrick SI, McIntyre L, Potestio ML. Child Hunger and Long-term Adverse Consequences for Health. Arch Pediatr Adolesc Med. 2010;164(8):754–762. doi:10.1001/archpediatrics.2010.117 
- Christine M. Olson; Nutrition and Health Outcomes Associated with Food Insecurity and Hunger, The Journal of Nutrition, Volume 129, Issue 2, 1 February 1999, Pages 521S–524S, https://doi.org/10.1093/jn/129.2.521S
- [Hunger in America](https://phcnpg.org/docs/Welcome%20Page/hunger-in-america-2014-full-report.pdf)
- [Feeding America](https://www.feedingamerica.org/hunger-in-america/child-hunger-facts) 
- [The Hungry and Overweight Paradox](https://www.eatright.org/health/weight-loss/overweight-and-obesity/the-hungry-and-overweight-paradox)
- [USDA Data](https://www.ers.usda.gov/data-products/food-environment-atlas/data-access-and-documentation-downloads/)
