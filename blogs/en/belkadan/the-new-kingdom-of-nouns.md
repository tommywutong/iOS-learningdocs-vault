---
title: The New Kingdom of Nouns
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/'
original_language: en
published: 2017-09-07
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0163f942bfb236b1'
translated: false
---

> 原文：[The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Over-abstraction](https://belkadan.com/blog/2017/09/Over-abstraction/)

[Color Palette #8](https://belkadan.com/blog/2018/01/Color-Palette-8/) »

« [Over-abstraction](https://belkadan.com/blog/2017/09/Over-abstraction/?tag=functional-programming)

« [Over-abstraction](https://belkadan.com/blog/2017/09/Over-abstraction/?tag=math)

[Many-to-Many Protocols](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/?tag=swift) »

« [Re: Contempt Culture](https://belkadan.com/blog/2015/12/Re-Contempt-Culture/?tag=programming-languages)

[Many-to-Many Protocols](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/?tag=programming-languages) »

## [The New Kingdom of Nouns](#)

[Last time](https://belkadan.com/blog/2017/09/Over-abstraction/) I talked about how algebraic abstractions like “monoid” and “semigroup” didn’t seem to be pulling their weight, despite love from functional programmers. That focused on a practical issue: do these abstractions aid or harm comprehension? Do they make programming easier or harder? (Of course, there’s not a simple answer to this question.)

This time, though, I want to talk about something more exploratory: do we have the right tools to _talk_ about these abstractions? This post is therefore going to be _much_ longer and contain a lot more rambling.

(I’ll note up front that these really are exploratory ideas, not something I’d intend to put into Swift directly. Things to consider for the _next_ language, perhaps, since [we’ll never find a programming language that frees us from the burden of clarifying ideas](https://www.xkcd.com/568/).)

---

Let’s start with something “simple”: the abstraction of a _semigroup._ This consists of a type and an operation, and the operation has to be [associative](https://simple.wikipedia.org/wiki/Associativity). If we were to write this as a Swift protocol, we could do something like this:

```
protocol Semigroup {
  // Binary semigroup operation
  // **AXIOM** Should be associative:
  //   a.op(b.op(c)) == (a.op(b)).op(c)
  func op(_ g: Self) -> Self
}
```

(from Brandon Williams’ “[Algebraic Structure and Protocols](http://www.fewbutripe.com/swift/math/algebra/2015/02/17/algebraic-structure-and-protocols.html)”)

Now, `Int` can certainly conform to this protocol:

```
extension Int: Semigroup {
  func op(_ b: Int) -> Int {
    return self + b
  }
}
```

This works great, because integer addition is associative.^[1](#fn:float) And as Brandon Kase mentions in his talk “[Beyond Types in Swift](http://2017.funswiftconf.com)”, this means it’s safe to use with a parallel implementation of `reduce`. This means I can get the sum of a collection of integers much faster than if I do a regular, serial `reduce`.

But wait, we could also have written it this way:

```
extension Int: Semigroup {
  func op(_ b: Int) -> Int {
    return self * b
  }
}
```

Integer multiplication is also associative, and getting the product of a collection of integers can also be a useful operation.

**It has always, _always_ bothered me that there are two ways for `Int` to be a semigroup.** Why do people act like `+` is obviously the “right” way to do it? And it’s even worse for `Bool`, where `||` and `&&` are much closer to being symmetric.

Haskell, as a language with a standard library and community that cares strongly about algebraic abstractions, [actually agrees with me here.](https://hackage.haskell.org/package/semigroups-0.18.1/docs/Data-Semigroup.html) Rather than make `Int` conform to `Semigroup`, they use simple wrapper structs (in Swift terms) called `Sum` and `Product`. In Swift, this would look something like this:

```
struct Sum<Wrapped: Arithmetic>: RawRepresentable {
  var rawValue: Wrapped
  init(rawValue: Wrapped) { … }
  init(_ rawValue: Wrapped) { … } // for convenience
}
extension Sum: Semigroup {
  func op(_ other: Sum<Wrapped>) -> Sum<Wrapped> {
    return Sum(self.rawValue + other.rawValue)
  }
}
```

(and similar for `Product`)

Pause.

---

Back in 2006, Steve Yegge wrote a blog post called “[Execution in the Kingdom of Nouns](http://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html)”. I hesitate a little to link to it because it probably qualifies as an instance of [Contempt Culture](https://belkadan.com/blog/2015/12/Re-Contempt-Culture/), but it does have some good points, and it relates to what I’m about to bring up, and without it I’d have to think of a different title for this blog post. But I’ll summarize it here for those who don’t want to read through Yegge’s parable about Java:

> Object-oriented languages, especially 2000s-era OO languages, especially 2000s-era Java, have a (natural) tendency to “make everything a noun”, i.e. to not have free functions or function values. Instead, you have to make a class that has a particular operation, and then make that a subclass of some known class (or implement an interface, Java’s equivalent of Swift’s protocols) so that the operation you want can be invoked via dynamic dispatch. This adds boilerplate to your code and obscures the fact that you _really_ just want to talk about an operation.
> 
> ```
> threadPool.execute(new Runnable() {
>   @Override public void run() { … }
> })
> ```

(As an addendum, Java 8 got some shorthand to handle these much more concisely, which they call [lambda expressions](http://www.drdobbs.com/jvm/lambda-expressions-in-java-8/240166764). The operation is still strongly typed on the declaration side, though, so people could reasonably still be unhappy.)

So, the problem in Java is (was) that **if you want to talk about an operation** (a verby thing like “add”), **you have to do it using a type** (a nouny thing like “BinaryOperation”, or its concrete implementation “Sum”). Swift is much better because it allows you to directly use functions as values, either by referencing them by name or by using closure expressions. Problem solved, right?

---

Last time I mentioned at the end of the post—snuck in, really—Dim Sum Thinking’s idea that **[algebraic abstractions act like “design patterns”](https://twitter.com/dimsumthinking/status/887498387293167618)**, in that the power came from the intuition and understanding that went with saying “this behaves like a semigroup” in the same way as “this behaves like a delegate”. Someone who’s been programming Cocoa for a while almost certainly knows what I mean when I say the latter (“weakly-referenced object that is consulted and/or informed about various things that happen to the main object”), and someone who’s familiar with algebraic abstractions knows what I mean about the former (“type with a combining binary operation that’s associative, so I can parallel-reduce it”). This is _useful_ for communication.

Only…there’s an idea (both longstanding and controversial) that [a design pattern compensates for a missing language feature](http://wiki.c2.com/?AreDesignPatternsMissingLanguageFeatures). The compiler can check (to some extent) if you’re using a language feature directly, and may provide special affordances to make it simpler and easier to get right. So, in that case, what language feature is missing?

---

At this point you might be wondering “what does this all have to do with `Sum` and `Product`?” Well, recall that I said that a useful thing about associative operations is that you can perform `reduce` in parallel. That means we’d define `parallelReduce` something like this:

```
extension RandomAccessCollection where Element: Semigroup {
  func parallelReduce(_ resultIfEmpty: Element) -> Element { … }
}
```

Notice that the extension is constrained: the element of the collection must be a `Semigroup`. This is a good thing; **we want the compiler to tell us if we try to `parallelReduce` with a non-associative operation**, like subtraction. **A design pattern can’t do this**; it’s “just” guidelines on how to write code. But using this protocol correctly with the rest of Swift becomes a bit unwieldy.

```
let questionScores: [Int] = …
// let totalScore: Int = questionScores.reduce(0, +)
let totalScore: Int =
    questionScores.lazy
                  .map { Sum($0) }
                  .parallelReduce(Sum(0))
                  .rawValue
```

That is, we have to jump in and out of the `Sum` type in order to talk about the summing operation.^[2](#fn:lazy)

We could get clever and throw more code at the problem:

```
extension RandomAccessCollection {
  func parallelReduce<Operation: Semigroup>(
    _ resultIfEmpty: Element,
    _ operation: Operation.Type) -> Element
  where Operation: RawRepresentable, Operation.RawValue == Element {
    return self.lazy
               .map { Operation(rawValue: $0) }
               .parallelReduce(Operation(rawValue: resultIfEmpty))
               .rawValue
  }
}

let questionScores: [Int] = …
// let totalScore: Int = questionScores.reduce(0, +)
let totalScore: Int = questionScores.parallelReduce(0, Sum.self)
```

But now, even though we’ve gotten down to something much closer to the original `reduce` code, we’re starting to see a familiar complaint. **In order to get the guarantee that `+` is associative, we had to _define a type._** We’re back in the Kingdom of Nouns.

---

I _think_ the trouble is that we don’t _really_ want to say “`Int` is a semigroup”, or even a more correct “`Int` forms a semigroup under addition” (or “with `+`”, if you want to sound less mathy). The natural way for _me_ to talk about these things is “`+` on `Int`s is associative”. And indeed, that’s what I _have_ been saying in the prose, throughout this whole post.

So, is that the missing language feature? Maybe we really want a way to describe the properties of _operations,_ specific values of function type.

```
// For illustrative purposes only.
operationgroup Semigroup<Element>: (Element, Element) -> Element

func +(left: Int, right: Int) -> Int: Semigroup { … }
func *(left: Int, right: Int) -> Int: Semigroup { … }
func -(left: Int, right: Int) -> Int { … }

extension RandomAccessCollection {
  func parallelReduce(
    _ resultIfEmpty: Element,
    _ combine: Semigroup<Element>) -> Element { … }
}

let questionScores: [Int] = …
// let totalScore: Int = questionScores.reduce(0, +)
let totalScore: Int = questionScores.parallelReduce(0, +) // ahhh...
```

There we go. Now we can continue referring to functions directly, but also the compiler can check if we screw up at the use site, and even do some basic checking to make sure the function’s type makes sense. I’m not exactly sure how it would works with closure literals, but let’s not worry about that right now.

(If you’re wondering why there isn’t a swift-evolution proposal about this right now, keep reading.)

This feels a lot better to me than what we had before. We don’t have to say a _data type_ has these particular properties. We don’t have to make a dummy type when there’s more than one way to satisfy the abstraction. We don’t even end up with the “generic operation” problem from the [previous post](https://belkadan.com/blog/2017/09/Over-abstraction/), because we use whatever names are natural for the operation.

(Okay, that last one is cheating, because now we have to pass the operation directly to `parallelReduce`, instead of inferring it from the element type. For `Semigroup` I think that’s the right tradeoff, but that might not always be the case. Keep reading.)

To summarize: **what this hypothetical syntax does is put the conformance into the _function_ type rather than the _data_ type.** It’s still “type checking”, and it’s still enforced by the compiler, so it’s more than just a design pattern, but at the same time it puts the abstraction in the right place.

…or does it?

---

After defining `Semigroup`—actually, the very first protocol covered—[Williams goes on to define `Monoid`](http://www.fewbutripe.com/swift/math/algebra/2015/02/17/algebraic-structure-and-protocols.html).

```
protocol Monoid: Semigroup {
  // Identity value of monoid
  // **AXIOM** Should satisfy:
  //   Self.e().op(a) == a.op(Self.e()) == a
  // for all values a
  static func e() -> Self
}
```

(I probably would have used a static property `identity` rather than a function, but whatever.)

The immediate advantage of a monoid is that you now have a good default for the `initialResult` parameter of `reduce` and the `resultIfEmpty` parameter of `parallelReduce`: the identity value.

```
extension Sequence where Element: Monoid {
  func reduce() -> Element {
    return self.reduce(.e(), { $0.op($1) })
  }
}
```

There’s an argument to be had over whether this is _sufficiently_ more expressive than `Semigroup` to be worth a separate protocol and another method on `Sequence`, but let’s set that aside. The problem we run into is that **the hypothetical `operationgroup` I came up with in the last section now has to grow actual members**.

```
operationgroup Semigroup<Element>: (Element, Element) -> Element {}
operationgroup Monoid<Element>: Semigroup<Element> {
  var identity: Element
}

func +(left: Int, right: Int) -> Int: Monoid {
  …
} where {
  var identity: Int { return 0 }
}
```

My makeshift syntax is getting uglier, and I have even less idea how it would work for closures at this point. Maybe this `operationgroup` thing isn’t going to fly.

---

This whole time I’ve been saying that the interesting part of a semigroup is the operation:

- It takes two values with the same type, and returns another value of that type.
- It’s associative. (This actually implies the previous condition, but let’s separate that just to be explicit.)

The way I’ve phrased the definition, the element type feels almost incidental, and therefore it makes sense to talk about the operation holding the “conformance”. But these aren’t the only kind of algebraic structures that show up in computer science. There’s another one called a _lattice_ that looks something like this:

```
protocol Lattice {
  // **AXIOM** Should satisfy:
  //   Commutativity: a.join(b) == b.join(a)
  //   Associativity: a.join(b).join(c) == a.join(b.join(c))
  //   Absorption:    a.join(a.meet(b)) == a
  //                  a.meet(a.join(b)) == a
  // for all values a, b, and c
  func join(_ other: Self) -> Self

  // **AXIOM** Should satisfy:
  //   Commutativity: a.meet(b) == b.meet(a)
  //   Associativity: a.meet(b).meet(c) == a.meet(b.meet(c))
  //   Absorption:    a.join(a.meet(b)) == a
  //                  a.meet(a.join(b)) == a
  // for all values a, b, and c
  func meet(_ other: Self) -> Self
}
```

A concrete example of a lattice is a `Set` with its `union` and `intersection` operations.^[3](#fn:refines)

```
struct SetInclusion<Element>: RawRepresentable {
  var rawValue: Set<Element>
  init(rawValue: Set<Element>) { … }
  init(_ rawValue: Set<Element>) { … } // for convenience
}
extension SetInclusion: Lattice {
  func join(_ other: SetInclusion<Element>) -> SetInclusion<Element> {
    return SetInclusion(self.rawValue.union(other.rawValue))
  }
  func meet(_ other: SetInclusion<Element>) -> SetInclusion<Element> {
    return SetInclusion(self.rawValue.intersection(other.rawValue))
  }
}
```

This is a death knell for the idea of `operationgroup`. Neither `join` nor `meet` is a “fundamental” operation that carries the “lattice-ness” of `SetInclusion`, and moreover their requirements both depend on the other operation!

The trouble is that **algebraic abstractions don’t constrain themselves to relating a single operation with a single type**; they can have multiple operations or even multiple types and still be useful. We could certainly decide that some _subset_ of abstractions deserves to be privileged with a language feature, but then we’ll have to make compromises when we go beyond that subset.

(In fact, you could say we’ve already done this: abstractions that really _do_ feel like they’re about one type in particular work very nicely as protocols, like `Sequence` and `RawRepresentable`.)

---

So, the missing language feature here, perhaps, is a way to relate _multiple_ types and _multiple_ operations, and refer to those relations directly. Surprise, there is in fact a language that does this: [ML](https://en.wikipedia.org/wiki/Standard_ML#Module_system)! ML’s equivalent of protocols is _signatures,_ but the things that conform to them aren’t the _datatypes_ (in Swift terms, enums with tuple payloads) but containers called _structures._ ML structures aren’t like Swift structs; they’re “just” relations between types and operations that satisfy signatures. In Swift syntax they’d look something like this:

```
structure SetInclusion<T>: Lattice {
  typealias Element = Set<T>
  func join(_ left: Set<T>, _ right: Set<T>) -> Set<T> {
    return left.union(right)
  }
  func meet(_ left: Set<T>, _ right: Set<T>) -> Set<T> {
    return left.intersection(right)
  }
}
```

(Disclaimer: I have never actually _written_ anything in ML; this is all accrued knowledge and surface-level research done in the process of writing this post, so I could very easily be getting things wrong.)

Let’s rewrite the example with the `Sum` struct in this way too.

```
structure Sum<T: Arithmetic>: Semigroup {
  typealias Element = T
  func op(_ left: T, _ right: T) -> T {
    return left + right
  }
}

extension RandomAccessCollection {
  func parallelReduce<Operation: Semigroup>(
    _ resultIfEmpty: Element,
    _ operation: Operation) -> Element
  where Operation.Element == Element {
    …
  }
}

let questionScores: [Int] = …
// let totalScore: Int = questionScores.reduce(0, +)
let totalScore: Int = questionScores.parallelReduce(0, Sum)
```

So, we’re in the Kingdom of Nouns again, but now we know why. **The noun isn’t the name of the operation; it’s the name of the relation between the type(s) and operation(s).** Curiously, math doesn’t usually give these relations nice, easy names, but that’s because a lot of them are ad hoc: `Sum` is “([ℤ](https://en.wikipedia.org/wiki/Integer), +)”, `SetInclusion` is “(_S,_ ∪, ∩)”, and so on. That wouldn’t be great for us programmers, where we may actually need to refer to the relation in multiple places.

(And if you haven’t spotted it already, surprise #2 is that you don’t _really_ need a new declaration kind to do this in Swift. The “structure” above is equivalent to the current idiom for sub-module “namespaces”: an enum with no cases.)

Some of the uneasiness here, at least for me, comes from the clash with normal object-oriented style. We have operations that operate on a particular type, and yet we don’t necessarily want to make them methods of that type. Instead, we’re mapping existing methods into a generic interface, and that generic interface may not have a good choice to be the `self` type.

On the other hand, being able to directly manipulate “structures” lets you do convenient things like having a `Set` that uniques class instances by pointer identity instead of calling `==`.^[4](#fn:conformance) Hm, this is starting to sound like the [strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)…

…and with that we’ve come full circle back to design patterns.

---

So, to conclude:

- Yes, being able to check properties of operations pulls us into the Kingdom of Nouns in today’s Swift.
- No, Swift cannot really do better in the general case, because it’s not always about just one operation.
- Yes, a `RawRepresentable` struct is the way to go when a type can conform to a protocol in multiple ways.

I think a possible takeaway from this for Swift is that defining such structs could be easier. There are a few ideas floating around about that, primarily a keyword like `newtype` that would handle the `RawRepresentable` conformance, and then some way to forward protocol implementations to the wrapped value. And possibly some automatic wrapping/unwrapping. But we’ll see.

Hope you’ve enjoyed this exploration of mine! Thanks for following along.

---

1. Fun fact: [addition of floating-point values is _not_ associative](https://en.wikipedia.org/wiki/Associative_property#Nonassociativity_of_floating_point_calculation). This isn’t important at all for this post, but it is one of the reasons why for a long time Swift didn’t have a common “Arithmetic” protocol that covers both integers and floating-point numbers: the straightforward implementation of a generic algorithm often doesn’t do the right thing for floats.

  Strictly speaking, integer addition is not associative in Swift either because `+` traps when you overflow: consider `.max + 1 + (-1)`. `&+` _is_ associative but doesn’t always behave like addition. I left this out of the original post because I literally forgot to consider adding negative numbers. [↩︎](#fnref:float)
2. The `.lazy` is there because we don’t _really_ care about the intermediate state of `Sum` values. Many other languages default to this behavior; Swift chose not to in order not to thrust types like `LazyMappedCollection` in new users’ faces when they really just wanted an Array back. One can argue over whether this was the right decision; I won’t address it further in this post. [↩︎](#fnref:lazy)
3. Why not make `Set` conform to `Lattice` directly? Turns out there’s another way that Sets can form a lattice: if you can do some kind of ordering on their elements. For example, a set of sets can form a “partition refinement lattice”, as illustrated in [this diagram from Wikipedia](https://en.wikipedia.org/wiki/Lattice_(order)#/media/File:Lattice_of_partitions_of_an_order_4_set.svg). But I think the union/intersection lattice is probably the one you’d see most often. [↩︎](#fnref:refines)
4. The Swift compiler actually _does_ reason directly about “structures”, calling them “conformances”. Just as an ML structure describes relations between types and operations that satisfy a signature, a Swift conformance describes how a particular type conforms to a protocol, including all of the operations and associated types. A conformance even has a run-time representation, which shows up as a hidden argument to a generic function. But the language doesn’t give you any ability to interact with conformances directly. [↩︎](#fnref:conformance)

This entry was posted on [September](https://belkadan.com/blog/2017/09) 07, [2017](https://belkadan.com/blog/2017) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Functional programming](https://belkadan.com/blog/tags/functional-programming), [Math](https://belkadan.com/blog/tags/math), [Swift](https://belkadan.com/blog/tags/swift), [Programming languages](https://belkadan.com/blog/tags/programming-languages)
