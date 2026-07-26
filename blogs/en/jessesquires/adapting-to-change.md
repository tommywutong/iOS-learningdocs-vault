---
title: Adapting to change
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2017/02/15/adapting-to-change-and-cutting-corners/'
original_language: en
published: 2017-02-15
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6a0ea904c21abd6e'
translated: false
---

> 原文：[Adapting to change](https://www.jessesquires.com/blog/2017/02/15/adapting-to-change-and-cutting-corners/)　·　Jesse Squires

In my [previous post](https://www.jessesquires.com/blog/2017/02/10/refactoring-singletons-in-swift/) I mentioned writing _adaptive_ code. That is to say, writing code that is easy to change, code that is malleable. It’s like creating [adaptive user interfaces](https://www.jessesquires.com/blog/2014/10/01/adaptive-user-interfaces/) but for all of your classes, modules, and other components.

> Building and designing good software means writing code that is **easy to change, but difficult to break.**

#### * * *

Software evolves too rapidly to predict. We cannot always foresee the changes we will need to make to accommodate new features or fix systemic bugs. What we can do is avoid backing ourselves into a corner, locking the door, and throwing away the key. We can avoid situations where the only (seemingly) viable solution is to destroy everything and [start from scratch](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/).

To [make progress](http://robnapier.net/refactoring) and actually ship code, you _will_ have to cut corners. Sometimes you will have to cut a lot of them. Some corners can easily be cut, while others should **never** be cut. Those are the corners that back you into a corner from which you cannot escape.

#### * * *

No one has a [perfect and pure object graph](https://twitter.com/sqlabs/status/789127047922774016) with perfectly modularized components. That is for what we strive, constantly [refactoring](https://martinfowler.com/books/refactoring.html). The more code we write, the more code we ship, and the more mistakes we make, the better our corner-cutting strategies and backed-into-a-corner-avoiding abilities will become. It takes a lot of shitty code and many bad ideas to finally arrive at slightly better code and a few great ideas.
