---
title: AnyObject
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/07/AnyObject/'
original_language: en
published: 2024-07-02
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:67a612dc4c63b324'
translated: false
---

> 原文：[AnyObject](https://belkadan.com/blog/2024/07/AnyObject/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [XZ Gon' Give It To Ya](https://belkadan.com/blog/2024/04/XZ-Gon-Give-It-To-Ya/)

[The Shell is a Program](https://belkadan.com/blog/2024/12/The-Shell-is-a-Program/) »

« [Run-time Polymorphism in Swift](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/?tag=swift)

## [AnyObject](#)

When is AnyObject not AnyObject? When it’s a protocol type.

Swift has a type called AnyObject that represents a single reference-counted object, with no available operations.^[1](#fn:objc) This doesn’t sound very useful, but sometimes you’re just using the object for its lifetime (a sort of dynamic RAII), and other times you’re planning to downcast it to a concrete type.

AnyObject can also be used as a generic constraint. If you use `T: AnyObject`, you’re guaranteed that T will have that single-object-reference representation. This allows you to have `weak` and `unowned` references to T, as you might expect.

You can also use AnyObject as a constraint on protocols: `protocol MyDelegate: AnyObject`. Now the implementers are known to have reference semantics, and with `T: MyDelegate` you can have weak references to T, as before. You can even have weak references to `any MyDelegate`, allowing swapping between delegates of different types.

What you might run into, though, is that `any MyDelegate` is not itself AnyObject.

(What?)

If you try to use `any MyDelegate` as a `T: AnyObject`, you’ll find the compiler is unhappy with you. Even though every concrete MyDelegate type is a valid AnyObject type, `any MyDelegate` itself is not. Why not? Because it carries more information than just a single object reference: it also has a “witness table” pointer, the run-time representation of a protocol conformance. That’s how protocol types (`any` types) _work_ in Swift: they have the normal value, stored in-line or out-of-line depending on size, plus the additional witness table that’s full of method pointers, basically. When you call a protocol method through an `any` type, the code at run time will look in the table that was given, and pull out the appropriate implementation of that method, then call it using the value part as `self`.^[2](#fn:extension)

But wait, Objective-C never had this problem! The `id <MyDelegate>` type doesn’t take up more than a single-object-reference to store! But that’s because ObjC protocols aren’t represented as tables of methods; they’re just promises that the implementing class _has_ methods with particular names. So the “table” for a protocol is the same as the “table” for _all_ of a class’s methods…at the cost of a single namespace for method names (selectors) and a bit of extra overhead on app launch and on method calls. And that’s stored in the type, and every object knows its type, so there’s no secondary pointer attached to the value.

(Was this a good tradeoff? A big question, with a lot more in the balance than just the representation of protocol types. Another time, perhaps.)

So that’s why Swift class-constrained protocol types are just a _bit_ less convenient than ObjC ones. You can still convert values to AnyObject, you can still reference them weakly or unownèdly, you can still trust that they have a fixed cost to copy and move. And you can still use the protocol as a constraint and get all the same effects. But you can’t mix the two, because `any MyDelegate` does not itself have an `AnyObject` representation.

1. [This is a lie on Apple OSs](https://belkadan.com/blog/2021/08/Swift-Regret-AnyObject-Dispatch/), but I encourage everyone to act as if it were true. [↩︎](#fnref:objc)
2. This is also why methods defined in a protocol extension are statically resolved: they’re not in the table. And separately-compiled modules means it may not be _possible_ to put them in the table. So there’s just one rule, and that’s that only the requirements of the protocol are [dynamically dispatched](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/). [↩︎](#fnref:extension)

This entry was posted on [July](https://belkadan.com/blog/2024/07) 02, [2024](https://belkadan.com/blog/2024) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift)
