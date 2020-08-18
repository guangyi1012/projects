# projects
### Data science related projects

Background: During the COVID-19 pandemic, our research facility require everyone works in the Hillman Cancer center(HCC) building to fill in a web form created with office form online to track daily activity, and to identify close contact personnel if anyone was infected.
 This form include a lot of repetitive information needed to be fill in, like name, PI name, location, have you been exposed to virus etc. other questions  like date and in/out time. the answers are relatively stable for someone work in the building routinely, so a pre-set computer program could help with this tedious work.

purpose: To autofill the webform with a python program. 

Design: looked for ways to manipulate on the webpage,  found selenium package(this is a package used for testing web apps by mimicking human interaction with it). The basic idea is that the package use webdriver(not totally understand, seems like a port that browsers have for developers) as a handle for us to do things on the page, like input, click (that was the only two I used). 


here is how it works:   
  1. download webdriver of your browser.   
  2. Create a webdriver object specifically for a certain browser.that opens up a target webpage.   
  3. use the developer tool on the browser to find the xpath of the html object you want to manipulate.  
  4. find the object with certain xpath.  
  5. do click or input on the object.  
  6. after you finish, you can use a .quit() to shut down the webdiver.
