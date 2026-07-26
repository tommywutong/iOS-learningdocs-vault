---
title: Dan Grossman’s Programming Languages Course
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/12/programming-languages-mooc/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9599e6e954b70423'
translated: false
---

> 原文：[Dan Grossman’s Programming Languages Course](https://oleb.net/blog/2014/12/programming-languages-mooc/)　·　Ole Begemann

# Dan Grossman’s Programming Languages Course

## One of the Best Courses I've Ever Taken

I just completed the University of Washington’s [Programming Languages course](https://www.coursera.org/course/proglang) on [Coursera](https://www.coursera.org/), and it was one of the best learning experiences I have ever had. This class is not your typical introduction to a particular language. Rather, instructor [Dan Grossman](http://homes.cs.washington.edu/~djg/) aims to teach the fundamental concepts that underlie all programming languages, highlighting important (conceptual, not syntactical) similarities and differences between them.

Two central themes dominate the course: the distinction between [functional](https://en.wikipedia.org/wiki/Functional_programming) and [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming) on one side and between [static](https://en.wikipedia.org/wiki/Type_system#STATIC) and [dynamic type-checking](https://en.wikipedia.org/wiki/Type_system#Dynamic_type-checking_and_runtime_type_information) on the other. To that end, Dan uses three different programming languages:

- [Standard ML](https://en.wikipedia.org/wiki/Standard_ML) as an example of a functional language with static type-checking.
- [Racket](https://en.wikipedia.org/wiki/Racket_(programming_language)), a Lisp/Scheme variant, as an example of a dynamically typed functional language.
- [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)), a dynamically typed object-oriented language.

[![Contrasting Standard ML, Racket and Ruby in a matrix: functional vs. object-oriented and dynamically vs. statically typed](https://oleb.net/media/programming-languages-mooc-language-matrix.jpg)](https://oleb.net/media/programming-languages-mooc-language-matrix.jpg)

<sub>In a matrix contrasting functional vs. object-oriented and dynamically vs. statically typed languages, ML, Racket and Ruby occupy three of the four spots. One reason why the fourth quadrant, a statically typed OOP language, is left out is that most students are likely to know Java, C#, or a similar language. (Image: screenshot from one of the course videos)</sub>

It is important not to dwell too much on the choice of these particular languages – another instructor could have easily chosen Haskell, Clojure and Python to teach the same concepts.^[1](#fn:1) And I’m convinced that completing this course will still make you a better programmer even if you don’t expect to work with any of those languages in the future.

Dan doesn’t hide that he is a big fan of functional programming, and that is clearly where the focus of the class lies.^[2](#fn:2) Since most students are probably more familiar with OOP, I think this is a very good choice.

# Workload

The course runs over 10 weeks. Each week consists of 2–3 hours of lecture videos with new material, and a large homework assignment. This is a university-level class, so you should expect to spend a significant amount of time on the assignments. I estimate that I invested approximately 8–10 hours per week in total.

It was definitely worth it. The homework problems were both interesting and challenging. My favorite assignment was the implementation of an interpreter for a small programming language, complete with variables, function calls and closures, in Racket (similar to [the Metacircular Evaluator example in SICP](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-26.html)).

The assignments force you to write real code (including tests), which is then graded not only by an automated script, but also by your fellow students. Each week, students are asked to evaluate the work of three other students on an anonymized basis and give feedback on style and things the auto-grader did not catch. It’s a great idea that unfortunately became a bit tedious after a while, largely because Coursera’s peer assessment UI was not very good.

# Final Words

If you’re like me and the arrival of Swift has motivated you to learn new things outside the Objective-C comfort zone, I highly recommend you take this class. Dan Grossman claims that completing it makes you a better programmer, and that is certainly true for me. Especially as someone who has no formal computer science education, I gained a deeper understanding of a bunch of things that I only vaguely understood before.

Dan is hands-down one the best teachers I know.

You can still sign up for this year’s edition of the course, though it’s too late to earn credit or a certificate. For me, having deadlines for the assignments was a good motivator to sit down and do the work, so you might have a better experience if you wait for the next run. I don’t know when that will be, but Coursera will send you an email if you add the course to your watchlist.

1. Dan gives good reasons why he chose these particular languages, though. For instance, Haskell’s lazy evaluation complicates the teaching of semantics, and Python is not as “fully” object-oriented as Ruby. [↩︎](#fnref:1)
2. If there is anything to criticize about the course, it’s that the quality of the Ruby section felt not quite up to the standard of the other parts. I felt that the Ruby assignments were less well thought-out and the sample code was less idiomatic than for ML and Racket. [↩︎](#fnref:2)
