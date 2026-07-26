---
title: Learnable Programming
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/09/learnable-programming/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:488ebd7effa63a36'
translated: false
---

> 原文：[Learnable Programming](https://oleb.net/blog/2012/09/learnable-programming/)　·　Ole Begemann

# Learnable Programming

Bret Victor in an essay titled [Learnable Programming – Designing a programming system for understanding programs](http://worrydream.com/LearnableProgramming/):

> Think about this. We expect programmers to write code that manipulates variables, without ever seeing the values of those variables. We expect readers to understand code that manipulates variables, without ever seeing the values of the variables. _The entire purpose of code is to manipulate data, and we never see the data._ We write with blindfolds, and we read by playing pretend with data-phantoms in our imaginations.
> 
> Information design pioneer Edward Tufte has one primary rule, and this rule should be the principle underlying any environment for creating or understanding.
> 
> _Show the data._
> 
> If you are serious about creating a programming environment for learning, the _number one thing you can do_ – more important than live coding or adjustable constants, more important than narrated lessons or discussion forums, more important than badges or points or ultra-points or _anything else_ – is to _show the data_.

This may be the best thing I have read this year. Highly recommended to anybody who is at all interested in programming. Despite its focus on teaching and learning programming, Bret’s essay also points out the poor state of our current IDEs, despite all their refactoring and navigation capabilities.

What Bret proposes is way ahead of how our current IDEs work. Yet, as he illustrates with many small videos, it’s a goal that is far from being unreachable. It does require a total change in the mindsets of developers and designers of programming tools, though. And it’s a worthy goal:

> Programming has to work like this. Programmers _must_ be able to read the vocabulary, follow the flow, and see the state. Programmers _have_ to create by reacting and create by abstracting. Assume that these are _requirements_. Given these requirements, how do we _redesign programming_?
> 
> … How do we design data structures that can be visualized? Can we invent data structures that are intended to be visualized? How do we move towards a culture where only visually-understandable data is considered sound? Where opaque data is regarded in the same way that “goto” is today?

And visual programming is not the answer:

> [V]isual programming is indeed worthless. But that’s because it visualizes the wrong thing. Traditional visual environments visualize the code. They visualize static structure. But that’s not what we need to understand. We need to understand what the code is doing.
> 
> Visualize data, not code. Dynamic behavior, not static structure.

If, after reading the essay, you can’t get enough of Bret’s work, watch his [talk titled Inventing on Principle](https://vimeo.com/36579366) next. It explores some of the same ideas with extremely cool live demos.
