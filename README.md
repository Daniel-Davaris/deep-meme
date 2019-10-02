# Deep-meme
A neural network for meme analysis, classification and lifetime expectancy 

## Getting Started

This project began using simple statistical methods to make label predictions, as such the linear_regression.py file can be run using the regression requirements while the neural network model can be run using the network requirements. 
## Requirements

In order to get the linear regression program working, the following packages must be installed:
  * matplotlib
  * sklearn
  * pandas


### Running the program

The following program has only been tested with [Python verison 3.7.4](https://www.python.org/downloads/release/python-374/) 

 Run 
```
linear_regression.py
```


## Running the network model

The network model is comprised of several files with separate functions. First the data is scraped from the Reddit API. The data is then imported through CSV to the data preparation file which converts the data into the appropriate form for the network model. 

## Requirements

In order to get the linear regression program working, the following packages must be installed:
  * praw
  * opencv-python
  * h5py
  * keras
  * tensorflow



### This file will export the reddit API as CSV data

run
```
scraper.py
```
Once the [exported_data.csv] has exported to the working directory run
```
data_prep.py
```
Data prep will perform several functions including regularisation, converting the data into objects and labels as well as the necessary h5 object conversions.


## Executing the network 
The model can now read in the data.h5 file and begin making predictions 

run
```
CNN.py
```

These predictions can then be saved as a pre-trained model which is exported as model.h5 

Execute the test file

run

```
run.py
```


## Authors

*   [**Daniel Davaris**](https://github.com/Daniel-Davaris)

*   [**Stephan Kashkarov** ](https://github.com/Stephan-kashkarov)
