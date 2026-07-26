---
title: 'Book Review: 97 Things Every Programmer Should Know'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/05/book-review-97-things-every-programmer-should-know/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ca872ab8c912c7e3'
translated: false
---

> 原文：[Book Review: 97 Things Every Programmer Should Know](https://oleb.net/blog/2011/05/book-review-97-things-every-programmer-should-know/)　·　Ole Begemann

# Book Review: 97 Things Every Programmer Should Know

[![Cover of 97 Things Every Programmer Should Know](https://oleb.net/media/97-things-every-programmer-should-know-cover.png)](https://www.amazon.com/Things-Every-Programmer-Should-Know/dp/0596809484/)

I recently finished reading [97 Things Every Programmer Should Know](https://www.amazon.com/Things-Every-Programmer-Should-Know/dp/0596809484/), a compilation of 97 short essays about all facets of programming, published by O’Reilly in February 2010. The essays cover a very broad range of topics, from coding style to unit testing, from handling customer complaints to version control, from command line tools to programming languages. Every one is two pages long so don’t expect to get in-depth coverage of a topic.

As editor Kevlin Henney says [on the book’s website](http://programmer.97things.oreilly.com/):

> There is no overarching narrative: The collection is intended simply to contain multiple and varied perspectives on what it is that contributors to the project feel programmers should know. This can be anything from code-focused advice to culture, from algorithm usage to agile thinking, from implementation know-how to professionalism, from style to substance.

In short, the book is a collection of mostly good advice that will hopefully give you some new ideas to explore further. If you are someone who reads a lot of programming blogs or [Hacker News](http://news.ycombinator.com/), you’ll likely won’t find much that you hadn’t heard about before but that’s not to say this repeated advice cannot be helpful.

To collect contributions to the book, O’Reilly used a wiki that they have kept open even after the book went to print. On the wiki, you can not only read [all essays that are in the book](http://programmer.97things.oreilly.com/wiki/index.php/Contributions_Appearing_in_the_Book) but also [more articles](http://programmer.97things.oreilly.com/wiki/index.php/Other_Edited_Contributions) that didn’t make the cut or were contributed at a later time. All posts are licensed under a [Creative Commons Attribution](http://creativecommons.org/licenses/by/3.0/us/) license. Kudos to O’Reilly for doing this in the open!

Conclusion: the book is not a must-read but I encourage you to take a look at a few essays on the website and see if you like them.

# Some of my favorite articles

[Apply Functional Programming Principles](http://programmer.97things.oreilly.com/wiki/index.php/Apply_Functional_Programming_Principles) by Edward Garson:

> Mastery of the functional programming can greatly improve the quality of tge code you write in other contexts. If you deeply understand and apply the functional paradigm, […] [your] functions consistenly yield the same results given the same input, irrespective on when they are invoked. That is, function evaluation depends less – ideally, not at all – on the side effects of mutable state.

[Before You Refactor](http://programmer.97things.oreilly.com/wiki/index.php/Before_You_Refactor) by Rajith Attapattu:

> Avoid the temptation to rewrite everything. It is best to reuse as much code as possible. …
> 
> Many incremental changes are better than one massive change.

[The Boy Scout Rule](http://programmer.97things.oreilly.com/wiki/index.php/The_Boy_Scout_Rule) by Robert C. Martin:

> The Boy Scouts have a rule: “Always leave the campground cleaner than you found it.” … What if we followed a similar rule in our code: “Always check a module in cleaner than when you checked it out”? … I think if we followed that simple rule, we would see the end of the relentless deterioration of our software systems.

[Dont’ Just Learn the Language, Understand Its Culture](http://programmer.97things.oreilly.com/wiki/index.php/Don%27t_Just_Learn_the_Language%2C_Understand_its_Culture) by Anders Norås:

> it takes more than just learning the syntax to learn a language: you need to understand its culture. … Once you’ve learned the ropes of a new language, you’ll be surprised how you’ll start using languages you already know in new ways.

[Know Your Next Commit](http://programmer.97things.oreilly.com/wiki/index.php/Know_Your_Next_Commit) by Dan Bergh Johnsson:

> Know your next commit. If you cannot finish, throw away your changes, then define a new task you believe in with the insights you have gained. Do speculative experimentation whenever needed, but do not let yourself slip into speculative mode without noticing. Do not commit guesswork into your repository.

[Make Interfaces Easy to Use Correctly and Hard to Use Incorrectly](http://programmer.97things.oreilly.com/wiki/index.php/Make_Interfaces_Easy_to_Use_Correctly_and_Hard_to_Use_Incorrectly) by Scott Meyers:

> Good interfaces are easy to use correctly … [and] hard to use incorrectly. Good interfaces anticipate mistakes people might make, and make them difficult—ideally, impossible—to commit. A GUI might disable or remove commands that make no sense in the current context, for example, or an API might eliminate argument-ordering problems by allowing parameters to be passed in any order.

[Message Passing Leads to Better Scalability in Parallel Systems](http://programmer.97things.oreilly.com/wiki/index.php/Message_Passing_Leads_to_Better_Scalability_in_Parallel_Systems) by Russel Winder:

> what is the root of the problem [of concurrency]? Shared memory. Almost all the problems of concurrency that people go on and on about relate to the use of shared mutable memory. … Instead of using threads and shared memory as our programming model, we can use processes and message passing.
