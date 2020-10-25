# Test Role - Automated Testing

## Workflow for Test Driven Development
When we create an application a test.py file is autoatically created by Django. This is where all of our tests will live. During milestone #3 we built several test cases. Check our [test.py](../../../eShopping_Main/eshop/tests.py) file.

In a Test Driven Development the test drives the progress of the code. Here is how we write and run our test enviroment.

## Workflow
- Write some code.
- Write a test in test.py to test the functionality of the code
- Inside the console, Run 'Python Manage.py test' 
- Check which test cases failed
- Check which test cases passed
- Make necessarry changes to the code and test.py file
- Repeat

## Unit Testing 

Unit Testing is the type of software testing level in which each individual components of a software are tested(geeksforgeeks).

Inside test.py there are two classes. Each class contains multiple functions that test for our code to make sure it is working how its supposed to. The first class is 'ViewsTest', this class was built to test all of the views and templates in our application. The second class in test.py is 'ModelTest', this class is testing all of our models to make sure that objects can be created and retrived without issues. 

## System Testing

System testing is done to check whether the software or product meets the specified requirements or not. System testing involes everything that we have built so far. We are trying to evaluate that our progress is taking us in the right direction that we eventually reach our end goal. We do this type of testing when we go through our workflow, while we test our site locally at 127.0.0.1:8000 and after we have uploaded it to pythonanywhere.

### References
- “Difference between Unit Testing and System Testing.” GeeksforGeeks, 17 May 2019, www.geeksforgeeks.org/difference-between-unit-testing-and-system-testing/. 





