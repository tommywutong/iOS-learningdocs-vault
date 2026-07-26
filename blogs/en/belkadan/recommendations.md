---
title: Recommendations
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2015/11/Recommendations/'
original_language: en
published: 2015-11-18
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:16ea5a9b28bb3a09'
translated: false
---

> 原文：[Recommendations](https://belkadan.com/blog/2015/11/Recommendations/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Nibblesort: Adventures in Optimization](https://belkadan.com/blog/2015/05/Nibblesort/)

[Re: Contempt Culture](https://belkadan.com/blog/2015/12/Re-Contempt-Culture/) »

« [Nibblesort: Adventures in Optimization](https://belkadan.com/blog/2015/05/Nibblesort/?tag=compilers)

[So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/?tag=compilers) »

« [Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=book)

« [Dealing with "Sandwich Code"](https://belkadan.com/blog/2011/06/Sandwich-Code/?tag=programming-languages)

[Re: Contempt Culture](https://belkadan.com/blog/2015/12/Re-Contempt-Culture/?tag=programming-languages) »

## [Recommendations](#)

A few weeks ago I asked people a question on Twitter:

> So, for people working on developer tools (compilers, debuggers, IDEs, many other things), how did you get into it?
> 
> — Jordan Rose (@UINT_MIN) [November 2, 2015](https://twitter.com/UINT_MIN/status/661221125381197824)

I got many interesting responses, but one of them asked if I had any recommendations for books on compilers.

Oh gosh. Books? Books about computer science? I’m actually not very well-read: while I’ve been programming since I was a kid, I “only” have an undergraduate formal education. That means the set of books I’ve read about CS is rather haphazard. But I suppose I do have a few things that come to mind.

### [Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sicp/)

Abelson and Sussman’s [Scheme](https://en.wikipedia.org/wiki/Scheme_(programming_language))-based textbook was originally designed for the first computer science course you’d take at MIT; when I was at Berkeley, it was the first course you’d take once you knew a bit about “programming”. SICP (pronounced “sick-P”) is divided into five chapters that build a solid foundation for many of the main ideas in programming. Chapter 4 is all about interpreters, beginning with a Scheme interpreter written in Scheme and then moving into several interesting variations. Chapter 5 takes this further by describing an abstract machine, and then turning the interpreter into a compiler for this machine.

If I had to choose the most important message from SICP (and from the Berkeley “61” series of lower-division CS classes), it’s that nothing is magic. Scheme is a small language, and yet you can use its relatively limited primitives to accomplish things that would be entire features on their own in a larger language like Swift.

(If I had to pick a favorite topic in the book, though, the _metacircular evaluator_—the Scheme-in-Scheme interpreter—loses out to _streams,_ the book’s treatment of lazy-but-infinite sequences. This was my first encounter with infinite data structures.)

SICP alone is very dense reading, so you may instead want something to follow along. Berkeley’s old “CS61A” course materials are [still online](http://www-inst.eecs.berkeley.edu/~cs61a/sp11/), as is the [new version of the course](http://cs61a.org) that uses Python. And finally, though I’m not sure it’s still active, you can also check out [Understudy](http://www.understudyapp.com), an iOS app that tries to pair newer students with those further along in a course. Think of them as your Scheme senpai.

### [Object-Oriented Software Construction](https://en.wikipedia.org/wiki/Object-Oriented_Software_Construction)

Meyer’s _Object-Oriented Software Construction_ is the first book I read that was really about programming language design, and I think it may still be the _only_ book I’ve encountered so far that really talks about _programming language design._ The book walks through the creation of a language from the ground up, justifying each feature along the way. There’s some talk about how to use the features as well—it is called “OO software construction”, after all—but what got me hooked was the language design parts. I may not agree with all of the choices, but for once someone was bothering to explain each one, in a way that didn’t depend on external literature or history.

(I haven’t picked up a copy of OOSC in almost a decade, so forgive me if I’ve misremembered some of the details.)

There are lots of books on _compilers_ out there, but most of them really are about compilers: different techniques for parsing source text into abstract syntax trees (“ASTs”), a discussion of the formal semantics of various constructs (“semantic analysis”), and then a lowering to machine code (“code generation”). All of this is important, but (a) not all of it is practical in real compilers^[1](#fn:parser), and (b) it felt like there was no sense of design; it’s just different techniques for getting from point A to point B. Problem-solving.

I don’t want to slander compiler work; I was just tired of the tried-and-true academic approach to compilers. And it turned out I was more interested in program semantics and language design anyway.

### “[Kaleidoscope](http://llvm.org/releases/3.6.2/docs/tutorial/LangImpl1.html)”

So let’s circle back to compilers. The [LLVM](http://llvm.org/) project has a series of tutorials on how to build a toy language called “Kaleidoscope” on top of LLVM’s libraries. This allows Kaleidoscope to be compiled to machine code or even immediately executed; it’s the same way that Clang and Swift are built on top of LLVM.

This isn’t a book, but a great thing about the tutorial is it shows how “writing a compiler” isn’t some gargantuan task beyond the abilities of mere mortals. It is in C++, though, so you’ll have to get used to that if it’s not a language you’re familiar with.

There are probably other compiler tutorials out there that are even more compact and/or even more accessible, possibly by virtue of not using C++. Kaleidoscope’s just the first one that comes to mind, but because it sits on top of LLVM and generates actual object files it’s well defended against criticisms that this isn’t what _real_ compilers are like.

### [Crafting Interpreters](https://craftinginterpreters.com)

_(added 2020-04-12)_ I had to come back to this post almost five years later to recommend Bob Nystrom’s _Crafting Interpreters,_ which walks through making an interpreter for a simple, garbage-collected object-oriented language…and then goes through it a second time to make a bytecode compiler and VM instead. One of the things I appreciated about it was the commitment to “no magic”: not only does Nystrom explain everything from the lexer to the garbage collector, but he includes _every line of code_ in the book itself. (And wrote a [heck of a blog post](https://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/) about how he went about _testing_ such a thing.^[2](#fn:ht)) On top of that, his writing style is fun and whimsical (all the examples are about breakfast), and the book contains dozens of hand-drawn diagrams and sketches with hand-lettered annotations.

I enjoyed _Crafting Interpreters,_ but as someone who’s been interested in compilers and interpreters and programming languages for years there wasn’t _too_ much that was new for me. So if you’ve already got baseline compiler knowledge, you may end up wanting to skip section II (the straightforward direct-from-parsed-code interpreter written in Java) and going straight to section III (the bytecode-based interpreter). But if you’re new to the field, I can recommend the whole thing as a sensible and approachable introduction to the main concepts.

### …and beyond

I’m sure there are more great books about both programming language design and compilers and other developer tools, not to mention myriad interesting _papers_ on compiler research. And then of course there’s the rest of the internet. Here are a few things that didn’t get full coverage above:

- _[From Mathematics to Generic Programming](http://fm2gp.com):_ What OOSC does for language design, FM2GP does for library design: it builds several algorithms from the ground up in simple C++ and shows how to make them both reusable and efficient…weaving in both math and _history_ of math along the way. It’s not a light read, and we’re getting further from the original question about “compilers”, but I will say that understanding the notion of _concepts_ in particular is a big part of understanding why the _Swift_ standard library is designed the way it is, not just C++’s.
- [Lambda the Ultimate](http://lambda-the-ultimate.org): A blog aggregating interesting articles about programming languages from across the internet. (Warning: often fairly technical and on the theory side of things.)
- [Embedded in Academia](http://blog.regehr.org): John Regehr is a CS professor who’s well-involved in the LLVM projects; he often posts about interesting features of C and C++ compilers (and the languages themselves).
- [NSBlog](https://mikeash.com/pyblog/): Mike Ash’s blog isn’t really about compilers, but his “Friday Q&A” series does talk a lot about how various things are implemented, delving into libraries and language runtimes in detailed but accessible depth.
- [Talks at past LLVM dev conferences](http://llvm.org/devmtg/).

But I’d also love to know what language and compiler resources _you’ve_ found interesting, so I can pick them up. Comment below or [on Twitter](https://twitter.com/UINT_MIN), and I’ll add them here!

**EDIT:** …and if you’ve come to this page looking for how to get started in compilers, [I did a later blog post about that too.](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/)

#### Reader Contributions

(added 2015-11-27)

- Several people mentioned “the Dragon Book”, which can refer to either _[Principles of Compiler Design](https://en.wikipedia.org/wiki/Principles_of_Compiler_Design)_ or the newer _[Compilers: Principles, Techniques, and Tools](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools)_. The former is actually one of the books I considered overly academic and theory/structure-based, but it’s also probably at the top of that list. At some point I’ll psych myself up for a reread.
- [John Regehr](https://twitter.com/johnregehr) (mentioned above) and a few others suggest Muchnick’s _Advanced Compiler Design and Implementation._ (There doesn’t seem to be a website for this book, but it’s still being sold and I assume you can find it in academic libraries.)
- Both Regehr and my coworker [Mark Lacey](https://twitter.com/duklaw) recommended Cooper and Torczon’s _[Engineering a Compiler](http://store.elsevier.com/product.jsp?isbn=9780120884780)._
- [FrancisVM](https://twitter.com/thegameg) suggests Appel’s _[Modern Compiler Implementation](https://www.cs.princeton.edu/~appel/modern/)._ [Brian Mastenbrook](https://twitter.com/bmastenbrook) independently added Appel’s _[Compiling With Continuations](http://www.cambridge.org/us/knowledge/isbn/item1116671)._
- Mastenbrook also recommends Friedman and Wand’s _[Essentials of Programming Languages](http://www.eopl3.com)._
- In the comments below, Chris suggests Wirth’s _Compiler Construction_ ([PDF](http://www.ethoberon.ethz.ch/WirthPubl/CBEAll.pdf)) over the Dragon Book.
- Chris also points out _[Linkers and Loaders](http://linker.iecc.com),_ which I recommend as well. Great little book about static and dynamic linking~~, and you can read it all for free online if you want (in draft form)~~.
- Another online resource: [Matt](https://twitter.com/matt_dz) pointed to Adrian Sampson’s online tutorial “[LLVM for Grad Students](http://adriansampson.net/blog/llvm.html)”. It looks pretty solid to me, whether or not you are a grad student.
- Finally, [Stephen Canon](https://twitter.com/stephentyrone) recommends following [@spun_off](https://twitter.com/spun_off) and [Rich Felker](https://twitter.com/RichFelker) on both Twitter and Stack Overflow ([here](http://stackoverflow.com/users/139746/pascal-cuoq) and [here](http://stackoverflow.com/users/379897/r), respectively). I’d personally recommend following Steve himself as well.

1. If you ever take a college course on compilers, you will almost certainly be introduced to `lex` and `yacc` (or their GNU equivalents, `flex` and `bison`). At a high level, these tools take an abstract grammar and generate a fairly efficient parser from it. However, both [Clang](http://clang.llvm.org) and [Swift](https://developer.apple.com/swift/) use hand-written “recursive descent” parsers, basically the most dead-simple, inefficient parsing algorithm you can think of. Why? Three reasons, I think:

    - The “efficiency” gains we’re talking about hardly ever apply in practice. When they are relevant, they’re easy enough to special-case.
    - The languages we’re parsing are messy and don’t fit into a tidy grammar.
    - Most importantly, a generated parser is great for perfect input, but doesn’t handle incorrect or incomplete code very well. A good compiler should have great error handling. (Insert your own dig at Swift here.)

  An undergrad college course will give you a good understanding of how we _want_ things to work, but as with pretty much every area of CS (and probably most majors outside of CS as well), the real world turns out be more complicated. Optimizing for the perfect case is, IMHO, the wrong tradeoff. [↩︎](#fnref:parser)
2. [h/t](https://en.wikipedia.org/wiki/Hat_tip#Metaphor) [Gus Mueller](https://shapeof.com/archives/2020/4/crafting_crafting_interpreters.html) [↩︎](#fnref:ht)

This entry was posted on [November](https://belkadan.com/blog/2015/11) 18, [2015](https://belkadan.com/blog/2015) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Compilers](https://belkadan.com/blog/tags/compilers), [Book](https://belkadan.com/blog/tags/book), [Programming languages](https://belkadan.com/blog/tags/programming-languages)
