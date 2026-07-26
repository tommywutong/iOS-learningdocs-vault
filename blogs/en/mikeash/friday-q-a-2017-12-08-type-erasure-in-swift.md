---
title: 'Friday Q&A 2017-12-08: Type Erasure in Swift'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-12-08-type-erasure-in-swift.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f9890a953a28a028'
translated: false
---

> 原文：[Friday Q&A 2017-12-08: Type Erasure in Swift](https://www.mikeash.com/pyblog/friday-qa-2017-12-08-type-erasure-in-swift.html)　·　mikeash.com Friday Q&A

Posted at 2017-12-15 14:09 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2018-04-27: Generating Text With Markov Chains in Swift](https://www.mikeash.com/pyblog/friday-qa-2018-04-27-generating-text-with-markov-chains-in-swift.html)  
Previous article: [Friday Q&A 2017-11-10: Observing the A11's Heterogenous Cores](https://www.mikeash.com/pyblog/friday-qa-2017-11-10-observing-the-a11s-heterogenous-cores.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-12-08: Type Erasure in Swift

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Hungarian (translation by Szabolcs Csintalan)](http://fertlond.com/tipus-torles-a-swift/).

**Motivation**  
There are times when you want to hide an underlying type from outside users. Sometimes it's just a matter of hiding implementation details. In other cases, it can prevent a static type from spreading through the codebase, or allow distinct types to interoperate. Type erasure is the process of removing a specific type annotation in favor of a more general one.

Protocols or abstract superclasses could be considered a really simple form of type erasure. Take `NSString` as an example. You never get a plain `NSString` instance; it's always an instance of some concrete subclass, usually private. That is mostly hidden from view, though, and the APIs all work with `NSString`. All of the various subclasses can be used without having to know what they are, and without having to sprinkle your code with their types.

More advanced techniques become useful when dealing with Swift's generics and protocols with associated types. Swift doesn't allow using such protocols as concrete types. For example, if you want to write some code that accepts any `Sequence` of `Int` values, you can't write this:

```
    func f(seq: Sequence<Int>) { ...
```

That's not legal Swift. You can specialize generic types that way, but not protocols. You can work around this using generics:

```
    func f<S: Sequence>(seq: S) where S.Element == Int { ...
```

Sometimes this works great, but there are cases where it can be troublesome. Often you can't just add generics in one spot: one generic function requires others to be generic which require yet more.... Even worse, you can't use this for return values or properties at all. This won't work the way you want it to at all:

```
    func g<S: Sequence>() -> S where S.Element == Int { ...
```

We're looking for something where `g` can return any conforming type, but instead this allows the _caller_ to choose which type it wants, and `g` is then required to provide an appropriate value.

Swift provides the `AnySequence` type to solve this problem. `AnySequence` wraps an arbitrary `Sequence` and erases its type, providing access to it through the `AnySequence` type instead. Using this, we can rewrite `f` and `g`:

```
    func f(seq: AnySequence<Int>) { ...

    func g() -> AnySequence<Int> { ...
```

The generics disappear and all the specific types are still hidden. There's a small code complexity and runtime cost from having to wrap the values in `AnySequence`, but the code is nice and clean.

The Swift standard library has a bunch of these `Any` types, such as `AnyCollection`, `AnyHashable`, and `AnyIndex`. It can be useful to create your own to go along with your own generics and protocols, or just use the techniques to simplify your code when dealing with them. Let's explore the various ways to accomplish type erasure.

**Type Erasure With Classes**  
We need to wrap up some common functionality from multiple types without exposing those types. This sounds a lot like a superclass-subclass relationship, and in fact we can use subclasses to implement type erasure. The superclass can expose an API that's blind to the underlying implementation type, and a subclass can implement that API with knowledge of the underlying type.

Let's see how our own version of `AnySequence` would look using this technique. I'll call it `MAnySequence` to incorporate my name:

```
    class MAnySequence<Element>: Sequence {
```

This class is also going to need an iterator type that it can return from the `makeIterator` method. We have to perform type erasure twice so that we can hide the underlying `Sequence` type as well as its `Iterator` type. This inner `Iterator` class conforms to `IteratorProtocol` and implements its `next` method to call `fatalError`. Swift doesn't have built-in support for abstract classes, so this will have to suffice:

```
        class Iterator: IteratorProtocol {
            func next() -> Element? {
                fatalError("Must override next()")
            }
        }
```

`MAnySequence` gets a similar implementation of `makeIterator`. It calls `fatalError` to encourage its subclass to override it:

```
        func makeIterator() -> Iterator {
            fatalError("Must override makeIterator()")
        }
    }
```

That is the type-erased public API. The private implementation subclasses it. The public class is parameterized by the element type, but the private implementation class is parameterized by the sequence type it wraps:

```
    private class MAnySequenceImpl<Seq: Sequence>: MAnySequence<Seq.Element> {
```

This class needs an internal subclass of the internal `Iterator` class from above:

```
        class IteratorImpl: Iterator {
```

It wraps an instance of the sequence's `Iterator` type:

```
            var wrapped: Seq.Iterator

            init(_ wrapped: Seq.Iterator) {
                self.wrapped = wrapped
            }
```

It implements `next` to call through to that wrapped iterator:

```
            override func next() -> Seq.Element? {
                return wrapped.next()
            }
        }
```

Similarly, `MAnySequenceImpl` wraps an instance of the sequence:

```
        var seq: Seq

        init(_ seq: Seq) {
            self.seq = seq
        }
```

It implements `makeIterator` to get an iterator from wrapped sequence, and then wrap that iterator in `IteratorImpl`:

```
        override func makeIterator() -> IteratorImpl {
            return IteratorImpl(seq.makeIterator())
        }

    }
```

We need a way to actually create these things. A `static` method on `MAnySequence` creates an instance of `MAnySequenceImpl` and returns it to the caller as an `MAnySequence`:

```
    extension MAnySequence {
        static func make<Seq: Sequence>(_ seq: Seq) -> MAnySequence<Element> where Seq.Element == Element {
            return MAnySequenceImpl<Seq>(seq)
        }
    }
```

In production code, we would probably want to clean this up a bit by using an extra level of indirection so that `MAnySequence` could provide an initializer instead.

Let's try it out:

```
    func printInts(_ seq: MAnySequence<Int>) {
        for elt in seq {
            print(elt)
        }
    }

    let array = [1, 2, 3, 4, 5]
    printInts(MAnySequence.make(array))
    printInts(MAnySequence.make(array[1 ..< 4]))
```

It works!

**Type Erasure With Functions**  
We want to expose functionality from multiple types without exposing those types. A natural approach for this is to store functions whose signatures only involve the types we want to expose. The function bodies can be created in a context where the underlying implementation types are known.

Let's look at how `MAnySequence` would look with this approach. It starts off similar to the previous implementation, although this one can be a `struct` rather than a `class` because it's just a dumb container and there's no inheritance:

```
    struct MAnySequence<Element>: Sequence {
```

Like before, it needs an `Iterator` that it can return. This one is also a `struct` and it contains a stored property which is a function that takes no parameters and returns an `Element?`, which is the signature used for the `next` method in `IteratorProtocol`. It then implement `IteratorProtocol` to call that function:

```
        struct Iterator: IteratorProtocol {
            let _next: () -> Element?

            func next() -> Element? {
                return _next()
            }
        }
```

`MAnySequence` itself is similar: it contains a stored property which is a function that takes no arguments and returns an `Iterator`. `Sequence` is then implemented by calling through to that function:

```
        let _makeIterator: () -> Iterator

        func makeIterator() -> Iterator {
            return _makeIterator()
        }
```

`MAnySequence`'s `init` is where the magic happens. It takes an arbitrary `Sequence` as its parameter:

```
        init<Seq: Sequence>(_ seq: Seq) where Seq.Element == Element {
```

It then needs to wrap the functionality of this sequence in a function:

```
            _makeIterator = {
```

How do we make an iterator here? We'll start by asking `seq` to make one:

```
                var iterator = seq.makeIterator()
```

Then we'll wrap that iterator in `Iterator`. Its `_next` function can just call `iterator`'s `next` method:

```
                return Iterator(_next: { iterator.next() })
            }
        }

    }
```

Here's some code that uses it:

```
    func printInts(_ seq: MAnySequence<Int>) {
        for elt in seq {
            print(elt)
        }
    }

    let array = [1, 2, 3, 4, 5]
    printInts(MAnySequence(array))
    printInts(MAnySequence(array[1 ..< 4]))
```

This one works too!

This function-based approach to type erasure can be particularly nice when you need to wrap a small amount of functionality as part of a larger type, and don't need separate classes implementing the entire functionality of whatever types you're erasing.

For example, let's say you want to write some code that works with various collection types, but all it really needs to be able to do with those collections is get a count and do a zero-based integer subscript. For example, this might be a table view data source. It might then look like this:

```
    class GenericDataSource<Element> {
        let count: () -> Int
        let getElement: (Int) -> Element

        init<C: Collection>(_ c: C) where C.Element == Element, C.Index == Int {
            count = { c.count }
            getElement = { c[$0 - c.startIndex] }
        }
    }
```

Then the rest of the code in `GenericDataSource` can easily call `count()` and `getElement()` to perform operations on that passed-in collection, without that collection type contaminating `GenericDataSource`'s generic parameters.

**Conclusion**  
Type erasure is a useful technique for stopping the viral spread of generics in your code, or just keeping interfaces simple. It's accomplished by wrapping the underlying type in a way which separates the API from the functionality. This can be done with an abstract public superclass and a private subclass, or it can be done by wrapping the API in functions. Type erasure with functions is particularly useful for simple cases where you only need a few pieces of functionality.

The Swift standard library provides several type erased types that you can take advantage of. For example, `AnySequence` wraps a `Sequence`, as the name indicates, and lets you iterate over a sequence without needing to know its type. `AnyIterator` is the companion to this type, providing a type-erased iterator. `AnyHashable` provides type-erased access to `Hashable` types. There are a few more for the various collection protocols. Search the documentation for `Any` to see those. The standard library also uses type erasure as part of the `Codable` API: `KeyedEncodingContainer` and `KeyedDecodingContainer` are type-erased wrappers around the corresponding container protocols, and are used to allow `Encoder` and `Decoder` implementations to provide containers without having to incorporate the container types into the API.

That's it for today! Come back next time for more programming fun and games. Friday Q&A is driven by reader suggestions, so if you have a topic you'd like to see me cover here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2017-12-08-type-erasure-in-swift.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
