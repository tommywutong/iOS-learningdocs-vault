---
title: 'Book Review: Coders at Work'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/02/book-review-coders-at-work/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:72916e49c2fa69ba'
translated: false
---

> 原文：[Book Review: Coders at Work](https://oleb.net/blog/2010/02/book-review-coders-at-work/)　·　Ole Begemann

# Book Review: Coders at Work

[![Coders at Work book cover](https://oleb.net/media/coders-at-work-cover-133x200.jpg)](https://www.amazon.com/Coders-at-Work-Peter-Seibel/dp/1430219483/)

In 2007, Jessica Livingston wrote a book called [Founders at Work](https://www.amazon.com/Founders-Work-Stories-Startups-Problem-Solution/dp/1430210788/), in which she interviewed a number of tech entrepeneurs about their experiences in the early days of their startups. I enjoyed that book very much, and so I was quite excited to see that [Peter Seibel](http://www.gigamonkeys.com/blog/) recently wrote what could be called the second part of what I hope will be a series of interview books. Instead of founders, this time it is all about programmers, and the title of the book is [Coders at Work: Reflections on the Craft of Programming](https://www.amazon.com/Coders-at-Work-Peter-Seibel/dp/1430219483/) (released in late 2009).

_Coders at Work_ consists of extensive interviews (each interview some 40 pages long) with 15 of the best-known programmers of the last 4 decades:

- [Jamie Zawinski](https://en.wikipedia.org/wiki/Jamie_Zawinski), author of XEmacs and the Unix version of Netscape Navigator.
- [Brad Fitzpatrick](https://en.wikipedia.org/wiki/Brad_Fitzpatrick), creator of LiveJournal, author of memcached.
- [Douglas Crockford](https://en.wikipedia.org/wiki/Douglas_Crockford), creator of JSON.
- [Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich), inventor of JavaScript.
- [Joshua Bloch](https://en.wikipedia.org/wiki/Joshua_Bloch), author of the Java Collections Framework.
- [Joe Armstrong](https://armstrongonsoftware.blogspot.com/), inventor of Erlang.
- [Simon Peyton Jones](https://en.wikipedia.org/wiki/Simon_Peyton_Jones), Co-creator of Haskell.
- [Peter Norvig](https://en.wikipedia.org/wiki/Peter_Norvig), Director of Research at Google.
- [Guy Steele](https://en.wikipedia.org/wiki/Guy_Steele), Co-designer of Scheme.
- [Dan Ingalls](https://en.wikipedia.org/wiki/Dan_Ingalls), principal creator of Smalltalk.
- [L. Peter Deutsch](https://en.wikipedia.org/wiki/L_Peter_Deutsch), author of Ghostscript and implementor of Smalltalk-80.
- [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson), creator of Unix.
- [Fran Allen](https://en.wikipedia.org/wiki/Frances_E._Allen), pioneer in optimizing compilers.
- [Bernie Cosell](http://www.codersatwork.com/bernie-cosell.html), one of the guys who wrote the first routers (Interface Message Processors) for the Arpanet.
- [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth), über-father and creator of TeX.

The interviews follow the same broad structure: Peter Seibel asks everyone how they got into programming; how they learned it in the first place and how they perfected their skills; which programming languages they like and which they hate; which editors, IDEs and debugging tools they use; how they approach the design of a program, top-down or bottom-up; etc. In addition to the general questions, Seibel digs deep into the projects his subjects are famous for: How did they end up working on these projects? What was it like? How was the project team organized? What did you learn? What were the hardest problems to solve, the fiercest bugs to squash?

To me, the greatest insight came from the interviewees’ reflections on their craft: How do they think about themselves and how do they personally practice programming? Despite having quite different backgrounds, it was interesting to discover that many of them had a common philosophy when it came to approaching programming.

For example, many mentioned their desire to take things apart, to understand how stuff works, as one of the prime impulses that brought them into the field. Also, motivation is a very important factor for learning, and personal side projects were often the ones where they learned the most. On the question whether it made sense to write the umpteenth C compiler or image processing library instead of just taking one that is already available, Joe Armstrong said:

> The really good programmers spend a lot of time programming. I haven’t seen very good programmers who don’t spend a lot of time programming. … And you get better at it—you get quicker at it. The side effect of writing all this other stuff [side projects] is that when you get to doing ordinary problems, you can do them very quickly.

# The importance of reading and writing

When asked whether they, as programmers, think of themselves as scientists or engineers or artists or craftsmen, some said they felt most like a writer whose job is to formulate their thoughts so that their audience — which comprises both the computer _and_ readers of the source code — understands them best. You want to become a great programmer? Write _a lot_ of code! Jamie Zawinski:

> It feels like you’re writing a story and you’re trying to express a concept to a very dumb person—the computer—who has a limited vocabulary.

Similarly, nearly everyone mentioned that reading code is as important as writing it. Many said that reading other people’s source code (written either by more-experienced co-workers or the code of well-known open source projects) was a formative experience for their development as a programmer. Still, it struck me that these experiences mostly came from accidental exposures to great pieces of code. Almost none of the 15 had made it a personal habit to explicitly grab the source of an interesting piece of software and read over it for both learning and fun. Or, as Joshua Bloch put it, When was the last time you sat down at night to read a beautiful piece of code?

Short of attacking monster projects like the Linux kernel, how do we find the good code that is worth reading, the code that makes us better programmers by studying it? I think there is a great opportunity for blogs and other websites here to research and present the truly great pieces of code in open source projects in an easy-to-digest and informative form. Perhaps Peter Seibel’s new project, [Gigamonkeys Quarterly](http://www.gigamonkeys.com/blog/2010/02/18/gigamonkeys-quarterly.html), could partly evolve into something like this.

# Historical quality

One reviewer of the book on Amazon:

> There is also a historical quality to the book. The majority of the people interviewed started programming in the 50s or the early 60s. One of the standard questions was “How did you learn to program?” and I thought it was quite interesting to read about the old computers they used, the punch cards etc. It was almost like little history lessons from the computing field. — [Henrik Warne](https://www.amazon.com/review/R2OV0TG7MJGXGL/)

While this is certainly true and nice, I felt that the book lacked a certain balance between the “old guys” and the young coders of today who learned programming on and for the Web. Brad Fitzpatrick is basically the only representative of the Web generation of programmers. I think including more of his generation could have given readers further insight on the learning and practice of programming today. This is especially so since many of the interviewees, having learned their craft decades ago, lamented the complexity of today’s hardware and software and how much harder it is today to dig deep into how things work at the most basic level. So how do people learn to program these days and how to they cope with the fact that they will never understand how the machine they are writing code for actually works? For instance, I would have liked to see [David Heinemeier Hansson](https://en.wikipedia.org/wiki/David_Heinemeier_Hansson) included in the book.

# Wrap-up

If you want to learn more about _Coders at Work_, Peter Seibel talked about it on [episode #69 of the Stack Overflow podcast](http://blog.stackoverflow.com/2009/09/podcast-69/). He also held a [one-hour long speech at Google](https://www.youtube.com/watch?v=pQy22qPH7i4) where he talks about a few anecdotes and some of the topics he addresses in the book.

I found _Coders at Work_ entertaining and inspiring. Reading the book has provided me with long lists of more books I want to read and programming languages I want to learn. Highly recommended for programmers; not recommended for non-programmers who want to learn more about programmers and programming. Finally, my favorite quote from the book is by Peter Seibel himself:

> Speaking of writing intricate code, I’ve noticed that people who are too smart, in a certain dimension anyway, make the worst code. Because they can actually fit the whole thing in their head they can write these great reams of spaghetti code.
