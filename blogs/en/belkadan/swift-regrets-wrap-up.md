---
title: 'Swift Regrets: Wrap-up'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/'
original_language: en
published: 2021-12-31
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f9f8a51aaaf11e78'
translated: false
---

> 原文：[Swift Regrets: Wrap-up](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift History: Assignment Methods](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/)

[Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/) »

« [Swift History: Assignment Methods](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/?tag=swift)

[Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=swift) »

« [Swift History: Assignment Methods](https://belkadan.com/blog/2021/12/Swift-History-Assignment-Methods/?tag=swift-regrets)

« [Swift Regrets](https://belkadan.com/blog/2021/09/Swift-Regrets/?tag=programming-languages)

[Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=programming-languages) »

## [Swift Regrets: Wrap-up](#)

Thus ends five months of [Swift regrets](https://belkadan.com/blog/2021/09/Swift-Regrets/) (and delights), things that I had been collecting during my last year at Apple…and things that came up during the ensuing discussion on Twitter. I wanted to talk about these things because every project learns from those that came before it, and that should include both the good parts and the bad parts. I have a memory of my former colleague [Joe Groff](https://twitter.com/jckarter) saying that we should normalize and encourage talking about mistakes and missteps in our field, and so this is a contribution.more

All of the Twitter threads have been collected on this site under the “[Swift regrets](https://belkadan.com/blog/tags/swift-regrets/)” tag. It’s not an exhaustive list of all things good or bad about Swift, but it does span quite a range. My personal favorite is probably one of the first ones I did, [Sequence](https://belkadan.com/blog/2021/08/Swift-Regret-Sequence/). It lays out the problem and the possible solution well—in my opinion, of course.

So what are the takeaways from this series? Besides “\<feature\> was a mistake, think twice about including a similar feature in your language”, I think we can probably come up with a few high-level ideas, the most important being that at some point in language work you don’t get to change things anymore! This is a limitation that just doesn’t apply to the majority of software projects, just (widely-adopted) languages, libraries with ABI stability, and interchange formats. Everywhere else you can introduce a new major version that replaces the old one and people will either move over or not—it might be difficult but it’s always an _option_. I think this is a culture shock for people coming from most open source projects, or straight-up app projects. (And I’m saying all this knowing the _massive_ number of changes from Swift 1b1 to Swift 3, so to think there were things that _still_ didn’t / couldn’t get fixed…)

That’s the most important thing. Some more regrets-related advice:

- It’s easier to add capabilities or remove restrictions than the reverse. People will immediately start using any features provided, especially if they’re the only way to accomplish a task, and even if you introduce a universally acclaimed better feature later, removing the old one becomes a breaking change.
- If you’re _going_ to make breaking changes, make them boldly, because you probably won’t get another chance.
- Make your most ambitious changes early, so you can try them out and tweak them…and revert them if necessary.
- That said, don’t add anything that seems “cool” or “clever” or even “obvious” unless you can cite real-world uses. Otherwise, it might be a trap, or extra complexity, or at the very least something else to maintain forever.
- Relatedly, if something’s not supported in another language with a similar feature, maybe there’s a reason.
- Implicit can be convenient, but it may also be a bad default.
- Consistency is good: less implementation and less to learn.
- But unrelated features can also interact in weird ways.
- Getting to go back and redo something properly is rare; your first version better be good enough to last forever even if you want to go back and fix it.
- Relatedly: perfect is the enemy of the good and good is the enemy of the perfect. Yes, it’s a problem in both directions.
- But sometimes you just won’t know you’ve built the wrong thing until you’ve seen it used. And sometimes there’s not obviously a right answer.

On the “delight” side, I think it’s less obvious what might tie everything together, but here are a few thoughts:

- Some of my favorite things about Swift are tweaks on what other languages already had. Sometimes the best thing you can do isn’t create from scratch but polish and make accessible…or straight-up do the same thing as someone else, if it’s the right thing. (That’s a very Apple approach.)
- Similarly, you may not be able to break compatibility yourself, but you can find all the places other people _wish_ they could break compatibility and follow that.
- All the usual pithy quotes like “easy things should be easy and hard things possible”, “API should steer you towards correct use”, “[clarity over brevity](https://swift.org/documentation/api-design-guidelines/)”, etc.

Given all this, I should probably again answer the question of “isn’t it worth breaking compatibility if it makes things better?” When you’re talking about a programming language, the old version _doesn’t go away,_ doubly so if you can import an old-version library at compile time and triply so with ABI stability on Apple platforms. Breaking compatibility means alienating your users or maintaining multiple versions for years to come, or more likely both, so the changes had _better_ be worth it. (There is a scale question here too: there are millions of developers for Apple platforms and in turn probably a billion users.)

I should also repeat that the takeaway is _not_ “Swift is a failure, look at all these things wrong with it”. _All_ languages have lists like this; the reason I did this for Swift is because I worked on Swift and can provide insight as to how and why things ended up the way they did. I’d love to see posts and threads from other language designers about what they regret and what’s held up well.

The series has generated a lot of good discussion, and in particular I want to give a shout-out to [Dave Zarzycki](https://twitter.com/davezarzycki), who also worked on early Swift as well as a number of other projects in his many years at Apple (including the original launchd). In one of our private conversations he came up with this, talking about a language that’ll last for years and be suitable for large collaborative projects:

> Assume success and solve the _people_ scaling problems as soon as possible. That’s it.
> 
> That being said, it’s a massive amount of work. It means getting a ton of defaults right, thinking hard about features interact with each other, progressive disclosure, planning for API evolution and resiliency etc, etc.
> 
> More so, it means foregoing some of the traps-of-convenience that new PLs are often tempted by (like haphazard implicit conversions)

And that all seems like good advice to me.

If you’re looking for more language design retrospection, I suggest [Joe Duffy’s series on Midori](http://joeduffyblog.com/2015/11/03/blogging-about-midori/), a Microsoft language and _operating system_ project that started a few years before Swift did. The project was eventually discontinued and the developers folded back into other parts of Microsoft, but its aims were even more ambitious than Swift’s, and there are both some striking similarities and some things we could have learned from.

Thanks for following along these five months. See you in 2022.

This entry was posted on [December](https://belkadan.com/blog/2021/12) 31, [2021](https://belkadan.com/blog/2021) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift regrets](https://belkadan.com/blog/tags/swift-regrets), [Programming languages](https://belkadan.com/blog/tags/programming-languages)
