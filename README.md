The Project consists of 3 phases. 

First one is Scraping data from RedBus app.
Second one is to store the Scraped data to a SQL server.
Third one is to create an application to filter and present required data.

The data scraping consists of collecting Route names, Route links, Bus type, Bus name, Seat availability, Rating, Price, Departure time, Reaching time and Duration.
To do this automatically, I've used Selenium with Python automation techniques. 
For some Bus Routes the automation might change due to low availability of bus. To avoid such encounters, we can modify the code simply by commenting unnecessary lines of code.

To store the scraped data I've used Xaamp local server and created a dataframe for government bus and private bus seperately.

Finally with the help of streamlit, I've created an application that can filter and project the necessary data with respect to dynamic change in data.
