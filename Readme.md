Framework will perform following : 

-  Automation and perform Test cases for the given website. - Functional / Regression - UI 
- Reporting - Maybe create reports in PDF format ?
- Logs - 
- Writing results into file verytime we do execution 
- Jenkins  + Git = Maybe do CI ???
- Snapshots -  during failures or on demand ? 
- Retrying Failed TCs in case someone wants to after execution of Test suites
- Cross Browser testing / Cross platform testing - Selenium Grid - 
    Chrome
    IE 
    firefox
- Multithreading 
- Analysis engine - which will decide type of failure in the report based on the failure type.
- Configurable different properties 
- Flag based execution
- headless execution ? - will learn abput it!


It will have following : 

- XLS / SQL - data driven approach.
- Helper classes for UI operations.
- Test Scripts - Python 
- API ?
- JAVAScript execution 
- Unit test libraries like mock will be used.


===================Hybrid Approach==========
==Create / Decide Architecture==
- Put all flags and TCs name - xlsx / text file.
 
- Once flag is TRUE , we will run a TC
 
- In TCs :
    UI 
    SQL/XLS
    UI / BE validations
    Logs wherever required 

- Utilities/Helper:
    Before execution : 
        Data Setup 
        Data reading etc...
    During execution : 
        UI
        BE - SQL/Linux etc.
        config_parser - Multhireading , cross browser etc.
        logs 
     After Execution  
        Reporting - Will be called after all test cases are done.
        Listeners -  Retrying failures.
        Writing results
     End
        Archiving data
        Creating reports based on results (analytics)
        
        
    
        

a. Write helper classes 
b. Decide our test cases.
c. Validate all our test cases 


===Libraries==
a. selenium
b. 
c. 