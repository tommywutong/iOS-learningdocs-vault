---
title: So You Want to Be a (Compiler) Wizard
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/'
original_language: en
published: 2016-05-23
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:0e1a677b6bfff511'
translated: false
---

> 原文：[So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Re: Contempt Culture](https://belkadan.com/blog/2015/12/Re-Contempt-Culture/)

[Webmailer's Update Bar](https://belkadan.com/blog/2016/05/Webmailer-Update-Bar/) »

« [Recommendations](https://belkadan.com/blog/2015/11/Recommendations/?tag=compilers)

[Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=compilers) »

[ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/?tag=assembly) »

« [Re: Contempt Culture](https://belkadan.com/blog/2015/12/Re-Contempt-Culture/?tag=diversity-in-tech)

[Pronoun Buttons](https://belkadan.com/blog/2016/06/Pronoun-Buttons/?tag=diversity-in-tech) »

## [So You Want to Be a (Compiler) Wizard](#)

A month or so ago, [@__biancat](https://twitter.com/__biancat) (whose username I can’t help but read as “Bian-cat” even though it’s probably “Bianca T.”) suggested I write up some ideas for getting into compilers and programming languages.

It turns out I’m happy to expound on this, and it doesn’t need a formal CS education either.[1](#fn:education) Unfortunately, pretty much all of them require some amount of free time. I’ll come back to that at the end of the post.more

P.S. I know the title is a bit [off-brand](https://twitter.com/jckarter/status/719585924338753537), but I couldn’t resist the [reference](https://en.wikipedia.org/wiki/So_You_Want_to_Be_a_Wizard).

### Little Projects

These are things you can do on your own. I’ve arranged them roughly in order of difficulty and time commitment, although of course the language / environment you pick will affect things.

- **Learn regular expressions.** This isn’t exactly a project, and it’s not how real compilers work, but regular expressions get you thinking about parsing and also about languages, and they’re handy to know regardless. I found [Regex Crossword](https://regexcrossword.com) to be a fun way to practice.
- **Make a calculator.** Not a [graphical one](http://www.folklore.org/StoryView.py?story=Calculator_Construction_Set.txt), but something that can take input like “1+2*3-4” and produce “3”. Or even “5”, as a start. If you don’t feel like doing the parsing part, just build a tree-like data structure that can represent mathematical expressions and write an `evaluate` function. A calculator is like a very tiny interpreter.
- **Make a text adventure.** This is one of my favorite ways to play with a new language, but it’s also a lot like an interpreter. Just start with the basics: a bunch of places and descriptions, and a “read-evaluate-print loop” that handles directions. From there you can add other actions, items, whatever.
- **Write `snprintf` in C.** For those who haven’t used C before, [`snprintf`](http://en.cppreference.com/w/cpp/io/c/fprintf) is a function that produces formatted output based on an input string and a variable number of arguments. Doing it in C forces you to deal with constraints you may not have had to deal with in a higher-level language. Don’t skip out on writing unit tests! (And don’t bother with floating-point numbers; just handle `%d` and `%s`.)

  ```
  const size_t bufferLength = 128;
  char buffer[bufferLength];
  snprintf(buffer, bufferLength, "%s %d %s", "first", 2, "last");
  assert(0 == strcmp(buffer, "first 2 last"));
  ```
- **Write `snprintf` in assembly**…for the exact same reason. Pretty much no one programs in assembly any more, and that’s generally a good thing, but this will (a) force you to learn a new and very suboptimal language, (b) get you to learn a little about your CPU[2](#fn:assembly), and (c) help you later on if you ever need to debug a compiled program without debug info. Bonus points if you can get your assembly version to work correctly with C.

  (This was an assignment in one of my lower-div classes at college.)
- **Learn LISP, Scheme, or [Racket](http://racket-lang.org), then make a tiny Scheme interpreter.** The benefit of doing this in one of these languages is twofold: first, the syntax is very simple, which lets you focus on semantics; and second, making an interpreter for a language _in_ that language feels much more impressive than otherwise. (This is the fourth chapter of the classic programming book _[Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sicp/).)_
- **Go through the [Kaleidoscope](http://llvm.org/docs/tutorial/index.html) tutorials.** This is a walkthrough to build a real compiler for a tiny language, using [LLVM](http://llvm.org/). LLVM is the compiler “backend” behind Clang, the C compiler used by Apple and many others, and of course Swift as well, so it’s hard to say you’re not building a _real_ compiler in this project. The original tutorial uses C++, but I know there are alternate versions of it for other languages around the internet.

  Andi McClure has a good diagram about [what LLVM provides for you](http://msm.runhello.com/p/1003) on her blog.

At this point I’ve shaded off of generic projects and into specific ones, which I’ve [talked about before](https://belkadan.com/blog/2015/11/Recommendations/).

### Books and Online Resources

[I did this one already.](https://belkadan.com/blog/2015/11/Recommendations/)

### Contributing to Open Source

Personal projects are all well and good, but they’re a far cry from working on a large program with many contributors and lots of moving pieces. I definitely had a shock when I started my first internship, even after writing my own apps and working on plenty of projects for school, because _you can’t possibly understand it all before you start making changes._

Don’t panic. That’s what good interfaces and good tests are for, and if either of those fails you, don’t be afraid to ask questions.

(There are also [a lot of ways to contribute to a project other than writing code](https://swift.org/contributing/), but I’m going to assume you’re here because you want to write code. Otherwise you wouldn’t have stayed through the previous section.)

I’m not sure I have any specific advice that hasn’t already been said before _somewhere_ on the internet (such as the site [First Timers Only](http://www.firsttimersonly.com), or [this Quora post](https://www.quora.com/How-do-I-participate-or-contribute-in-open-source-projects?share=1)), but here are some things I’d suggest keeping in mind:

- **Pick a bug and try to solve it.** Look through the bug database and find a bug that you understand and that _feels_ like it should be a small thing to fix. Some projects, including Swift, have dedicated “[starter bugs](https://bugs.swift.org/issues/?jql=resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20StarterBug)” or “first-timers only” bugs that they expect someone with less experience to be able to tackle. You’re not limited to those, especially if you’re interested in a particular area of a project, but they’re a place to start looking.

  When choosing a bug you might not even have looked at the code for that part of the project. That’s fine. Pick a bug, then jump into the code and go looking for the problem. If there’s something you don’t understand, but you don’t need it to fix the issue, feel free to ignore it. At the same time, though, a lot of bugs in a bug database are open because they’re trickier than they look, so be willing to set a bug back on the shelf if you’re not making progress.
- **Partial answers are better than none.** While it’s not quite as satisfying as being able to close a bug, just taking, say, a crash, and figuring out _why_ it’s happening can be incredibly useful, even if you don’t know how to fix it. (Example: “It crashes when I compile this file.” → “It’s crashing in `TypeChecker::doTheThing`.” → “The type of some property is null.” → “The type gets reset to null by accident in `TypeChecker::fixTypesPoorly`.”)
- **Talk to people.** Ask for feedback on patches. Ask questions when you’re stuck. Most projects have mailing lists and/or chat rooms (IRC, Slack, etc.); subscribe / sign in even if you don’t have a question at the moment. Answer _other_ people’s questions when you can.

  Don’t forget to be polite. In general, learn how to [get answers](https://mikeash.com/getting_answers.html), and please _don’t_ ask a question before looking for an answer in the obvious places, like the documentation.

  There’s a hidden motive here: regular contributors to the project recognize names that come up regularly. Asking questions demonstrates interest; contributing back demonstrates capability and value.

  If you don’t get an answer, please don’t be offended. Not only are open-source contributors busy people (like everyone else), but usually participation on mailing lists, forums, and chat rooms isn’t an official part of their duties. It’s usually acceptable to “ping” an email after several days or a week to see if anyone has time now.
- **Open source projects are big.** I said this already, but don’t get stuck on the size of the project. I’ve been working on Swift for years, and Clang for years before that, and there are still big chunks of both compilers that I don’t understand. You start in one area, and you learn what you need to as time goes on.
- **Don’t forget to follow contributor guidelines.** It’s one of the more mundane things about working on a project with other people, but if you don’t follow the contribution process and coding standards of the project you’re working on, other people are less likely to take you seriously. (They’ll feel a little like you’re wasting their time.)
- If you’re a student, consider **[Google Summer of Code](https://summerofcode.withgoogle.com).** In short, if you can come up with a good project idea and convince an open-source project to take you on, Google will pay you to work on it for a summer. It’s like a lightweight, remote internship. (This is actually how I got into compilers, by working on the [Clang Static Analyzer](http://clang-analyzer.llvm.org) for GSoC. Not that I wasn’t already interested in programming languages.)

  GSoC also isn’t the only non-internship game in town, so look around. Your particular project might even have their own program.

### On “Free Time”

The sad thing is, there are [10 kinds](https://en.wikipedia.org/wiki/Mathematical_joke#Jokes_with_numeral_bases) of open-source developers: those who do open-source work for a company, and those who do it in their spare time. For those in the former group, open-source work is mostly the same as any other software work: we get paid for it, and we’re not expected to do it _outside_ of work.

If you’re reading this post, you might be in that group—say, if this is your first compiler job—but more likely you’re looking to switch. That means you’re expected to do all of this in your free time, on top of your normal job and any other responsibilities or outside interests you might have.

I want to explicitly recognize this as a form of **privilege**. The people most likely to have spare time to do outside projects are people

- who don’t have families to take care of (kids, parents, whatever)
- who have a good, steady income (i.e. not learning while, say, balancing two part-time jobs)
- who live close to work (minimizing a commute)

etc. Additionally, people who’ve been programming for a long time will likely have an easier time picking up one more thing, meaning the process is also biased towards those who had the _opportunity_ to learn to program when they were younger. In the US, that means men more than women, upper-class more than lower-class, and [white more than black](http://www.alterconf.com/talks/conforming-succeed-and-what-it-means-people-color).

All of that is _institutional_ bias, even before taking into account the _individual,_ usually-unconscious biases that plague our industry (particularly from “people who look like [me](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/me.jpg)”)…not to mention [Imposter Syndrome](https://www.quora.com/What-are-some-effective-ways-to-overcome-the-Impostor-Syndrome-as-a-female-engineer/answer/Anne-K.-Halsall?srid=u5P&share=1). And it stinks. But it can’t stop you—and rather than take my word for it, you can read Kronda Adair’s “[Dear Marginalized People Coming Into Tech](https://modelviewculture.com/pieces/dear-marginalized-people-coming-into-tech)”.

Oh, one more thing to look for is that the project has community guidelines and a code of conduct. That doesn’t automatically mean there won’t be conduct problems, but it at least indicates that the community is considered important, not just the product.

This section is a short and simplified look at some of the problems with today’s open source model. For more depth, check out Ashe Dryden’s “[The Ethics of Unpaid Labor and the OSS Community](http://www.ashedryden.com/blog/the-ethics-of-unpaid-labor-and-the-oss-community)”.

### Valediction

Like [last time](https://belkadan.com/blog/2015/11/Recommendations/), I’d love to hear of other good resources for starting out on compiler work, or for first-time open-source contributors. Comment below or [on Twitter](https://twitter.com/UINT_MIN), and I’ll add them here. I also enjoy talking to people about their _own_ experiences, and I’m happy to help out with _non-technical_ questions on Twitter as well. (Technical questions should usually stay on the mailing lists or review discussion, so that other people can see them.)

Good luck, have fun. We can’t wait to have you.

1. I have a B.A. in Computer Science, and took just one upper-division class about compilers and one grad class about programming languages (though some of my lower-division classes did have compiler-related work in them). My coworker [Joe Groff](https://twitter.com/jckarter) doesn’t have _any_ formal education, and he’s one of the best compiler people I know. [↩︎](#fnref:education)
2. In reality, CPUs have tons of tricks up their proverbial sleeves, which means even assembly doesn’t correspond precisely to how the program actually gets run. But it gives you an idea of common denominator capabilities, anyway. [↩︎](#fnref:assembly)

This entry was posted on [May](https://belkadan.com/blog/2016/05) 23, [2016](https://belkadan.com/blog/2016) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Compilers](https://belkadan.com/blog/tags/compilers), [Assembly](https://belkadan.com/blog/tags/assembly), [Open source](https://belkadan.com/blog/tags/open-source), [Diversity in tech](https://belkadan.com/blog/tags/diversity-in-tech)
