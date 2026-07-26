---
title: Rob Rix on Postmodern Programming
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/10/rob-rix-postmodern-programming/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2b2a9a23b93a765a'
translated: false
---

> 原文：[Rob Rix on Postmodern Programming](https://oleb.net/blog/2013/10/rob-rix-postmodern-programming/)　·　Ole Begemann

# Rob Rix on Postmodern Programming

Rob Rix published a transcript titled [Postmodern Programming](https://github.com/robrix/Postmodern-Programming/blob/master/Postmodern%20Programming.md) of the talk he gave at CocoaConf Columbus 2013:

> But part of what I think about when I think of “declarative programming” is the notion that you are constructing a system of objects at runtime out of which the desired behaviour falls naturally: a necessary consequence of the structure.
> 
> To give an example of this, the appearance of a view hierarchy is a consequence of the structure of the views, and their arrangement and visual properties. All of these are declared properties of the view controllers; in this sense, we can think of a view hierarchy as being a declarative system, whose value is the contents of the layer, or perhaps the screen buffer.
> 
> View controllers have a similar hierarchy which provides the semantic structure of the app; this, and the paths through which the user will be taken at runtime, is the structure made explicit in storyboards.
> 
> Views and view controllers are, basically, a solved problem—Apple has provided these things, and by and large we use them. It’s important to realize, however, that they have not cornered the market. We solve problems all day every day, generally more than we cause; that’s why anyone bothers to pay us. Some of these problems are likely to have declarative solutions (after all, if you can’t talk about what these things are, then what are they, really?); some of those declarative solutions may well be qualitatively better than how we might be solving them otherwise—in fact, I think that’s extremely likely, given what we’ve seen about their behaviour with regard to time and ordering relative to imperative solutions.

I’d love to quote the whole thing.

In the wake of [ReactiveCocoa](https://github.com/ReactiveCocoa/ReactiveCocoa) and other libraries, non-imperative programming paradigms have gained a lot of mindshare in the Objective-C community lately. And while I haven’t found the time yet to play with these approaches in large projects, I have definitely experienced the “discomfort” that Rob cites and many of us feel with the “standard” way of writing Cocoa apps.

I found Rob’s talk to be a great overview of the ideas behind declarative programming. It doesn’t offer any fully baked solutions but it has given me a lot of food for thought. Highly recommended.
