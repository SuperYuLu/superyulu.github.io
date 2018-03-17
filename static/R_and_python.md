# Compare python (pandas) and R in data science   


## Data types   
- Python:
  - float
  - int
  - string
  - boolean 
  - 
- R:
  - numerics 
  - characters
  - logical 

## function str()  
In python, str() converts input to string type, while in R str() is to print out the structure of a element (like type() in python).  

## list  
List in both R and python can be composed of mixed datatypes, but in R the list element can be named, yes, just like dictionary in python. There is also difference in dictory index. In python, one has to d A['element'] with 'element' as the key to select the value of 'element', while in R one has to use double square bracket like A[['element']] or A$element, otherwise using A['element'] will give $'element' value\_of_element.

## Index  
- Python  
  - index 0 for the 1st elements 
  - Non-inclusive index range, e.g. A[0:9] doesn't include A[9]
  - implicit index: e.g. A[:3,1], A[:, 1]
- R
  - index 1 for the 1st elements 
  - Inclusive index range, e.g. A[0:9] doesn't include A[9]
  - implicit index: e.g. A[,1], A[1:3, 1]

## Print  
In python the print() function is so powerfull that you can print mixed types in a single line, while in R, you have to use paste() fucntion so that diferent segment can be combined together, e.g. 'This is number x' given x = 10

## Logical Operators  
In Python and R, the logical operators works pretty much works the same, such as '&' for and, '|' for or, '!' for not. However, while python works with chanined operators like 3 < x <= 6, R doesn't like this kind of expression, one has to do 3 < x && x <= 6  

## Condinal statements  
In python, use if, elif, else with comma followed, while in R use if { } else if {} else {}. One more differece is that, in R the else{} statement has to close follow the closing '}' of the preceeding if{} statement, one cannot write the else{} part in a newline ! Same applies for else if{}.  

## While loop  
There is no big difference of while loop in Python and R, except that R uses c-like tyle (e.g. while(){}), both can have break in side.  

## For loop  
Similar to while, the for loop in R works like for(){}, where in the (), one can have python-like interation such as i in list_A or i in 1:length(A). One big difference is that, python uses continue to skip one iteration, while R uses next.  

## Function  
The funcitions in R and python are pretty much similar, still, R follows C style, function goes like funcname <- function(arg1, arg2, ...){ return()}, here "return" is optional, the last sentence of a R function can just be a expression, such as "x + y", which will be returned automatically. One thing one has to notice is that, R passes arguments by value, means that an R function cannot change the variable that you input to that function. While in python, the variable cannot be changes unless the variable is list, dictonary, set, tuple, etc.

## Packages  
R basic functions are from base package, plot use "ggvis" package, to install, use install.packages(). load package = atach to search list, library("package name"), search() loaded packages.

## Map and lapply()
map() in python is what lapply() in R. Annoymous function is R is what lambda function in python. Since in R when difining a function one has to specificly do something like: functionName <- function(){}, thus anoymous function in R is use function(){}, a function that has no name! lapply() app.
