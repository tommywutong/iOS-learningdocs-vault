---
title: 'Quality control in application development without unit testing | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/01/high-quality-in-software-development.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:20c242b89e3eae84'
translated: false
---

> 原文：[Quality control in application development without unit testing | Cocoa with Love](https://www.cocoawithlove.com/2010/01/high-quality-in-software-development.html)　·　Cocoa with Love (Matt Gallagher)

In my last two posts, I've shown a [Mac app with full unit tests](https://www.cocoawithlove.com/2009/12/sample-mac-application-with-complete.html) and an [iPhone app with full unit tests](https://www.cocoawithlove.com/2009/12/sample-iphone-application-with-complete.html). The reality though is that I do not write or test code this way. In this post, I look at why so few applications are actually developed using unit tests. I'll also look at the alternate approaches — both manual and automated — that are normally used to maintain high quality and low bug rates in application development.

## Introduction

I have many friends who love unit tests. They never write code without writing the unit tests first. And they love it; the thought of writing code without unit tests seems foolish and scary to them. Test-first approaches ensure that they never write anything that isn't specified and unit tested.

This post is not to dissuade these people from unit tests. If you already know that you know and love unit tests, then stick with them.

But even unit testing advocates should remember that unit tests are about code-level specification and working within certain types of development methodology — they do not attempt to catch all bugs.

This post is primarily for people who have heard of unit tests and are wondering if they are an efficient way to maintain product quality and lower bug rates.

The short answer is: no. If you simply want to lower bug counts, the best and most efficient approach is through system tests.

## Difficulties of unit testing for application development

Depending on your development methodology, unit tests can serve a number of different functions. But if used purely to detect bugs then they are a very high cost approach for low return.

Unit tests don't test the overall program, only isolated units. This creates many holes (integration, timing, re-entrancy, inter-module communication) that need to be tested another way. These limitations are not unique to application development so I'll focus instead on something that is: the difficulty of isolating your units for testing.

Advocates of unit testing claim that you can follow good program design and reduce coupling and integration, making tests easy to write.

Unfortunately, in application development, that's not exactly possible.

As I noted when I was [discussing iPhone application design](https://www.cocoawithlove.com/2009/12/design-of-iphone-application.html), the code that you write in a Cocoa application is mostly controller classes — since the model and view classes are so reusable, you rarely need to write them yourself.

Controller classes are the classes which link your program together — they join model and view elements together to make your program. The entire purpose of these classes is coupling. The unit tests I wrote for the [WhereIsMyMac program](https://www.cocoawithlove.com/2009/12/sample-mac-application-with-complete.html) were approximately three times the size of the original code due to large numbers of mock objects and tricky hackery to intercept calls into the Cocoa framework — and this was a simple sample application, it could easily be much worse. Every mock object reduces the accuracy of the test by reducing the reality of the test environment and the risk of false positives or negatives in test results.

Since controller classes are so common in applications and the main role of a controller class is to join different objects together, unit testing suffers from the following serious problems in application development:

- Requires huge amounts of mocking code and other fakery (time consuming).
- The resulting tests are far removed from the integrated reality, making false positives and false negatives highly likely and leaving large holes that are simply not tested.

## System testing methodologies for application development

The best approach for testing an application is to accept the coupled, integrated, timing dependent, environment dependent nature and test everything in place. The idea is simple: test the complete program in the exact manner (or as close as possible) in which you expect it to be used.

Tests which operate in this manner are classed as "[system tests](http://en.wikipedia.org/wiki/System_testing)".

The reason why system tests are the most efficient and accurate form of product testing is simple: if you want to ensure low bug rates for the user, test the program in the same way that the user will use it; don't test a fake environment and don't test at levels the user can't access.

### Types of system testing

There are lots of ways to system test your code. In order from most important to least important for application development:

1. [Sanity testing](http://en.wikipedia.org/wiki/Sanity_test)
2. [User interface testing](http://en.wikipedia.org/wiki/GUI_software_testing)
3. [API testing](http://www.logigear.com/newsletter/api_vs_unit.asp)
4. [Regression testing](http://en.wikipedia.org/wiki/Regression_testing)
5. [Performance testing](http://en.wikipedia.org/wiki/Performance_testing)
6. [Load testing](http://en.wikipedia.org/wiki/Load_testing)
7. [Scalability testing](http://en.wikipedia.org/wiki/Scalability_testing)

I'm not going to give full definitions of these tests here — I'm simply going to discuss their importance to applications and related projects. Follow the links to read more about each one.

Every good application has point 2 and most have 3 and 4 as part of their regular testing methodology — sanity checks occur as part of the development methodology (run your code before you commit) and fall outside formal testing.

The important step in making system tests work is to keep them formalized. If the test is not automated, then it should be formally documented so that each of the steps is correctly run during a testing phase. A basic or ad hoc approach to any of these points doesn't count though: proper quality comes from rigorous and clearly defined testing approaches.

### User interface testing

User interface testing is normally performed using testing matrices. In its simplest form, this means a document containing all user interface test cases in a table — a spreadsheet, workprocessor or TextEdit document, it doesn't really matter as long as it is documented.

The rows in the table are all steps in operating your program (selecting menu items, operating buttons, perform edit operations). Every single user interface element in the program should be tested and most should be tested multiple ways to account for different expected effects.

The columns are all environmental differences between runs. Different operating system versions, different computers, different installation settings or different builds of the application (lite, demo or full).

Each cell in the table should then contain the observed result and an indication of whether this is a success or failure according to the specification.

If you can automate the process, then great — there are software tools that will help with this on the Mac. If you can't — yes, user interface testing will get manual and tedious but ultimately, it is the only way to guarantee that the program works as expected. Most of the programs you use have simply had someone sitting in front of them, progressively clicking all the buttons and using all the controls — for every test case in every version.

You need to have the whole table documented and it needs to cover every element of the user interface. The purpose is to remind you to test everything (bad luck will ensure that failure to test a row will guarantee that it contains uncaught bugs).

### API testing

In theory, user-interface testing should test everything in a user facing application. It may seem inefficient to suggest API testing (which is normally done for libraries and code modules).

There are three reasons that any substantial application would want API tests:

- Human testers of user-interfaces are lazy, forget or make mistakes
- API tests are automated and can be run at build-time or as part of continuous integration
- You can test issues that may not be obvious during user testing (like data coherency)

For user applications though, it presents the problem that you must create an API layer that can actually be programmatically tested. The common approach is to separate the "model" of your application into a separate module with an API layer.

API testing is similar to unit testing in many respects:

- it is automated
- can be implemented using OCUnit or similar libraries
- can be used to develop your application using test-first methodologies

The difference is that API tests do not separate the units within the module. API tests test the whole module in-place, fully integrated. This means that the API tests can be quite removed from the implementation details — which has the advantage that they can be more easily written by a separate programmer or test engineer, freeing up programming resources. API tests also aim to be optimally efficient: they only test inputs and outputs and don't care about how intermediary steps in the transformation occurs.

API tests attempt to provide a realistic environment and data but do suffer from some of the same limitations as unit tests in that some parts of the environment must be synthetic (the full application will not be present during testing).

### Regression tests

After you're happy that your program is working as intended, regression tests ensure that subsequent work doesn't screw it up.

These are tests are normally used for programs that produce a file output. Their operation is basically: run the regression test and compare the output to the "known good" result which was saved previously. If the output changes unexpectedly, the test fails.

For many file producing projects (like a few major open-source projects specializing in video codecs, PDF renderers, DVD authoring packages) this is the only test they include. However, it's all that these types of project require: a good set of regression tests should have high code coverage (exercise almost all of the program) and perform most of the work of API testing too.

Regression tests can be human or automatically driven. Applescript can drive regression tests in full applications or OCUnit can be used to drive regression tests through an API layer.

## Specification

As I hinted previously, there are a few roles served by unit tests that system tests handle. One is that unit tests are a form of specification for the code. You can use the tests as a way of learning what the code is supposed to do and in some cases for sketching out how future code should operate.

API testing can certainly replicate the unit testing specification at the API level; again, API tests are like an interface optimized application of unit tests.

However, I prefer the old-school approach: document your code with comments. Not with a line or two inside the method but full comment blocks on every single method documenting conditions on all parameters and the return parameters and effects of the method. Like test-first development, it is common to write comments first (specify the functionality of the method, then write it, asserting pre and post conditions if desired).

I use a customized version of Xcode's "Script Menu→HeaderDoc→Insert @method comment" to automate the creation of the comment block's formatting from the method prototype.

If the comments at the start of each method are not clear enough for documentation (think about Apple's Cocoa API documentation) then you're not doing your commenting job.

## Conclusion

Unit testing an application is filled with difficulties and problems. In my development style, I consider the time cost of unit testing an application outweighs its benefits — especially since a unit tested application still requires system tests like user-interface and regression tests for proper validation.

Regardless of whether you use unit tests, formalized system testing — either automated or manual and methodical — is required to fully validate an application and ensure the lowest possible low bug rates.

The most efficient approach is to test the interface that the program exposes in the exact way that the user will use it. For user interface apps, this means user testing matrices. For applications with a lot of model code, this means API tests. For document producing applications, this means regression tests. In many cases though, a combination of all three is best.

Most of these approaches require that you be disciplined. You need to comment your code. You need to maintain user interface testing matrices. You need to refactor your model layer so it has an interface that can be tested automatically. You need to measure the code coverage of your regression tests.

I know these things are tedious. I know that no one wants to write test plans, test documents and API tests. But if you love your program and you want it to suck less, this is work that needs to be done.
