---
title: Over-abstraction
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2017/09/Over-abstraction/'
original_language: en
published: 2017-09-05
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:6154ca61effc11c1'
translated: false
---

> 原文：[Over-abstraction](https://belkadan.com/blog/2017/09/Over-abstraction/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Macromancy, Part 2](https://belkadan.com/blog/2016/08/Macromancy-2/)

[The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/) »

[The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/?tag=functional-programming) »

[The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/?tag=math) »

## [Over-abstraction](#)

Back in July I got myself into a [discussion on Twitter](https://twitter.com/UINT_MIN/status/887348345831698432) about whether some of the more algebraic concepts in functional programming were net-useful, after reading [Brandon Williams](http://www.fewbutripe.com)’ (great) articles on how they can be applied in Swift. [Brandon Kase](http://hkr.me) suggested I watch his talk “Beyond Types in Swift” from this year’s [Functional Swift](http://2017.funswiftconf.com) conference.more

I admit I’m still unconvinced. I also admit that I might still just not get it. But I had two interesting thoughts that I wanted to write out in longform. I thought about cramming them both into one article, but figured it’d be better for discussion purposes to just do one at a time. So this is an exploration of the first idea, “Over-abstraction”.more The next one will come in about a week or so.

(I’ve already loaded the discussion just from the title, but hey, it’s my blog.)

---

I think this is my primary problem with using algebraic abstractions for programming. It’s _true_ to say that functions and Optionals are both [Monoids](http://hackage.haskell.org/package/base-4.10.0.0/docs/Data-Monoid.html), but is it useful? The criterion for this in the Swift standard library is usually “can you define any meaningful reusable generic operations on this protocol?”.

I’m not going to directly talk about whether Monoid itself has useful generic operations; it’s just an example. But it leads to people writing code like this:

```
let fullArticle: View<Article, [Node]> =
  articleHeader
    <> articleBody
    <> articleFooter
```

(from Williams’ “[Composable HTML Views in Swift](http://www.fewbutripe.com/swift/html/dsl/2017/06/29/composable-html-views-in-swift.html)”)

The trouble is I (hyperbolically) have no idea what that means. Because `<>` (or `mappend` in Haskell) is a high-level operation, I know that it has certain properties I can rely on, like [associativity](https://simple.wikipedia.org/wiki/Associativity). But I don’t know what that means for a `View`. I can _guess,_ but the generic name is in the domain of the abstraction rather than the concrete type.

---

Let’s take an example from human language. Imagine a friend has a problem with their bird feeder: the seeds keep getting eaten before the birds can get there. “What’s been eating them?”, you ask. Now, it would be _valid_ for your friend to say “mammals keep eating the seeds”, but you’d probably give them a funny look. “Cats and squirrels” would go over much better. If the abstraction level is too far removed from the domain, things get _harder_ to understand.

(This also works in reverse. “Siamese cats, Maine coons, and Western gray squirrels” would be considered an over-specific answer. _Some_ abstraction is usually a good thing.)

To stretch the example even further, let’s say you wanted to ask if the cats and squirrels could reach the bird feeder directly from the ground with their legs, or if they had to climb something to get to the delicious birdseed. But not all mammals have legs, so instead you have to ask whether their _appendages_ are long enough. You’ve used the correct general term, but now it’s harder to understand.

I’ve tortured my poor metaphor enough, but hopefully you see what I’m getting at.

---

Note that we already have some of this problem with just the Swift standard library. A [Set](https://developer.apple.com/documentation/swift/set) is a [Sequence](https://developer.apple.com/documentation/swift/sequence), which means you can call `dropFirst` on it. What’s the first element of an unordered set? What’s the “rest”? And yet you _can_ use this to build useful reusable operations on Sequence, and then it’s useful to be able to apply those operations to a Set.

So, my thesis: Abstractions are good because they let you reuse both your intuitions and your code across different types…but they can also hurt comprehension when working with a type concretely. That leads to having to choose between sacrificing the domain-specific name in favor of the generic name, and having two names for the same operation.

(Also, it doesn’t help that the names chosen by mathematicians don’t feel very approachable.)

---

I _do_ want to highlight some of the important criteria for inclusion of a new protocol in the Swift standard library:

- Are there generic operations that work with this protocol? That is, will there be protocol extension methods, or somewhere that uses this protocol as a generic constraint?
- Is there more than one concrete type that would conform to this protocol?
- If this protocol is part of a hierarchy, are there types that conform to the parent protocol and not this one? If not, it’s probably not worth making a separate protocol for it.
- Does the operation have any semantic requirements? (This is what keeps String’s `+` and Int’s `+` from being in a protocol.)

These criteria gave us the distinctions between [Sequence](https://developer.apple.com/documentation/swift/sequence), [Collection](https://developer.apple.com/documentation/swift/collection), [BidirectionalCollection](https://developer.apple.com/documentation/swift/bidirectionalcollection), and [RandomAccessCollection](https://developer.apple.com/documentation/swift/randomaccesscollection), but not between [Numeric](https://developer.apple.com/documentation/swift/numeric) and a hypothetical “[Additive](https://en.wikipedia.org/wiki/Semiring#Definition)” that doesn’t support subtraction. There just aren’t enough concrete types that only support addition _and_ still make sense to write generic algorithms over for this to be in the standard library.

How the algebraic abstractions we’ve been talking about match up against these criteria is a matter of debate. And of course, just because something’s not in the standard library doesn’t mean it can’t be useful. But I think the loss of domain-specific terminology is a high price to pay in the common case; the benefit you get should be commensurate.

---

P.S. One idea that came out of the original Twitter discussion was a distinction between abstractions as _protocols_ (“type classes” in Haskell) and abstractions as _[design patterns](https://twitter.com/dimsumthinking/status/887498387293167618)._ It’s _useful_ to know when an operation is associative, because that lets you perform folds (`reduce`) in parallel; this is a key part of the “[semigroup](http://www.fewbutripe.com/swift/math/algebra/2015/02/17/algebraic-structure-and-protocols.html#semigroup)” abstraction. And even when you can’t build meaningful generic operations on top of a particular abstraction, it may still be useful to other developers reading your code or using your types to get that shared intuition of how something behaves.

However, the difference between a design pattern and a language feature is that the compiler usually won’t check that you’re using a design pattern correctly, which means using actual protocols does have value. I’ll return to this idea in [the next (much longer) post](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/).

P.P.S. After I posted this, Brandon Williams made a [bit of a response](https://twitter.com/mbrandonw/status/905458906121547778) in tweetstorm format, and Elviro Rocca made a [blog post](https://broomburgo.github.io/fun-ios/post/on-abstraction/) a few days after. You can also read [other Twitter people’s responses](https://twitter.com/UINT_MIN/status/905452666771226624).

This entry was posted on [September](https://belkadan.com/blog/2017/09) 05, [2017](https://belkadan.com/blog/2017) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Functional programming](https://belkadan.com/blog/tags/functional-programming), [Math](https://belkadan.com/blog/tags/math)
