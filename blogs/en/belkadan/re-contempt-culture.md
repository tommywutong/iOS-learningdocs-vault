---
title: 'Re: Contempt Culture'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2015/12/Re-Contempt-Culture/'
original_language: en
published: 2015-12-29
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:68baed3e26458964'
translated: false
---

> 原文：[Re: Contempt Culture](https://belkadan.com/blog/2015/12/Re-Contempt-Culture/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Recommendations](https://belkadan.com/blog/2015/11/Recommendations/)

[So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/) »

« [Recommendations](https://belkadan.com/blog/2015/11/Recommendations/?tag=programming-languages)

[The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/?tag=programming-languages) »

« [AlterConf SF/Oakland](https://belkadan.com/blog/2015/02/AlterConf/?tag=diversity-in-tech)

[So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/?tag=diversity-in-tech) »

## [Re: Contempt Culture](#)

Two weeks ago Aurynn Shaw wrote a piece called “[Contempt Culture](http://blog.aurynn.com/86/contempt-culture)”:

> OKAY finally got it together. My post on why you need to shut up on bashing languages [http://blog.aurynn.com/86/contempt-culture](http://blog.aurynn.com/86/contempt-culture)
> 
> — cute af (@aurynn) [December 16, 2015](https://twitter.com/aurynn/status/676918280062373888)

And even before I finished reading it I had a thought:

> _Oh, this is not the article I expected to be reading._

So here’s the article I thought I was going to read, based on the tweet. A short version, anyway.

---

If you’re like me, you probably have a language (at least one) that you think of as _completely bad._ The big one is PHP, which has entire websites devoted to its problems. There’s also C++, Java, JavaScript, BASIC…did at least one of these make you cringe a little?

I’m here to tell you that that instinct will get you into trouble. Here’s an excerpt from Shaw, minus a part of _her_ point so that I can make _my_ point:

> If [programmers using these languages] say what they use, we as a culture laugh at their choice. We tell them they should know better, tell them that it’s a horrible tool. Tell them that they are _wrong._ We ignore the achievement and focus exclusively on how it was reached, on how much _better we are_ because we had access to narratives that the broader culture had already deemed _more real._

Shaw points out that this is exclusionary and drives other programmers away. That’s _already_ a good enough reason to think twice about what we’re doing, but if you need another one:

**If you dismiss something out of hand, you can’t learn from it.**

That applies both to what it does poorly and what it does well. You’re likely to have some examples of the former (presumably you have some idea of why the language is considered “bad”), but that doesn’t mean you won’t make some _other_ mistake that you didn’t realize has been made before. As for the latter…

- PHP was (and arguably still is) great for templating—the sort of thing [Liquid](http://liquidmarkup.org) is used for (e.g. on GitHub Pages), but more powerful.
- C++ has supported Swift-style value semantics from the start.
- Java has a level of access control, “package”, between “just this file” (`private`) and “the entire world” (`public`). It’s even the default, just like in Swift.
- JavaScript’s compact object literal syntax is used as today’s interchange format (JSON).
- BASIC allows top-level imperative code, while most of its contemporaries didn’t.

These things may not be unique to these languages, but they’re still things I’d consider _good ideas._ And as someone heavily involved in [designing a language](https://swift.org), ideas _matter._ That of course doesn’t mean shoveling features into Swift until it can do absolutely everything, but if we _do_ want to add a feature, and another language got it right, we can and should (and do) follow that lead.

So I agree with Shaw: we should stop bashing languages, tools, libraries, etc. both because it drives away ideas and because it drives away people.

---

P.S. Did you read [Shaw’s post](http://blog.aurynn.com/86/contempt-culture) yet? Cause she’s right about all the human aspects here, and those are probably more important in the long-term.

P.P.S. David MacIver posted his own follow-up entitled “[On criticizing programming languages (without criticizing their users)](http://www.drmaciver.com/2015/12/on-criticizing-programming-languages/)”, which is about exactly that. In particular, the “guidelines for constructive criticism” at the very end are worth keeping in mind.

This entry was posted on [December](https://belkadan.com/blog/2015/12) 29, [2015](https://belkadan.com/blog/2015) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Programming languages](https://belkadan.com/blog/tags/programming-languages), [Diversity in tech](https://belkadan.com/blog/tags/diversity-in-tech)
