# cryptocurrency_price_bot

## Intro

This is an advanced software engineering project. This project should cover 11 different phases. This project is coding a telegram bot for getting the price of cryptocurrencies with some actions like getting charts or comparison coins.

## 1. Git

A git repository was set up and I am going to use git features like branches, pull requests, and GitHub action for my project.

## 2. UML

For this project, I have used three UML diagrams.

<ul>
<li> The <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/tree/main/diagrams/usecase.md'>Usecase diagram</a> which shows the system's usecases and user stories.</li>
<li> The <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/tree/main/diagrams/activity-diagram.md'>Activity diagrams</a> which show flow diagrams, activity and the way they work for each usecase.</li>
<li> The <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/tree/main/diagrams/state-diagram.md'>State diagrams</a> which show state of the system in different conditions and different user input</li></ul>

## 3. DDD

The project has six domains.

<ol>
<li>User interaction</li>
<li>Accounting</li>
<li>Cryptocurrency integration</li>
<li>Notification</li>
<li>Statistics</li>
<li>Charts</li>
</ol>

The
<a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/tree/main/diagrams/ddd-diagram.md'>DDD diagram</a> shows how we separated our system into mentioned domains and how the domains are related to each other.

## 4. Metrics

I used
<a href='https://sonarcloud.io/summary/overall?id=maryam-mohebbi_cryptocurrency_price_bot'>SonarCloud</a> and GitHub action to calculate metrics for our project such as:

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=maryam-mohebbi_cryptocurrency_price_bot&metric=bugs)](https://sonarcloud.io/summary/new_code?id=maryam-mohebbi_cryptocurrency_price_bot)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=maryam-mohebbi_cryptocurrency_price_bot&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=maryam-mohebbi_cryptocurrency_price_bot)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=maryam-mohebbi_cryptocurrency_price_bot&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=maryam-mohebbi_cryptocurrency_price_bot)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=maryam-mohebbi_cryptocurrency_price_bot&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=maryam-mohebbi_cryptocurrency_price_bot)

[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=maryam-mohebbi_cryptocurrency_price_bot&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=maryam-mohebbi_cryptocurrency_price_bot)

## 5. Clean Code Development

In the design part, I used the `autopep8` for matters which follow most of the PEP 8 roles.
I also try to apply clean code rules on my project as we as possible. for example, - I used meaningful names for the functions and variables

<ul>
<li>All functions do only one task</li>
<li>I broke the code into reusable functions</li>
<li>The structure of the code follows the dependency inversion principle</li>
<li>I tried to keep the code as simple and readable as possible</li>
</ul>

<a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/documents/cleancode.md'>Here</a> is a sample of what I did. I also prepare a python <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/documents/clean-code-cheat-sheet.md'>Clean Code Sheat Sheet</a>.

## 6. Build Management

I have used pybuilder for build management. The build file is available <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/build.py'>here</a>.

Build will be run with `pyb --verbose` command with detail of which tests passed and which ones fail and finally build was successful or not.

## 7. Unit-Tests

I create some unit tests for my project. For being clear, I separated the test files based on my components. Test files are available in the `src/test` folder or directly from <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/tree/main/src/test'>here</a>.

## 8. Continuous Delivery

For the continuous delivery pipeline, I used GitHub Action. There are two workflows.

<ol>
<li><b>Metrics:</b> Here I update the metrics via `SonarCloud`</li>
<li><b>Build:</b> Here I used `autopep8` as a linter and `pybuilder` for running the tests and building the project.</li>
</ol>

The file available <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/.github/workflows/build.yml'>here</a>.

## 9. IDE:

My favorite IDE is `Visual Studio Code`. I like it for use very easily, useful extensions, Git integration, and good plugins.I used these shortcuts more than others:

<ul>
<li>Control + Shift + L: Select all same words</li>
<li>Command + D: Select words one after another (not all)</li>
<li>Command + Option + Array key: Select same point of lines</li>
<li>Ctrl+`: Toggle terminal
<li>Command + S: Save</li>
<li>Control + Tab: Scroll next</li>
<li>Control + Shift + Tab: Scroll prev</li>
<li>Command + X: Cut
<li>Command + C: Copy</li>
<li>Command + V: Paste</li>
<li>Command + N:  New File</li>
</ul>

## 10. DSL

I created the <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/documents/dsl.pseudo'>DSL</a> for the Chat Bot based a pseudocode language that describes the functionalities of the bot with a clear understandable language.

## 11. Functional Programming

Throughout the duration of this project, I made an effort to incorporate a functional programming approach as much as feasible.

<ol>
<li>All the functions in the code are side effect free. Examples can be found <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/src/services/utils.py#L1'>here</a>.</li>
<li>You can find examples of functions with parameters and return values <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/src/adapters/coinapi_adapter.py#L26/'>here</a>.
</li>
<li>Examples of higher order functions can be found <a href='https://github.com/maryam-mohebbi/cryptocurrency_price_bot/blob/main/src/adapters/telegram_adapter.py#L9'>here</a>. I passed another function as input for this function to set it as callback.</li>
</ol>
