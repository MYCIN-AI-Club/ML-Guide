#!/usr/bin/env python
# coding: utf-8

# # FUNCTION
# ## A function is a block of codewhich only runs when it is called.You can pass data known as.
# ## parameters,into a function.A function can return data asa result.Function can becreated in various ways 
# 
# # Creating a function:
# ## In python function is defined usinga 'def' keyword.
# ## Example:
# 
# 
# 
#  

# In[2]:


def my_function():
    print("Creating function")
my_function();


# # Calling a function:
# ## To call a function,use the function name followed by paraenthsis
# ## Example:
# 

# In[3]:


def my_function():
    print("Calling a function")
my_function();


# # Arguments
# ## Information canbe passed into a function as arguments.
# ## Arguments are specified after the function name,inside the paranthesis.You can add as amany argument as you want,just seperate them with a comma.
# ## The following example hasa function with one argument(Fnum).When the function is called we pass alonga first name,which is used insdie a function to printa fullname:
# ## Example:

# In[5]:


def my_function(fnum):
    print(fnum+30)
    
my_function(50);
my_function(40);
my_function(20);


# # Parameters or Arguments?
# ## The term parameter and argument canbe used for the same thing: information that are passed into a function.
# ## From a function perspective:
# ## A parameter is the variable listed inside the parenthesis in the function definition.
# ## A argument is the value that is sent to the function when it is called.
# 
# 
# # Number of Arguments:
# ## By default,a function must be called with the correct number of arguments.Meaning that is function expects 2 arguments,you have to call the function with 2 arguments,not more,and not less.
# ## Example:
# ## This function expects 2 arguments and gets 2 arguments.

# In[10]:


def my_function(fname1,fname2):
    print(fname1+" "+fname2);
my_function("Vanshita","Srivastava");


# ## This function expects 2 arguments if you give 1 or 3 you will get an error:
# ## Example:
# ## This function expects2 arguments but will get only 1

# In[11]:


def my_function(fname1,fname2):
    print(fname1+" "+fname2);
my_function("Vanshita");


# # Arbitary Arguments, *args
# ## If you do not know how many arguments that will be passed into your function,add a * before the parameter name in the function definition.
# ## This way the function will recieve a tuple of arguments,and can item accordingly.Arbitrary Arguments are often shortened to *args in Python documentations.
# ## Example:
# ## If the number of arguments is unknown, add a * before the parameter name:

# In[13]:


def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Yash", "Vivek", "Varun")


# # Keywords Arguments
# ## You can also send arguments with the key = value syntax.This way the order of the arguments does not matter.The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
# ## Example:
# 

# In[15]:


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Yash", child2 = "Vivek", child3 = "Varun")


# # Arbitrary Keyword Arguments, **kwargs
# ## If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.This way the function will receive a dictionary of arguments, and can access the items accordingly.Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
# ## Example:
# ## If the number of keyword arguments is unknown, add a double ** before the parameter name:
# 

# In[18]:


def my_function(**kid):
    print("Her last name is " + kid["lname"])

my_function(fname = "Vanshita", lname = "Srivastava")


# # Default Parameter Value:
# ## The following example shows how to use a default parameter value.If we call the function without argument, it uses the default value:
# ## Example:
# 

# In[19]:


def my_function(color = "Red"):
    print("I love color " + color)

my_function("Blue")
my_function("Black")
my_function()
my_function("Orange")


# # Passing a List as an Argument:
# ## You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# ## If you send a List as an argument, it will still be a List when it reaches the function.
# ## Example:
# 
# 
# 

# In[21]:


def my_function(food):
    for x in food:
        print(x)

food = ["burger", "maggi", "fries"]

my_function(food)


# # Return Values:
# ## To let a function return a value, use the return statement:
# ## Example:
# 

# In[23]:


def my_function(x):
    return 5 * x

print(my_function(0))
print(my_function(7))
print(my_function(19))


# # The Pass Statement:
# ## Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# ## Example:

# In[24]:


def myfunction():
    pass


# #  Recursion:
# ## Python also accepts function recursion, which means a defined function can call itself.When a function calls a function within itself it is called Recursion.Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# ## In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
# 
# # Recursion Example
# 

# In[26]:


def t_recursion(x):
    if(x > 0):
        result = x+ t_recursion(x - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
t_recursion(6)


# In[ ]:




