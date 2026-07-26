---
title: Run-time Polymorphism in Swift
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/'
original_language: en
published: 2024-04-06
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9937df14dd40ba8a'
translated: false
---

> 原文：[Run-time Polymorphism in Swift](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Online Communication](https://belkadan.com/blog/2024/01/Online-Communication/)

[XZ Gon' Give It To Ya](https://belkadan.com/blog/2024/04/XZ-Gon-Give-It-To-Ya/) »

« [GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=swift)

« [Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=programming-languages)

## [Run-time Polymorphism in Swift](#)

This has come up several times on the forums over the years, but I’ve never written it up in a standard place, so here it is: **There are only three ways to get run-time polymorphism in Swift.** Well, three and a half.

What do I mean by _run-time polymorphism?_ I mean a function/method call (or variable or subscript access) that will (potentially) run different code each time the call happens. This is by contrast with many, even _most_ other function calls: when you call Array’s `append`, it’s always the same method that gets called.

So, what are the three, sorry, three and a half ways to get this behavior?

- [Calling a function value](#calling-a-function-value) (closure)
- [Calling a class member](#calling-a-class-member)
- [Calling a protocol requirement](#calling-a-protocol-requirement)
- [Manually testing the type of a value](#manually-testing-the-type-of-a-value)

### Calling a function value

This one’s kind of obvious. If you’re calling a callback, it can be anything that matches the function type, depending on where it’s coming from.

### Calling a class member

A non-`final` method on a non-`final` class may be overridden in subclasses, so calling a class method does dynamic dispatch based on the run-time type of `self`. This is the most familiar, object-oriented notion of “polymorphism”, and it’s usually not surprising to people.

Note that “class method” is kind of ambiguous: this rule applies to instance methods and type-level methods (and to properties, subscripts, and `required` initializers). In a class, however, `static` is equivalent to `class` plus `final`, so in that case there won’t be any dynamic dispatch.

There’s actually one more place where class members are dynamically dispatched, and that’s the very specific case of convenience initializers. The call to `self.init` _within_ a convenience initializer is dynamically dispatched, which is why convenience initializers are only inherited if you provide all the non-convenience initializers of your superclass. This is a pattern from Objective-C turned language feature in Swift, and yeah, [maybe it’s more complexity than we really needed](https://github.com/apple/swift/blob/swift-5.10-RELEASE/docs/InitializerProblems.rst).

### Calling a protocol requirement

This one’s also not too surprising; after all, the whole point of protocols is that they provide a common API implemented by concrete types. What might be surprising is that members added in extensions to the protocol do _not_ get to participate in this behavior. If you think about it, though, supporting that would mean that _at run time_ the program would have to look at all the possible methods a concrete type has and see if any of them match this extension method. If more than one matched, the runtime system would have to perform _overload resolution._ And what if that comes out ambiguous? So no, extension methods are either chosen directly at compile time, or passed over directly at compile time; whether they get called is entirely determined by static type information, not run-time polymorphism.

### Manually testing the type of a value

This doesn’t really count, but it’s here because sometimes it really is the best answer to a problem. Swift does not provide perfect [parametricity](https://www.seas.upenn.edu/~cis1940/spring13/lectures/05-type-classes.html); you can attempt to downcast/convert to a more specific type whenever you want with `is` and `as?` expressions, or with `is` and `as` patterns:

```
if firstPet is Cat, let secondPet = secondPet as? Dog { /* … */ }
```

```
switch thirdPet {
case is Cat:
  /* … */
case let thirdPet as Dog:
  /* … */
default:
  break
}
```

Whether or not this is a good idea is partly a matter of tradeoffs and partly of taste, but Swift does allow it.

### Aside: What about generics?

Generics are a powerful and flexible tool, but in general they don’t result in any more run-time polymorphism than `any` types (formerly “protocol composition types”). This often throws people who are used to C++ templates, where overload resolution is done on the _concrete_ type that satisfies the generic constraints rather than on the _generic_ type. Swift didn’t choose that option for two main reasons: it makes it much harder to diagnose issues at compile time, and it means that the entire body of the generic has to be visible to callers (so they can substitute in the concrete type). This is good for optimization, but bad for library evolution. You can think of Swift’s model as “the decision of which overload to call is made based on the knowledge where the call is written, which in this case is inside a generic function with certain constraints”.

I don’t know of any other modern languages that have templates like C++, but there’s still a choice between _monomorphization,_ i.e. generating a separate copy of the code for every concrete type, and _polymorphic_ generics, where a single copy of the code uses dynamic dispatch to work on many different types.^[1](#fn:optimizer) Different languages take different approaches to this:

| Language | Generics are… | Generic types are… | Overloads are resolved… |
|---|---|---|---|
| C++ | monomorphized | expanded into concrete types | on the concrete types (hence “template”) |
| Rust | monomorphized | expanded into concrete types | based on constraints |
| Swift | polymorphic | expanded into concrete types (but sometimes indirected) | based on constraints |
| Java | polymorphic | “erased” to their constraints | based on constraints |
| Objective‑C | polymorphic | “erased” to their constraints | what’s an overload^[2](#fn:objc) |

There _is_ now a way to get C++-like behavior in Swift (and Rust): macros. But Swift’s macros are _entirely_ syntactic and have to be invoked explicitly, so they don’t naturally lend themselves to C++ template-style usage, at least not today. So sometimes instead this is where the “3.5” solution comes into play: a dynamic cast inside the body of a generic method acts as a form of “specialization”, even though it does have a checking cost at run time.

### Takeaways

So let me re-iterate: the three-and-a-half features listed at the top are the _only_ forms of run-time polymorphism in Swift. Now when someone asks “how can I allow arbitrary different argument types to result in different behavior”, you know the answer: make a protocol. (Or piggyback on a base class, if they’re already classes in a hierarchy you own.) When someone asks “why didn’t this method call pick the more specialized overload”, you know the answer: generics aren’t templates, overload resolution happens based on the generic constraints alone, and they may want to make a protocol. And when someone asks “hey, how do I make my protocol extension methods overridable?”, you know the answer: you have to make _another_ protocol (and possibly downcast to it from the original type).

…Look, the tagline “protocol-oriented programming” may be a bit of a buzzword, but we weren’t kidding! Protocols are your tool for run-time polymorphism, and polymorphism in general, that works on value types. Use them!

1. Optimizations blur these distinctions. C++ or Rust code may generate many copies of the same function, but then optimize them back into one function if they have the same behavior at the machine code level, or at least _outline_ the common parts of the function to save on code size. Like inlining, this is something that’s often based on heuristics and other settings, and is still an area of active development (or at least was a few years ago). Conversely, while Swift formally uses a single definition for every version of a generic function, it sometimes _specializes_ them for particular concrete types to increase performance at the cost of code size. [↩︎](#fnref:optimizer)
2. I joke, but actually Objective-C _does_ care about doing _some_ type-checking on method calls for generics, to get the right calling convention. You just can’t call a method that’s declared to return `float` in one place and `id` in another, and so the compiler will complain if you try to call a method that’s not in the parameter’s constraints at all.

  I also snuck in Rust overloads. Rust _does_ have overloading, even though it pretends not to: separate traits can declare methods with the same name, and a caller is required to disambiguate between them manually if both traits are valid. [↩︎](#fnref:objc)

This entry was posted on [April](https://belkadan.com/blog/2024/04) 06, [2024](https://belkadan.com/blog/2024) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Programming languages](https://belkadan.com/blog/tags/programming-languages)
