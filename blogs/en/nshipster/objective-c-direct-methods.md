---
title: Objective-C Direct Methods
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/direct/'
original_language: en
published: 2019-12-16
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:e187e6c924ca6a42'
translated: false
---

> 原文：[Objective-C Direct Methods](https://nshipster.com/direct/)　·　NSHipster (Mattt)

# [Objective-C Direct Methods](https://nshipster.com/direct/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  December 16^th, 2019

It’s hard to get excited when new features come to Objective-C. These days, any such improvements are in service of Swift interoperability rather than an investment in the language itself _(see [nullability](https://developer.apple.com/swift/blog/?id=25) and [lightweight generics](https://developer.apple.com/documentation/swift/imported_c_and_objective-c_apis/using_imported_lightweight_generics_in_swift))_.

So it was surprising to learn about [this recently merged patch to Clang](https://reviews.llvm.org/D69991), which adds a new direct dispatch mechanism to Objective-C methods.

The genesis of this new language feature is unclear; the most we have to go on is an Apple-internal [Radar number](https://nshipster.com/bug-reporting/) ([`2684889`](rdar://2684889)), which doesn’t tell us much beyond its relative age (sometime in the early ’00s, by our estimation). Fortunately, [the feature landed](https://github.com/llvm/llvm-project/commit/d4e1ba3fa9dfec2613bdcc7db0b58dea490c56b1) with enough documentation and test coverage to get a good idea of how it works. _(Kudos to implementor Pierre Habouzit, review manager John McCall, and the other LLVM contributors)_.

This week on NSHipster, we’re taking this occasion to review Objective-C method dispatching and try to understand the potential impact of this new language feature on future codebases.

---

To understand the significance of direct methods, you need to know a few things about the Objective-C runtime. But let’s start our discussion one step before that, to the origin of OOP itself:

## Object-Oriented Programming

Alan Kay coined the term “object-oriented programming in the late 1960s. With the help of Adele Goldberg, Dan Ingalls, and his other colleagues at Xerox PARC, Kay put this idea into practice in the ’70s with the creation of the Smalltalk programming language.

In the 1980s, Brad Cox and Tom Love started work the first version of Objective-C, a language that sought to take the object-oriented paradigm of Smalltalk and implement it on solid fundamentals of C. Through a series of fortuitous events in the ’90s, the language would come to be the official language of NeXT, and later, Apple.

For those of us who started learning Objective-C in the iPhone era, the language was often seen as yet another proprietary Apple technology — one of a myriad, obscure byproducts of the company’s [“Not invented here”](https://en.wikipedia.org/wiki/Not_invented_here) (NIH) culture. However, Objective-C isn’t just “an object-oriented C”, it’s one of _the original_ object-oriented languages, with as strong a claim to OOP credentials as any other.

Now, what does OOP mean? That’s a good question. ’90s era hype cycles have rendered the term almost meaningless. However, for our purposes today, let’s focus on something Alan Kay wrote in 1998:

> I’m sorry that I long ago coined the term “objects” for this topic because it gets many people to focus on the lesser idea. The big idea is “messaging” […] \> [Alan Kay](https://wiki.c2.com/?AlanKayOnMessaging)

## Dynamic Dispatch and the Objective-C Runtime

In Objective-C, a program consists of a collection of objects that interact with each other by passing messages that, in turn, invoke methods, or functions. This act of message passing is denoted by square bracket syntax:

```
[someObject aMethod:withAnArgument];
```

When Objective-C code is compiled, message sends are transformed into calls to a function called [`objc_msgSend`](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) (literally _“send a message to some object with an argument”_).

```
objc_msgSend(object, @selector(message), withAnArgument);
```

- The first argument is the receiver (`self` for instance methods)
- The second argument is `_cmd`: the selector, or name of the method
- Any method parameters are passed as additional function arguments

`objc_msgSend` is responsible for determining which underlying implementation to call in response to this message, a process known as method dispatch.

In Objective-C, each class (`Class`) maintains a dispatch table to resolve messages sent at runtime. Each entry in the dispatch table is a method (`Method`) that keys a selector (`SEL`) to a corresponding implementation (`IMP`), which is a pointer to a C function. When an object receives a message, it consults the dispatch table of its class. If it can find an implementation for the selector, the associated function is called. Otherwise, the object consults the dispatch table of its superclass. This continues up the inheritance chain until a match is found or the root class (`NSObject`) deems the selector to be unrecognized.

If you think all of this indirection sounds like a lot of work… in a way, you’d be right!

If you have a hot path in your code, an expensive method that’s called frequently, you could imagine some benefit to avoiding all of this indirection. To that end, some developers have used C functions as a way around dynamic dispatch.

## Direct Dispatch with a C Function

As we saw with `objc_msgSend`, any method invocation can be represented by an equivalent function by passing implicit `self` as the first argument.

For example, consider the following declaration of an Objective-C class with a conventional, dynamically-dispatched method.

```
@interface MyClass: NSObject
- (void)dynamicMethod;
@end
```

If a developer wanted to implement some functionality on `MyClass` without going through the whole message sending shebang, they could declare a static C function that took an instance of `MyClass` as an argument.

```
static void directFunction(MyClass *__unsafe_unretained object);
```

Here’s how each of these approaches translates to the call site:

```
MyClass *object = [[[MyClass] alloc] init];

// Dynamic Dispatch
[object dynamicMethod];

// Direct Dispatch
directFunction(object);
```

## Direct Methods

A direct method has the look and feel of a conventional method, but has the behavior of a C function. When a direct method is called, it directly calls its underlying implementation rather than going through `objc_msgSend`.

With this new LLVM patch, you now have a way to annotate Objective-C methods to avoid participation in dynamic dispatch selectively.

### objc_direct, @property(direct), and objc_direct_members

To make an instance or class method direct, you can mark it with the `objc_direct` [Clang attribute](https://nshipster.com/__attribute__/). Likewise, the methods for an Objective-C property can be made direct by declaring it with the `direct` property attribute.

```
@interface MyClass: NSObject
@property(nonatomic) BOOL dynamicProperty;
@property(nonatomic, direct) BOOL directProperty;

- (void)dynamicMethod;
- (void)directMethod __attribute__((objc_direct));
@end
```

When an `@interface` for a category or class extension is annotated with the `objc_direct_members` attribute, all method and property declarations contained within it are considered to be direct, unless previously declared by that class.

```
__attribute__((objc_direct_members))
@interface MyClass ()
@property (nonatomic) BOOL directExtensionProperty;
- (void)directExtensionMethod;
@end
```

Annotating an `@implementation` with `objc_direct_members` has a similar effect, causing non-previously declared members to be deemed direct, including any implicit methods resulting from property synthesis.

```
__attribute__((objc_direct_members))
@implementation MyClass
- (BOOL)directProperty {…}
- (void)dynamicMethod {…}
- (void)directMethod {…}
- (void)directExtensionMethod {…}
- (void)directImplementationMethod {…}
@end
```

Applying these annotations to our example from before, we can see how direct and dynamic methods are indistinguishable at the call site:

```
MyClass *object = [[[MyClass] alloc] init];

// Dynamic Dispatch
[object dynamicMethod];

// Direct Dispatch
[object directMethod];
```

---

Direct methods seem like a slam dunk feature for the performance-minded developers among us. But here’s the twist:

**In most cases, making a method direct probably won’t have a noticeable performance advantage.**

As it turns out, [`objc_msgSend` is surprisingly fast](https://www.mikeash.com/pyblog/friday-qa-2016-04-15-performance-comparisons-of-common-operations-2016-edition.html). Thanks to aggressive caching, extensive low-level optimization, and intrinsic performance characteristics of modern processors, `objc_msgSend` has an extremely low overhead.

We’re long past the days when iPhone hardware could reasonably be described as a resource-constrained environment. So unless Apple is preparing for a new embedded platform _([AR glasses, anyone?](http://appleinsider.com/articles/17/01/09/rumor-apple-working-with-carl-zeiss-on-ar-glasses-to-debut-in-2018))_, the most reasonable explanation we have for Apple implementing Objective-C direct methods in 2019 stems from something other than performance.

## Hidden Motives

When an Objective-C method is marked as direct, its implementation has hidden visibility. That is, direct methods can only be called within the same module _(or to be pedantic, [linkage unit](https://clang.llvm.org/docs/LTOVisibility.html))._ It won’t even show up in the Objective-C runtime.

Hidden visibility has two direct advantages:

- Smaller binary size
- No external invocation

Without external visibility or a way to invoke them dynamically from the Objective-C runtime, direct methods are effectively private methods.

While hidden visibility can be used by Apple to prevent swizzling and private API use, that doesn’t seem to be the primary motivation.

[According to Pierre](https://twitter.com/pedantcoder/status/1197269246289444864), who implemented this feature, the main benefit of this optimization is code size reduction. Reportedly, the weight of unused Objective-C metadata can account for 5 – 10% of the `__text` section in the compiled binary.

---

You could imagine that, from now until next year’s developer conference, a few engineers could go through each of the SDK frameworks, annotating private methods with `objc_direct` and private classes with `objc_direct_members` as a lightweight way to progressively tighten its SDK.

If that’s true, then perhaps it’s just as well that we’ve become skeptical of new Objective-C features. When they’re not in service of Swift, they’re in service of Apple. Despite its important place in the history of programming and Apple itself, it’s hard not to see Objective-C as just that — _history_.
