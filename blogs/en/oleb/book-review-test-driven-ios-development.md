---
title: 'Book Review: Test-Driven iOS Development'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/08/test-driven-ios-development/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c817a8a951417bb9'
translated: false
---

> 原文：[Book Review: Test-Driven iOS Development](https://oleb.net/blog/2012/08/test-driven-ios-development/)　·　Ole Begemann

# Book Review: Test-Driven iOS Development

[![Test-Driven iOS Development Book Cover](https://oleb.net/media/test-driven-ios-development-cover-500px.jpg)](https://www.amazon.com/Test-Driven-iOS-Development-Developers-Library/dp/0321774183/)

The [testing](https://en.wikipedia.org/wiki/Software_testing)^[1](#fn:1) mindset is something that is deeply ingrained in some programming communities and almost absent in others. How a community treats testing seems to be largely a factor of built-in tools support and how much the practice is promoted by the founders or protagonists of that community. For instance, testing has been a big thing in the Ruby on Rails community because the framework had built-in unit testing support and [DHH](https://en.wikipedia.org/wiki/David_Heinemeier_Hansson) mentioned it in every talk he gave. This, in turn, led to testing being covered even by beginner books from the get-go.

# Testing in the Cocoa Community

It always seemed to me that the Cocoa developer community did not have a similar attachment to testing. Although [OCUnit](http://www.sente.ch/software/ocunit/) was one of the first testing frameworks in any language (the first release was in 1998) and has been integrated into Xcode since version 2.1 (1995), I haven’t seen many discussions of the benefits and drawbacks of automated testing, be it from Apple or other people.^[2](#fn:2) Considering that I’m only part of this community since 2008, my impression may be wrong, of course. In fact, you should read Wil Shipley’s article [Unit testing is teh suck, Urr](http://wilshipley.com/blog/2005/09/unit-testing-is-teh-suck-urr.html) and [Bill Bumgarner’s response](http://www.friday.com/bbum/2005/09/24/unit-testing/) for a great discussion on the topic from 2005.

Most of us probably write iOS apps and, as Bill pointed out, Unit Testing cannot test User Experience. Nevertheless, I think testing can be a very useful tool for app developers and more developers should learn about it. Which brings us to the book I want to talk about.

# The Book

Graham Lee’s [Test-Driven iOS Development](https://www.amazon.com/Test-Driven-iOS-Development-Developers-Library/dp/0321774183/) (published April 2012) is the only book I know of that talks especially about automated testing in the context of iOS development. At about 250 pages, it’s quite short and to the point. It only took me a few days to read it.

The book starts with an introduction to automated testing and a definition of different testing methods developers can use ([unit testing](https://en.wikipedia.org/wiki/Unit_testing), [system testing](https://en.wikipedia.org/wiki/System_testing), and so on; the book only deals with unit testing). I especially liked the explanation of the [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) approach and its motiviation:

> The idea behind test-driven development is that it makes you think about what the code you’re writing needs to do while you’re designing it. Rather than writing a module or class that solves a particular problem and then trying to integrate that class into your app, you think about the problems that your application has and then write code to solve those problems.

The central part of the book covers the development of a fully functioning app with TDD. That is, no code is written unless we have written a failing unit test for the required behavior first. While the author lists a number of popular testing frameworks that are available to iOS developers, the book only uses OCUnit for writing tests. Since OCUnit is integrated in Xcode and as such the framework that is easiest to start with, I think this is a good decision.

The sample app downloads questions and answers from Stack Overflow and displays the results in a table view. As such, it represents a fairly typical iOS app that has some model classes, deals with networking code, and uses view controllers to manage the UI. Accordingly, the unit tests the author writes use fake and mock objects to simulate network connections, notification centers and even user actions. One of the biggest learnings for me was the extent to which Graham was able to test UI code (e.g., what should happen when a user taps a table cell) by just using unit tests. The resulting test code did not always look elegant but it certainly did the job.

After finishing the sample app, the author concludes the book with some general advice how to design and write testable code and a very useful section on how to apply TDD retroactively to your existing codebases that do not yet include tests. One aspect that I would have liked to see covered in more detail is the testing of concurrent code. Graham’s general recommendation here is to employ the [producer-consumer pattern](http://msdn.microsoft.com/en-us/library/dd728068.aspx) where possible. In Cocoa, this pattern is used by the [`NSOperationQueue`](https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/NSOperationQueue_class/Reference/Reference.html) class. Here, the concurrency aspect is handled by a single class (which in this case has been tested extensively by Apple) and the tasks (`NSOperation` instances) that should run concurrently can be tested separately. However, as Graham notes,

> this ability to completely unit test concurrent code says nothing about its behavior in the integrated system, and it’s still possible for resource contention or scheduling problems to exist in the code.

Exactly. Perhaps this area can never be sufficiently tested with unit tests alone.

# Conclusion

In summary, _Test-Driven iOS Development_ is a very good book to get you into the TDD mindset and to help you write your first unit tests. It’s also useful if you are used to the automated testing of infrastructure code but you are unsure how to apply this knowledge to the testing of user interfaces. If you’re already familiar with automated testing for UI applications on other platforms, you are probably better off reading the Apple documentation to learn how to set up and use unit testing in the iOS environment.

Graham also writes a very good blog at [blog.securemacprogramming.com](http://blog.securemacprogramming.com). If you like this blog, you should definitely also subscribe to Graham’s.

**Update September 5, 2012:** Graham posted an article on his blog titled [An apology to readers of Test-Driven iOS Development](http://blog.securemacprogramming.com/2012/09/an-apology-to-readers-of-test-driven-ios-development/), in which he talks about quoting potentially wrong and unreliable data about the alleged cost of fixing bugs at different stages of the development process – one of the big arguments in favor of test-driven development:

> I perpetuated what seems (now, since I analyse it) to be a big myth in software engineering. I uncritically quoted some work without checking its authority, and now find it lacking. As an author, it’s my responsibility to ensure that what I write represents the best of my knowledge and ability so that you can take what I write and use it to be better at this than I am. In propagating incorrect information, I’ve let you down. I apologise unreservedly.

This doesn’t necessarily say that the data is totally wrong, of course. Graham just could not find a reliable source to say it is correct. It’s good to see an author being honest with his readers.

# Translations

Thanks to Anja Skrba for translating this post into Serbo-Croatian: [Pregled knjiga: Test vodjen iOS razvoj](http://science.webhostinggeeks.com/pregled-knjiga)

1. When I mention testing in this article I refer to _automated_ testing. Obviously, everybody agrees that testing is very important. Opinions differ to what degree it can (and should) be automated. [↩︎](#fnref:1)
2. This is not to say that Apple doesn’t care about automated testing at all. The unit testing integration into Xcode has gotten much better with Xcode 4, and Apple also introduced [UI Automation testing](http://developer.apple.com/library/ios/#documentation/DeveloperTools/Reference/UIAutomationRef/_index.html) with iOS 4. All I want to say is that the automated testing mindset is not as ingrained in the Cocoa community as it could be. [↩︎](#fnref:2)
