---
title: 'The weirdest subclass I''ve ever written | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/protocols-versus-subclasses.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:ed9e107d57090116'
translated: false
---

> 原文：[The weirdest subclass I've ever written | Cocoa with Love](https://www.cocoawithlove.com/blog/protocols-versus-subclasses.html)　·　Cocoa with Love (Matt Gallagher)

Object-oriented programming is losing popularity and some newer programming languages like Go and Rust don’t offer subclassing at all. In Swift, there’s a push for “protocol-oriented programming” where shared interfaces, default behaviors and substitutability are achieved through protocols rather than subclasses.

We should limit our use of subclasses to when we interoperate with Objective-C or we need to inherit both data members and behavior from another class, right?

Right?

## Object-oriented programming

I’m sure I don’t need to explain object-oriented programming but I do want to look at how the object-oriented hierarchies that used to dominate programming are being reconsidered and replaced by hierarchies that are dramatically shallower, with much of the functionality moved from classes into protocols.

```swift
protocol NSObjectProtocol { /* ... */ }
open class NSObject: NSObjectProtocol { /* ... */ }
open class NSResponder: NSObject { /* ... */ }
open class NSView: NSResponder { /* ... */ }
open class NSControl: NSView { /* ... */ }
open class NSButton: NSControl { /* ... */ }
```

In the above inheritance chain from AppKit, an `NSButton` “is a” kind of `NSView` (inheritance is often described as “is a” composition, versus “has a” composition or “conforms to” implementations). `NSButton`’s relationship with `NSView` could be argued as a clear case of traditional subclassing: we can use an `NSButton` anywhere an `NSView` is needed, the button shares all of the data from `NSView` and the button inherits the same interface and behaviors.

But the inheritance chain includes more than just `NSButton` or `NSView`.

`NSObject` is a default implementation for `NSObjectProtocol` but if Objective-C had default protocol implementations, you’d probably be able to replace the entire `NSObject` class with an allocator function.

`NSView` and `NSResponder` are really orthogonal concepts – display behavior and event behavior – so it’s not clear that an `NSView` is a kind of `NSResponder`. More importantly, _any_ object (not just those with `NSResponder` in their inheritance chain) should be able to perform responder chain behaviors, merely by conforming to the interface and inserting itself into the chain.

`NSControl` is a harder to call good or bad; it provides a grab-bag of interaction and data behaviors, as well extending of some `NSResponder` behaviors. In some ways inheriting from `NSControl` _does_ provide a good point for code reuse between subclasses – so there’s an argument that it might be fine as a subclass – but its role as an abstract class in the middle of an inheritance chain (you never instantiate `NSControl` directly) implies that it might work better as a protocol with an associated type for target/action and state storage – possibly broken into separate smaller protocols for different _kinds_ of control.

## Protocol-oriented programming

In Swift, a number of interfaces that would previously have been written as classes in Objective-C can instead be protocols. Since protocols aren’t single-inheritance, they’re easier to mix together in a range of different ways. Protocols work with Swift value types and classes equally, and protocols let us more narrowly specify input requirements rather than relying on dynamic behaviors.

The Apple WWDC 2015 video “[Protocol Oriented Programming in Swift](https://developer.apple.com/videos/play/wwdc2015/408/)” provided a great introduction to this topic and how it is distinct from object-oriented programming.

Swift didn’t invent this style of programming; a number of recent languages, including Rust and Go, have no subclassing and rely largely on “traits” and “interfaces” (equivalents to Swift protocols in those languages) for code reuse and polymorphism. Functional languages have used “type classes” to similar effect for decades.

A crude reorganizing of the `NSButton` hierarchy, following the broad rules I’ve discussed so far, might give a hierarchy that looked more like this:

```swift
protocol NSObjectProtocol { /* ... */ }
protocol NSResponder { /* ... */ }
protocol NSControl { /* ... */ }
protocol NSTwoStateControl: NSControl { /* ... */ }
open class NSView: NSObjectProtocol, NSResponder { /* ... */ }
open class NSButton: NSView, NSTwoStateControl { /* ... */ }
```

With no need for `NSObject` at all (it’s implemented as the default behavior for `NSObjectProtocol`), `NSResponder` and `NSControl` become protocols with `NSControl` further broken down into a number of simpler protocols (since greater functionality can now be easily achieved through intermixing).

In summary, protocols are more flexible and easier to intermix. They are also better suited to specifying constraints (which I haven’t discussed in this article) and they can be used with value types (which I also haven’t discussed).

With protocols being so flexible and capable, we should limit subclassing to when one class:

1. of a base class’s behavior, AND,
2. of a base class’s data layout

## The weirdest subclass I’ve ever written

Let’s imagine I have two classes. For argument’s sake, [let’s call them `Signal` and `SignalMulti`](https://github.com/mattgallagher/CwlSignal/blob/master/Sources/CwlSignal/CwlSignal.swift?ts=3).

The `Signal` class has a few different responsibilities and among them is a public function named `subscribe`. The `SignalMulti` class is _only_ a `subscribe` implementation (no other responsibilities) but the implementation is completely different (it allocates an entirely new instance of `Signal` internally and delegates the subscribe work to that instance instead).

These two classes share a single function interface, with no common implementation and don’t need any common data members or layout (technically, `SignalMulti` uses the `preceeding` member but it could easily declare that for itself). They are otherwise completely different.

Revisiting the two bullet points from the previous section:

1. does not want to share

  of the base class’s behavior
2. doesn’t need

  of the base class’s data layout

Despite this, I still implemented `SignalMulti` as a subclass of `Signal`, in violation of every common guideline about interfaces in Swift.

## Why use a subclass when a protocol is the obvious choice?

I’m not a big fan of object oriented design – the only other place I’ve used it in my Swift code on this blog is for wholly _private_ classes – so why have I broken the common guidelines and used a subclass here?

Let’s look at the effective shared interface between the two classes (I’m simplifying by omitting the `attach` function on the real classes):

```swift
public class Signal<T> {
   public func subscribe(context: Exec, handler: @escaping (Result<T>) -> Void) ->
      SignalOutput<T>
}

public class SignalMulti<T>: Signal<T> {
   public override func subscribe(context: Exec, handler: @escaping (Result<T>) -> Void) ->
      SignalOutput<T>
}
```

### Associated types require generic constraints which are clumsy

If we implemented `Signal` as a protocol it would need to have an `associatedtype` to capture the value type `T`. This associated type would mean that the protocol could be used only as a type constraint and every scope that operates on `Signal`s will also need to be generic.

For example, instead of a simple looking function like this:

```swift
class MyClass {
   public func receiveSignal(signal: Signal<Int>)
}
```

you would need to use:

```swift
class MyClass {
   public func receiveSignal<S>(signal: S) where S: Signal, S.ValueType == Int
}
```

Now the function is generic, which makes it a bit more confusing and technical to write (due to the need to constrain the generic parameter), could bloat code size if it is specialized and if it can’t be specialized may end up significantly slower.

### Implementations are less substitutable than protocols

Another topic which I feel is often left out of discussions about protocol oriented design – is the concept of [substitutability](https://en.wikipedia.org/wiki/Liskov_substitution_principle).

The substitutability I want is that you should _always_ be able to pass a `SignalMulti` where a `Signal` is requested but if a `SignalMulti` is requested, only a `SignalMulti` will suffice.

Technically, you could define a `Signal` protocol and a `SignalMulti` protocol that derives from it and capture this substitutability scenario. Protocols are theoretically capable of the same substitutability as classes.

However, the associated type that caused problems in the previous section causes problems here again: we must make `public` all implementations of our protocols. This creates a situation where we wouldn’t just have:

- `protocol Signal { assocatedtype ValueType }`
- `protocol SignalMulti: Signal`

but we’d also need to have:

- `class SignalImplementation<ValueType>: Signal`
- `class SignalMultiImpementation<ValueType>: SignalMulti`

and annoyingly, most user code will have instances of the latter two, not the former two. This – combined with the previous “generic constraints are clumsy” point – creates a situation where you’re likely to declare functions taking `SignalImplementation`, a declaration which _cannot_ accept a `SignalMulti`.

When we use `protocol`s with associated types, we’re forced to expose implementations that are less substitutable than the `protocol`s and likely to cause problems.

### Sealed behaviors

Since the `Signal` protocol needs to be public, _anything_ could implement the protocol. While this might seem great – all kinds of different classes could expose a `subscribe` function – the `Signal` classes are highly interconnected and dependent on lots of subtle behaviors to ensure thread safety and graph behavior propagation. This is a case where I really wanted the set of possible behaviors _sealed_ so that rules are _strictly_ obeyed.

You can’t make a `public` protocol sealed. Meanwhile, `public` classes _are_ sealed (they’re only subclass-able if they’re `open`).

## Conclusion

Protocol oriented programming is good – watch the “[Protocol Oriented Programming in Swift](https://developer.apple.com/videos/play/wwdc2015/408/)” video and use protocols where appropriate – but don’t forget that subclassing and inheritance retain some unique strengths in Swift.

I initially gave the following bullet points and claimed that you should favor a subclass over a protocol only if both of the following two points are true for the subclass:

1. of a base class’s behavior, AND,
2. of a base class’s data layout

The reality is that these bullet points don’t cover the whole range of considerations.

There are numerous syntactic differences around each and – since protocols and subclasses overlap significantly in the problems that they _can_ solve – you can validly choose between subclassing and protocols for a range of different syntactic reasons rather than a strict design rule.

Subclasses manage a specific substitutability arrangement that protocols can’t precisely model. Generic subclasses have better syntax than do protocols with associated types.

Finally, if you’re obsessive about controlling your interface, sometimes a little _less_ flexibility may be what you want: the `public` versus `open` distinction and the `final` keyword, make classes easier to tightly control, compared to protocols.
