# Python Clean Code Cheat Sheet

## 1. DRY (Don't Repeat Yourself)

This principle states that you should avoid repeating the same code or logic multiple times in your program. Instead, you should create reusable functions or classes that can be called multiple times.

### Example:

Instead of writing the same print statement multiple times in your code, you can create a function called "print_message" that takes a message as an argument and then call that function whenever you want to print the message.

### Or

Instead of writing the same calculation code in multiple places in your program, you can create a function that does the calculation and call that function whenever you need to perform the calculation.

## 2. KISS (Keep It Simple, Stupid)

This principle states that you should keep your code as simple and easy to understand as possible. Complex code can be hard to understand and debug, so it's best to keep things simple.

### Example:

Instead of using a complex algorithm to calculate the average of a list of numbers, you can simply use the built-in sum() and len() functions to add up all the numbers and divide by the number of items in the list.

### Or

Instead of using fancy, complex algorithms to sort a list of numbers, you can use a simple sorting algorithm like bubble sort.

## 3. SOLID

This is a set of five principles that are meant to be followed together, and they are SRP, Open-Closed, Liskov Substitution, Interface Segregation and Dependency Inversion. These principles help to make your code more maintainable and scalable.

### Example:

Instead of having a single class that performs multiple tasks, you can break it down into smaller classes each with a single responsibility.

## 3.1 SRP (Single Responsibility Principle)

This principle states that each function or class in your code should have a single, specific responsibility.

### Example:

Instead of having a single function that both accepts user input and performs a calculation, you can create two separate functions: one for accepting input, and another for performing the calculation.

## 3.2 Open-Closed Principle

This principle states that a class or function should be open for extension but closed for modification. This means that you should be able to add new functionality to a class or function without modifying the existing code.

### Example:

Instead of modifying the existing "calculate_total" function to handle a new tax rate, you can create a new class called "TaxCalculator" that inherits from the original "calculate_total" class and overrides the appropriate methods.

## 3.3 Liskov Substitution Principle

This principle states that objects of a superclass should be able to be replaced with objects of a subclass without affecting the correctness of the program.

### Example:

Instead of having separate classes for "Rectangle" and "Square", you can create a single "Shape" class with a "set_width" and "set_height" method, and then have "Square" inherit from "Shape" and override the "set_width" and "set_height" methods to ensure that the width and height are always equal.

## 3.4 Interface Segregation Principle

This principle states that a class should not be forced to implement interfaces it doesn't use.

### Example:

Instead of having a single "Automobile" interface that requires a class to implement methods for both driving on the road and flying in the air, you can create separate "RoadVehicle" and "AirVehicle" interfaces that each require a class to implement only the appropriate methods.

## 3.5 Dependency Inversion Principle

This principle states that high-level modules should not depend on low-level modules, but both should depend on abstractions.

### Example:

Instead of having the "Order" class depend directly on the "Inventory" class, you can create an "InventoryService" interface that the "Order" class depends on, and then have the "Inventory" class implement that interface.

## 4. YAGNI (You Ain’t Gonna Need It)

This principle means that you should only write code that is needed for the current task at hand. Don't write code for future features that may never be needed.

### Example:

Instead of creating a function to handle a future feature that you think you might need, you should only add functionality to your code as it is needed for the current project or task.
###Or
Instead of writing a complex system to handle multiple types of user input, you can just write the code to handle the input you currently need.

## 5. DRY-RUN

This principle means that you should test the code in your head by running through it step by step before you start writing. This helps you to think through any potential issues and helps you to write better code.

### Example:

Before writing a function that takes a list of numbers and returns their sum, you can dry-run the function in your head by going through the steps of the function with a sample list of numbers.

## 6. LOD (Law of Demeter)

This principle means that an object should only interact with its immediate neighbors. A class should not reach deeply into the structure of another class.

### Example:

Instead of having a class that directly accesses the properties of another class, it can have a method that returns the required information.

## 7. Test-Driven Development (TDD)

This principle states that you should write automated tests for your code before you write the actual code. This helps to ensure that your code is working as expected and that any future changes do not break existing functionality.

### Example:

Instead of writing the code for a new feature and then testing it manually, you can write a test that describes the expected behavior of the feature, and then write the code to make the test pass. This helps to catch any bugs early on and makes it easier to refactor your code without introducing new errors.

## 8. Code Readability

This principle means that the code should be easy to read and understand. This makes it easier for other people (or even yourself) to understand and modify the code.

### Example:

Using meaningful variable names and comments to explain what the code is doing.

### Or

Instead of using short variable names like "i" or "x", you should use descriptive variable names like "index" or "counter" that clearly indicate the purpose of the variable. Also, you should use appropriate indentation and whitespace to make your code more readable.

## 9. Error Handling

This principle states that you should anticipate and handle errors in your code to prevent unexpected behavior or crashes.

### Example:

Instead of leaving a potential "null" value unchecked, you should add a null check before using a variable and either handle the error or throw an exception.

### Or

Instead of crashing the program, you can use try-except block to catch the exception and show a meaningful message to the user.

## 10. Code Reusability

This principle means that the code should be written in such a way that it can be reused in other parts of the program or in other programs.

### Example:

Creating a function for a specific task, that can be used in multiple parts of the program or in different programs.

## 11. Performance

This principle means that the code should be optimized for performance.

### Example:

Instead of using a slow algorithm, you can use a faster algorithm that takes less time to run.

## 12. Modularity

This principle states that you should break your code into small, independent modules that can be reused and combined in different ways.

### Example:

Instead of having a single large class that does everything, you can create smaller classes that each have a specific responsibility and can be used together to build the larger functionality.

## 13. Naming Convention

This principle states that you should choose descriptive and consistent names for your variables, functions, and classes.

### Example:

Instead of using variable names like "a" or "b", you should use meaningful names like "user_name" or "total_price" that clearly indicate the purpose of the variable. And also, use a consistent naming convention throughout your project, such as using camelCase for variable names.

## 14. Code Review

This principle states that you should have other developers review your code before it is deployed to production. This helps to catch any errors or potential issues early on and also helps to spread knowledge about the codebase.

### Example:

Instead of committing your code directly to the production branch, you can create a pull request and have other developers review your code and provide feedback. This helps to ensure that your code is of high quality and that any issues are identified and addressed before it is deployed.

## 15. Comments

This principle states that you should add comments to your code to explain what it is doing and how it works.

### Example:

Instead of having a hard-to-understand code, you should add comments to your code explaining the logic behind it and how it works. This makes it easier for other developers to understand what your code is doing, and also helps you to remember how your code works when you come back to it later.
