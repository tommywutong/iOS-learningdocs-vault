---
title: 'Friday Q&A 2009-02-27: Holistic Optimization'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-02-27-holistic-optimization.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dad4a48d207d589f'
translated: false
---

> 原文：[Friday Q&A 2009-02-27: Holistic Optimization](https://www.mikeash.com/pyblog/friday-qa-2009-02-27-holistic-optimization.html)　·　mikeash.com Friday Q&A

Posted at 2009-02-27 04:21 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-03-06: Using the Clang Static Analyzer](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html)  
Previous article: [Friday Q&A 2009-02-20: The Good and Bad of Distributed Objects](https://www.mikeash.com/pyblog/friday-qa-2009-02-20-the-good-and-bad-of-distributed-objects.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [performance](https://www.mikeash.com/pyblog/?tag=performance) [rant](https://www.mikeash.com/pyblog/?tag=rant)

Friday Q&A 2009-02-27: Holistic Optimization

by [Mike Ash](https://www.mikeash.com/)

**Engineering Optimization**  
 Let's forget about code for a moment, and talk about something completely different: aircraft design. Bear with me, we'll get back to programming in a bit.

I'm part owner of a Schleicher ASW-20C. This is a 15 meter wingspan competition glider originally designed in the mid-1970s. At the time it was at the top of its class, although of course technology has improved over the decades since. What does it take to make a top class competition glider?

Obviously it takes an expert aeronautical engineer with a great deal of experience in designing sailplanes and a factory which can actually construct the product. A top competition machine has to be highly optimized. But what does "optimized" mean in this case? What exactly was the designer optimizing when he designed this airplane?

The obvious thing to optimize is glide ratio. This is a measure of how much distance can be obtained for any given amount of altitude. Since altitude is the only source of the glider's energy this number is highly significant and it's usually the first thing a pilot looks at when he examines the numbers of a new machine. This number might range anywhere from 20:1 to 60:1. The ASW-20's glide ratio is a bit over 40:1 which at the time was exceptional in the 15 meter class.

But of course there's more to it than a single number. The best glide ratio is at a single speed, but pilots fly at lots of different speeds. Two machines might have the same best glide ratio but one might have a much better glide ratio at high speed, giving it a significant edge. The designer must not only optimize the best glide ratio, but the glide ratio over a wide range of speed.

Weight is another big consideration. Sailplanes are built extremely light, and their construction uses fiberglass and other advanced composites to achieve this. The lighter a glider is the better it can climb, so this is highly important.

Weight is also important. I just said this, but this time I mean the opposite. The heavier sailplane is the faster it can fly on strong days. In order to achieve the goal of being both light and heavy, a system of water ballast is used, allowing the pilot to load up with water on strong days and leave it out on weak days.

But what else? Certainly doesn't stop here. Handling is important: if the plane handles like a truck then nobody will buy it. Ease of assembly is important. Many gliders are stored disassembled in a trailer and are put together before each day's flying. A glider which has a reputation for being difficult to assemble will be unpopular. Crashworthiness is, of course, significant. Cockpit ergonomics matter a great deal, since the pilot might spend five hours in a row or more sitting in the seat. Strength is key. Gliders fly through rough air and need to be able to take the punishment. And last but far from least: cost. None of this does any good if nobody can afford to purchase the result.

Clearly, designing an airplane involves a huge number of different goals, even when the airplane is just a 600 pound competition glider. (Imagine the goals involved when designing a 200-_ton_ 747.) Worse yet, many of these goals are contradictory. The quest for lighter weight is directly opposed to the quest for strength. Improvements in performance often hurt handling. Making the glider easier to assemble involves "wasted" structure which is otherwise just dead weight. And of course _everything_ conflicts with the goal of lower cost.

A successful aeronautical engineer has to juggle all of these different constraints and come up with the best solution he can given his budget for both time and money. In fact, the word "aeronautical" is completely unnecessary in that sentence: any engineer faces the same problems.

**Software Optimization as Engineering Optimization**  
 Enough of that airplane business, let's get back to programming. Most people don't think of software engineers as "real" engineers, and there's a lot of truth to that. Software engineering is a young discipline, and it's missing a lot of the certainty and standardized practices that can be found in other forms of engineering. But one thing that we do have in common with other forms of engineering is this concept of tradeoffs.

Unfortunately, most software engineers aren't really aware of this whole idea. It's rarely taught in school, or formally explored elsewhere. Most have a vague idea that you can't have everything, and sometimes you have to sacrifice one thing, for example features or stability, in order to achieve another, for example a deadline, but there isn't a codified concept of making tradeoffs in order to come up with the best possible result given the resources at hand. As a result, programmers tend to think of "optimization" as being purely about performance.

Even performance optimization involves a lot of trade-offs. Just like with the competition glider, software performance is actually many different quantities which are often mutually contradictory. Do you want to optimize latency or throughput? Speed or battery life? Memory usage or disk usage? Perceptual time or wall clock time?

And beyond performance there are many other goals reach as well. I like to think of it mathematically. Imagine a fitness function, which takes the program as its input and as its output generates some number, the higher the better. This magical function takes into account all those different kinds of performance, as well as things like programmer time, money, features, reliability, ship date, and anything else that affects how "good" a program is. Optimization then involves getting the largest number out of this function possible with the resources available.

Looking at it this way, the problem of premature performance optimization becomes obvious. You have limited resources in the form of programmer time, programmer salaries, overhead, and other such things. To optimize the entire program, you have to spend those limited resources where they will do the most good. When you optimize too early, you don't know where to put those resources in order to extract the most good. If you spend all your time optimizing module A but it turns out the program spends most of its time in module B, you've just wasted all those resources. If you spend all your time optimizing both, so that you can be sure that you've covered everything, you've still wasted a lot of resources on A.

Beyond the question of performance, there are always other variables as well. Is spending resources on performance the best way to spend them? Often the answer is no. And even more often, the answer is "we don't know yet."

I'm a big advocate of the "optimize later" approach. Whenever I bring this up, people accuse me of advocating slow, bloated applications. But the fact of the matter is that "optimize later" is how you make the _fastest possible application_, given all of the other constraints. From the perspective of airplane design, what most programmers mean by "optimization" is stuff like drilling holes in panels to reduce the weight: it can be a big advantage, but if you spend all of your time drilling holes early in the game, the product as a whole is going to suffer badly.

**Wrapping Up**  
 That's it for this week's Friday Q&A. Leave your feedback and hate mail in the comments below. Also please leave any ideas you might have for future Friday Q&As, or if you prefer, you can [e-mail them to me](mailto:mike@mikeash.com) (and tell me explicitly if you don't want me to use your name). Friday Q&A runs on your ideas so please contribute early and often.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-02-27-holistic-optimization.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
