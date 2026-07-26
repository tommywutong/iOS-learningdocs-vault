---
title: Swift Compiler Diagnostics
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/08/swift-compiler-diagnostics/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e9e5f482638d4fc4'
translated: false
---

> 原文：[Swift Compiler Diagnostics](https://oleb.net/blog/2015/08/swift-compiler-diagnostics/)　·　Ole Begemann

# Swift Compiler Diagnostics

One of my favorite things in the release notes of the last few Xcode 7 beta releases has been this rather vague item:

> Type checker diagnostics continue to improve in precision and specificity.

Unhelpful error messages can be a big blow to productivity, especially when you have to deal with an evolving language and a compiler that still has some rough edges. And the Swift compiler definitely has lots of room for improvement in this area. It’s good to see that the Swift team is aware of the problem and is actively working on providing better diagnostics.

# Example

Here’s a concrete example of one such improvement that I noticed recently. Consider this simple piece of code, in which I want to construct an array of strings by mapping over a range of numbers:

```
let xs = 1...10.map(String.init)
```

This code doesn’t compile. Can you spot the problem? If so, great. If not, let’s see if the compiler can help us.

## Beta 3

In Xcode 7 beta 3, it would give the following error message:

```
Could not find an overload for 'init' that accepts the supplied arguments
```

I don’t know about you, but to me this suggests that something is wrong with the `String.init` part. I had seen previously that referring to initializers as function values [doesn’t always work as expected](https://twitter.com/nnnnnnnn/status/616696761889861632), so I would probably try to use an inline closure next:

```
let xs = 1...10.map { String($0) }
```

And beta 3 would reply with this error message:

```
Cannot invoke 'map' with an argument list of type '((_) -> _)'
```

Really, I have no idea what you want to tell me.

## Beta 5

Let’s try the same in Xcode 7 beta 5:

![The Swift compiler displays an error message in Xcode](https://oleb.net/media/swift-compiler-error-message.png)

<sub>With the right error message, the fix is trivial.</sub>

```
let xs = 1...10.map(String.init)
// error: value of type 'Int' has no member 'map'
```

Ah, now we’re getting somewhere. Apparently, the compiler tries to invoke `map` on an `Int`, which would explain why the code doesn’t work. It also highlights the `10` to indicate the location of the problem. With this information, it’s easy to see my mistake: I had incorrectly assumed that the range operator `...` had a higher precedence than function application. The fix is to add parentheses around the range:

```
let xs = (1...10).map(String.init)
// => ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
```

---

If you spotted my mistake right away, you might think this is a trivial example. Perhaps, but if an improved error message can save you just a few minutes of frustration (and, more importantly, help not to interrupt your flow), I consider it a big win. Thanks, Swift team!

# Radars Work (Sometimes)

I filed an enhancement request with this specific example on July 17, 2015, and not even three weeks later it was fixed. And although I have no idea if my bug report played a role in this (I didn’t receive a reply), I do know that the Swift team needs our feedback to understand where we struggle with the compiler. So the next time you come across an error message you find misleading or confusing, please file a bug. It usually [only takes a few minutes](http://www.quickradar.com/).
