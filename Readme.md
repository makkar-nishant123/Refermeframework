THIS FRAMEWORK SHOULD BE ABLE TO AUTOMATE ANY WEBSITE IRRESPECTIVE OF THE TEST CASE PROVIDED.


Framework will perform following : 

-  Automation and perform Test cases for the given website. - Functional / Regression - UI - selenium 
- Reporting - Maybe create reports in PDF format ? - 
        generate a table based report and email to Test engineers 
        analyse and send back with RCA ...... - Class candidates 
- Logs - timestamp + line where it failed etc. - Done 
- Writing results into file verytime we do execution - result.txt file writing - Done 
- Jenkins  + Git = Maybe do CI ??? - Optional  - WIP 
- Snapshots -  during failures or on demand ? - Candidates 
- Retrying Failed TCs in case someone wants to after execution of Test suites - Listner - customized - Candidates
- Cross Browser testing / Cross platform testing - Selenium Grid -Partially Done  
    Chrome
    IE 
    firefox - drivers needed for all 3.
- Multithreading  - Candidates
- Analysis engine - which will decide type of failure in the report based on the failure type. - Partially Done
- Configurable different properties - configparser - Done  
- Flag based execution - Partially Done 
- headless execution ? - will learn abput it! - *chromejs* / phantomjs - Partially Done 
- Performance check !! - unit test library for same. - Not Done  - Candidate 


It will have following : 

- XLS / SQL - data driven approach. - Done 
- Helper classes for UI operations. - Done 
- Test Scripts - text file - Done 
- API ? - THINK/RESEARCH ABOUT HOW WE WILL DO API EXECUTION - Candidates 
- JAVAScript execution  - 
- Unit test libraries like mock,unittest will be used.- - Candidate 


===================Hybrid Approach==========
==Create / Decide Architecture==
- Put all flags and TCs name - xlsx / text file.
 
- Once flag is TRUE , we will run a TC
 
- In TCs :
    UI - selenum 
    SQL/XLS - mysqlclient + xlrd 
    UI / BE validations 
    Logs wherever required - loogers 

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
        Creating reports based on results (analytics) - another feature archiving
        
        
    
        

a. Write helper classes 
b. Decide our test cases.
c. Validate all our test cases 


===Libraries==
a. selenium
b. sqlalchemy
c. mysql-connector-python
d. logging
e. configparser



TASKS - 

a. Candidates - Write atleaset 20 real and good MMT TCs
b. Candidates - Write atleaset 20 real and good oneplus website TCs 
