---
title: 'ARC in Swift: Basics and beyond'
session_id: 10216
collection: wwdc2021
year: 2021
duration: '20:42'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10216/'
content_hash: 'sha256:34930f3f5251d0ae'
translated: false
---

# ARC in Swift: Basics and beyond

<sub>WWDC2021 · 20:42 · Swift</sub>

Learn about the basics of object lifetimes and ARC in Swift. Dive deep into what language features make object lifetimes observable,...

> [!note] 归档理由
> ARC 的插入规则、生命周期与 withExtendedLifetime，内存管理核心

## Resources

- [ARC - The Swift Programming Language](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10216/4/884C234F-2424-47DF-A4CF-A9010D869C66/downloads/wwdc2021-10216_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10216/4/884C234F-2424-47DF-A4CF-A9010D869C66/downloads/wwdc2021-10216_sd.mp4?dl=1)
- [ARC Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=109)
- [Reference Cycle Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=397)
- [Weak Reference Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=545)
- [Accessing an object via weak reference](https://developer.apple.com/videos/play/wwdc2021/10216/?time=605)
- [Accessing an object via optional binding of weak reference](https://developer.apple.com/videos/play/wwdc2021/10216/?time=674)
- [Safe techniques for handling weak references - withExtendedLifetime()](https://developer.apple.com/videos/play/wwdc2021/10216/?time=705)
- [Safe techniques for handling weak references - Redesign to access via strong reference](https://developer.apple.com/videos/play/wwdc2021/10216/?time=775)
- [Safe techniques for handling weak references - Redesign to avoid weak/unowned reference](https://developer.apple.com/videos/play/wwdc2021/10216/?time=860)
- [Deinitializer Example](https://developer.apple.com/videos/play/wwdc2021/10216/?time=923)
- [Sequencing deinitializer side-effects with external program effects](https://developer.apple.com/videos/play/wwdc2021/10216/?time=970)
- [Safe techniques for handing deinitalizer side effects - withExtendedLifetime()](https://developer.apple.com/videos/play/wwdc2021/10216/?time=1076)
- [Safe techniques for handing deinitalizer side effects - Redesign to limit visibility of internal class details](https://developer.apple.com/videos/play/wwdc2021/10216/?time=1111)
- [Safe techniques for handling deinitalizer side effects - Redesign to avoid deinitializer side-effects](https://developer.apple.com/videos/play/wwdc2021/10216/?time=1148)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ Bass music playing ♪ ♪ Meghana Gupta: Hi, my name is Meghana.

Today, I'll be talking to you about ARC in Swift.

Swift provides powerful value types like structs and enums.

You should prefer to use value types when possible to avoid the dangers of unintended sharing that comes with reference types.

Classes are reference types in Swift, and if you decide to use them, Swift manages its memory via Automatic Reference Counting, or ARC.

In order to write effective Swift, it is important to understand how ARC works.

In this session, we’ll do just that.

I’ll start with a review of object lifetimes and ARC in Swift.

Then, I’ll describe what observable object lifetimes are.

I'll explain in detail what language features make object lifetimes observable, consequences of relying on observed object lifetimes, and some safe techniques to fix them.

Let’s begin.

An object’s lifetime in Swift begins at initialization and ends at last use.

ARC automatically manages memory, by deallocating an object after its lifetime ends.

It determines an object’s lifetime by keeping track of its reference counts.

ARC is mainly driven by the Swift compiler which inserts retain and release operations.

At runtime, retain increments the reference count and release decrements it.

When the reference count drops to zero, the object will be deallocated.

Let’s see how it works with an example.

Imagine we want to build a travel app.

To represent a traveler, let’s write a class with name and an optional destination property.

In the test() function, first, a Traveler object is created, then its reference is copied, and finally, its destination is updated.

In order to automatically manage the memory of the Traveler object, the Swift compiler inserts a retain operation when a reference begins and a release operation after the last use of the reference.

traveler1 is the first reference to the Traveler object, and its last use is the copy.

Here, the Swift compiler inserts a release operation immediately after the last use of the traveler1 reference.

It does not insert a retain operation when the reference begins, because initialization sets the reference count to one.

traveler2 is another reference to the Traveler object, and its last use is the destination update.

Here, the Swift compiler inserts a retain operation when the reference begins and a release operation immediately after the last use of the reference.

Let's step through the code and see what happens at runtime.

First, the Traveler object is created on the heap and initialized with a reference count of one.

Then in preparation of the new reference, retain operation executes, incrementing the reference count to two.

Now traveler2 is also a reference to the Traveler object.

After the last use of the traveler1 reference, the release operation executes, decrementing the reference count to one.

Then the destination of the Traveler object is updated to Big Sur.

Since that was the last use of the traveler2 reference, release operation executes, decrementing the reference count to zero.

Once the reference count drops to zero, the object can be deallocated.

Object lifetimes in Swift are use-based.

An object's guaranteed minimum lifetime begins at initialization and ends at last use.

This is different from languages like C++, in which an object’s lifetime is guaranteed to end at the closing brace.

In this example, we saw the object was deallocated immediately after the last use.

However, in practice, object lifetimes are determined by the retain and release operations inserted by the Swift compiler.

And depending on the ARC optimizations that kick in, the observed object lifetimes may differ from their guaranteed minimum, ending beyond the last use of the object.

In such cases, the object is deallocated at a program point beyond its last use.

In most cases, it doesn’t really matter what the exact lifetime of an object is.

However, with language features like weak and unowned references and deinitializer side effects, it is possible to observe object lifetimes.

And if you have programs that rely on observed object lifetimes instead of guaranteed object lifetimes, you can end up with problems in the future.

Because relying on observed object lifetimes may work today, but it is only a coincidence.

Observed object lifetimes are an emergent property of the Swift compiler and can change as implementation details change.

Such bugs may not be discovered during development and may remain hidden for a long time, only to be uncovered by a compiler update with improved ARC optimizations or unrelated source changes that enable a previously limited ARC optimization.

I’ll go over the language features that make object lifetimes observable, walk through what can happen if we rely only on observed object lifetimes, and some safe techniques to fix them.

Unlike default references that are strong references, weak and unowned references do not participate in reference counting, and for this reason, they are commonly used to break reference cycles.

Before I get into their details, let’s see what reference cycles are.

This is an extension of our Travel app.

We now want to introduce an optional points system.

A traveler can have an account and accumulate points in it.

To represent this, we have a new Account class with points property.

The Account class refers to the Traveler class, and the Traveler class refers back to the Account class.

In the test() function, we create Traveler and Account objects, and then call the printSummary() function via the traveler reference.

Let’s step through the code and see what happens with ARC.

First, Traveler object is created on the heap with a reference count of one.

Then Account object is created on the heap with a reference count of one.

Since the Account object refers to the Traveler object, the reference count of the Traveler object is incremented to two.

Now the Traveler object starts referring to the Account object, so the reference count of the Account object is also incremented to two.

This is the last use of the account reference.

After this, the account reference goes away and reference count of the Account object is decremented to one.

Then, printSummary() function is called to print name and points.

This is the last use of the Traveler reference.

After this, the Traveler reference goes away and the reference count of the Traveler object is decremented to one.

Even after all the references that make the objects reachable go away, the reference count of the objects remain one.

This is because of the reference cycle.

As a result, the objects are never deallocated, causing a memory leak.

You may break the reference cycle with a weak or unowned reference.

Because they don’t participate in reference counting, the referred object may be deallocated while a weak or unowned reference is in use.

When this happens, the Swift runtime safely turns access to weak references as nil, and access to unowned references as traps.

Any reference participating in the reference cycle can be marked as weak or unowned to break the reference cycle.

It depends on the application.

In our example, let’s mark the traveler reference in the Account class as weak.

Because weak reference does not participate in reference counting, after the last use of the Traveler object, its reference count drops to zero.

Once the reference count of the Traveler object is zero, it can be deallocated.

When the Traveler object goes away, its reference to the Account object goes away, making its reference count zero.

Now the Account object can be deallocated.

In this example, we used the weak reference to only break the reference cycle.

If a weak reference is used to access an object while its guaranteed object lifetime has ended, and you are relying on observed object lifetime for the object to be available, you can end up with bugs in the future when the observed object lifetime changes for unrelated reasons.

Let’s see an example.

Here, the printSummary() function is moved from the Traveler class to the Account class.

And the test() function now calls the printSummary() function via the Account reference.

What exactly happens when printSummary() function is called? It may print the traveler’s name and points today, but this is only a coincidence.

This is because the last use of the Traveler object is before the call to the printSummary() function.

After this, the reference count of the Traveler object can drop to zero if the compiler inserted a release immediately after the last use.

If the reference count has dropped to zero, access to the Traveler object via the weak reference will be nil, and the Traveler object may be deallocated.

So when the printSummary() function is called, the force unwrap of the weak Traveler reference will trap, causing a crash.

You may be wondering if the force unwrap is the reason for the crash here, and optional binding may have prevented it.

Optional binding actually worsens the problem.

Without an obvious crash, it creates a silent bug that may go unnoticed when the observed object lifetime changes for unrelated reasons.

There are different techniques to safely handle weak and unowned references, each of them with varying degrees of upfront implementation cost versus continuous maintenance cost.

Let’s explore them one by one with our example.

Swift provides withExtendedLifetime() utility that can explicitly extend the lifetime of an object.

Using withExtendedLifetime(), it is possible to safely extend the lifetime of the Traveler object, while the printSummary() function is being called, preventing potential bugs.

The same effect can be achieved by placing an empty call to withExtendedLifetime() at the end of the existing scope.

For more complex cases, we can ask the compiler to extend the lifetime of an object to the end of the current scope using defer.

withExtendedLifetime() may look like an easy way out of object lifetimes bugs.

However, this technique is fragile, and transfers the responsibility of correctness on you.

With this approach, you should ensure withExtendedLifetime() is used every time a weak reference has a potential to cause bugs.

If not controlled, withExtendedLifetime() can creep up all over the codebase, increasing maintenance cost.

Redesigning classes with better APIs is a much more principled approach.

Object lifetime surprises can be prevented, if access to the object can be limited to strong references only.

Here, the printSummary() function is moved back to the Traveler class, and the weak reference in Account class is hidden.

Tests are now forced to call the printSummary() function via a strong reference, eliminating potential bugs.

In addition to carrying a performance cost, weak and unowned references can expose bugs if you are not careful with class design.

It is important to pause and think, why are weak and unowned references needed? Are they used only to break reference cycles? What if you avoid creating reference cycles in the first place? Reference cycles can often be avoided by rethinking algorithms and transforming cyclic class relationships to tree structures.

In our example, Traveler class needs to refer to the Account class.

It is not really necessary for the Account class to refer to the Traveler class.

Account class only needs access to the traveler’s personal information.

We can move the traveler’s personal information into a new class called PersonalInfo.

Both Traveler class and Account class can refer to the PersonalInfo class, avoiding the cycle.

Avoiding the need for weak and unowned references may have additional implementation cost, but this is a definite way to eliminate all potential object lifetime bugs.

Another language feature that makes object lifetimes observable are deinitializer side effects.

A deinitializer runs before deallocation and its side effects can be observed by external program effects.

If you write code to sequence deinitializer side effects with external program effects, it can lead to hidden bugs, which are uncovered only when the observed object lifetime changes due to unrelated reasons.

Before I get into how such bugs can come up, let’s see what a deinitializer is.

This is a repeat of the first example, now with a deinitializer.

The deinitializer has a global side effect: printing a message on the console.

Today the deinitializer may run after "Done traveling" is printed.

But since the last use of the Traveler object is the destination update, the deinitializer can run before "Done traveling" is printed, depending on the ARC optimizations that kick in.

In this example, deinitializer side effects were observable but not relied upon.

Let’s look at a more complex example, where deinitializer side effects are relied upon by external program effects.

We now introduce travel metrics to the Traveler class.

Whenever a destination is updated, it is recorded in the TravelMetrics class.

Eventually when deinitializing the Traveler object, metrics get published to a global record.

Metrics published are the traveler’s anonymous ID, number of destinations looked up, and a computed travel interest category.

In the test() function, first, a Traveler object is created, then reference to the travelMetrics is copied from the Traveler object.

The traveler’s destination is updated to Big Sur, which records Big Sur in TravelMetrics.

The traveler’s destination is updated to Catalina, which records Catalina in TravelMetrics.

Then the travel interest category is computed by looking at the recorded destinations.

Today the deinitializer may run after computing travel interest, publishing the interested category as Nature.

But the last use of the Traveler object is the destination update to Catalina, immediately after which the deinitializer can run.

Since the deinitializer runs before computing the travel interest, nil gets published, causing a bug.

Just like weak and unowned references, there are different techniques to safely handle deinitializer side effects.

Each of them with varying degrees of upfront implementation cost versus continuous maintenance cost.

Let’s look at them one by one.

withExtendedLifetime() can be used to explicitly extend the lifetime of the Traveler object until the travel interest category is computed, preventing potential bugs.

As discussed before, this transfers responsibility of correctness on you.

With this approach, you should ensure withExtendedLifetime is used every time there is a potential of incorrect interaction between deinitializer side effects and external program effects, increasing maintenance cost.

Deinitializer side effects cannot be observed if the effects are all local.

Redesigning class API by limiting the visibility of internal class details can prevent object lifetime bugs.

Here, TravelMetrics is marked private, hiding it from external access.

The deinitializer now computes the most interested travel category and publishes the metrics.

This works, but a more principled approach is to get rid of the deinitializer side effects altogether.

Here, defer is used instead of the deinitializer to publish metrics, and the deinitializer only performs verification.

By removing deinitializer side effects, we can eliminate all potential object lifetime bugs.

We explored our educational Travel app example to learn about ARC, weak and unowned references, and deinitializer side effects.

It is important to thoroughly understand the language features that make object lifetimes observable and eliminate potentially incorrect reliance on observed object lifetimes, so that we don’t uncover bugs at surprising times.

With Xcode 13, a new experimental build setting called "Optimize Object Lifetimes" is available for the Swift compiler.

This enables powerful lifetime shortening ARC optimizations.

With this build setting turned on, you may see objects being deallocated immediately after last use much more consistently, bringing observed object lifetimes closer to their guaranteed minimum.

This may expose hidden object lifetime bugs, similar to the examples discussed.

You can follow the safe techniques discussed in this session to eliminate all such bugs.

I hope you enjoyed this session.

Thanks for watching.

♪
