
#Copilot Shortcuts Linux

| Shortcut | Description |
| -------- | ----------- |
| `tab` | Accept suggestion |
| `alt+enter` | Show 10 suggestions |
| `alt+/` | Show suggestions |
| `alt+[` | Show previous suggestions |
| `alt+]` | Show next suggestions |
| `ctrl+alt+i`, `ctrl+shift+c` | Chat |
| `ctrl+i` | Chat inline |
| `ctrl+l` | Clear the session |
| `ctrl+enter` | Insert into code |
| `ctrl+alt+enter` | Insert into terminal |
------------------------
# What is GitHub Copilot?
  - Very Advanced Auto Completion Code
  - Write Repetitive Code
  - Its a LLM
  - Its a SSaS product, everyone uses the same LLM

# Writing Code with GitHub Copilot
- Autocompletion features and capabilities
- Working with different languages and frameworks
- Customizing suggestions and feedback loops

# Copilot Features and Capabilities
  - Code Autocompletion
  - Converting Comments to Code
  - Ctrl + i Commands
  - Code Refactoring
  - Chat Window
  - Slash Commands
  - Boilerplate Generation
  - Translating from one library/framework to another
  - Updating code to the latest version
  - As long as there's enough public code for the library on Github, Copilot can help
  - Using Copilot for code documentation
  - AI-assisted PRs
  - 
# Copilot for Documentation
  - Generate explanatory comments for code
  - Highlight code, then use the /doc command
  - The /explain command is nice too

# Github Copilot Benefits
  - Increased Productivity
  - Learning and Development
  - Code Diversity
  - Supports Multiple Languages
  - Reduced Coding Errors

# Github Copilot Drawbacks
  - Accuracy Concerns
  - Potential Security Risks
  - Over-reliance Risk
  - Privacy and Intellectual Property
  - Cost Factor
  - Limited Context Understanding
  - Cannot not be trained our own code and standards
 
 
# Code Autocompletion
- write a function name to get suggestions.
- Write comment and get code suggestions. Control+Enter will give suesstions
- using Copilot and then use optioms like-  Can Fix trhe code, Can explain the code, generate documentation
- Write comment and give an example. This will give suggestions
- contril+i -> ask copilot to write code. ask copilot to write car with properties and methods
- select the code and then press control+i, ask the copilot.. refactor this function so that the code to do this in more simpler steps
- select the code and then press control+i, add "/" it gives different options ike doc, explain, fix, tests
- select the code and then press control+i, add "/test" add "use mocha" and then "use mocha and chai" and then generate test cases. See how it works. It creates a seperate file.

# Code Refactoring
- select the code and then press control+i, ask the copilot.. refactor this function so that the code to do this in more simpler steps
- select the code and then press control+i, ask the copilot.. rewrite this as and arrow function. (corresponding in python can be lambda)
-  ask the copilot.. rewrite this code from class component to function component in React
-  ask the copilot.. rewrite update the code with latest version, is very good. Little bit behid but good enough.
-  Rewrite code from Angular to React
-  user the chat to rewrite the code in different language. "rewrite this code in python". "rewrite all this code in python" -> this will use the open files as input.
-  

# Generate test data
- create a file test-data.js
- generate an array of 10 user with name, age and e-mail (in Copilot chat)
- actually i want users to have realistic names and e-mail. just hardcode names and e-mails. (in Copilot chat)
- copy paste the code in the file and try to rector. select the code and the conrile+i, "add amdid property to each user", "add id property which has uuid as each user", "add hard coded uiud for each user"


# Getting Better Suggestions
- "If you want to change the output, first change the prompt"
- Refine iteratively
- Be specific about the framework/library/strategy you're using
-  Use Copilot a lot
- keep writing different function name and parameters to get better suggestions (getPercentiles(number)
- /test "just log out the result calling duntions with different data"
- /test "don't user mocha and chai, just use console.log"
- "Create a function that inserts a users name, age, and e-mail into a paragrah tas and returns an html string."
- we can ask from Copilot Chat - "Do you see any code vulnerability in this code" user code generated code from above to do this.

# Code Refactoring 2
- First write python func tion to
- "rewrite this into an advanced python function that accepts a validated enum and generate the appropriate regex
- use the chat more than auto completion
- It uses open files as context

# Github
- Add comments to pull request
- Do PR code review using github copilot
- 
---------------------------
# Copilot Chat Can
  - Generate unit test
  - Generate documentation
  - Generate code for a specific task
  - Explain code
  - Propose code fixes
  - Answer coding questions

# Prompt Engineering Tips
  1. Goal
  2. Clarity
  3. Context
  4. Refine   

# WARNING Copilot Chat
- Limited scope
- Potential for bias
- Security risks
- Inaccurate code
- Matches with public code

-  Github link - https://github.com/ldynia/workshop-github-copilot-chat
   
