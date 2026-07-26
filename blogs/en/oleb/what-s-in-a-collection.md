---
title: What’s in a Collection?
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/09/collection-associated-types/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:dd846ef0c0b9a164'
translated: false
---

> 原文：[What’s in a Collection?](https://oleb.net/blog/2016/09/collection-associated-types/)　·　Ole Begemann

# What’s in a Collection?

_This is an excerpt from the Collection Protocols chapter in the upcoming new edition of [Advanced Swift](https://www.objc.io/books/advanced-swift/) (somewhat amended to fit in a blog post). [Chris Eidhof](http://chris.eidhof.nl) and I are almost done updating the book for Swift 3. It will be out real soon now._

Collections in Swift are very powerful but also [very complex](http://chris.eidhof.nl/post/protocols-in-swift/). If you want to implement your own custom collection type, you need to understand how the [`Collection`](https://developer.apple.com/reference/swift/collection) protocol works. And even if all you want to do is _use_ the familiar collection types from the standard library, we think it’s worth learning how things work, not least because it can be a big help in decoding what the compiler wants to tell you with its error messages.

In this article, we’d like to discuss the `Collection` protocol’s [associated types](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Generics.html#//apple_ref/doc/uid/TP40014097-CH26-ID189). This might seem like an obscure topic, but we think understanding what the associated types do and why they are needed is key to understanding collections in Swift.

# Overview

`Collection` has five associated types. They are declared as follows (this is not the actual code because `Index` is declared in `IndexableBase`, but you get the idea):

```
protocol Collection: Indexable, Sequence {
    associatedtype Iterator: IteratorProtocol = IndexingIterator<Self>
    associatedtype SubSequence: IndexableBase, Sequence = Slice<Self>
    associatedtype Index: Comparable // declared in IndexableBase
    associatedtype IndexDistance: SignedInteger = Int
    associatedtype Indices: IndexableBase, Sequence = DefaultIndices<Self>
    ...
}
```

The first four are inherited from the base protocols [`Sequence`](https://developer.apple.com/reference/swift/sequence), [`Indexable`](https://developer.apple.com/reference/swift/indexable), and [`IndexableBase`](https://developer.apple.com/reference/swift/indexablebase)[1](#fn:1); `Collection` restates all of them except `Index` with tighter constraints or different default values, though.

Notice that `Collection` provides defaults for all but one of its associated types — conforming types only have to specify an `Index` type. Even though you don’t _have_ to care much about the other associated types, let’s go through them one by one.

## [Iterator](https://developer.apple.com/reference/swift/collection/iterator)

Inherited from `Sequence`. Sequences provide access to their elements by creating an iterator. The iterator produces the values of the sequence one at a time and keeps track of its iteration state as it traverses through the sequence.

Iterators have an associated type of their own called [`Element`](https://developer.apple.com/reference/swift/iteratorprotocol/element). The `Element` type specifies the type of the values the iterator produces. For example, the element type of the iterator for [`String.CharacterView`](https://developer.apple.com/reference/swift/string.characterview) is [`Character`](https://developer.apple.com/reference/swift/character). By extension, the iterator also defines its sequence’s element type; the fact that `Element` is an associated type of [`IteratorProtocol`](https://developer.apple.com/reference/swift/iteratorprotocol) is why you often see references to `Iterator.Element` in method signatures or generic constraints for `Sequence` and `Collection`.

The default iterator type for collections is [`IndexingIterator<Self>`](https://developer.apple.com/reference/swift/indexingiterator). This is a pretty simple struct that wraps the collection and uses the collection’s own indices to step over each element. Most collections in the standard library use `IndexingIterator` as their iterator. There should be little reason to write your own iterator type for a custom collection.

## [SubSequence](https://developer.apple.com/reference/swift/collection/subsequence)

Also inherited from `Sequence`, but `Collection` restates this type with tighter constraints: a collection’s `SubSequence` should itself also be a `Collection`. (We say “should” rather than “must” because this constraint is currently not fully expressible in the type system.)

`SubSequence` is used as the return type for operations that return slices of the original collection:

- and

  — take the first or last

  elements.
- and

  — return subsequences where the first or last

  elements have been removed.
- — break up the sequence at the specified separator elements and return an array of subsequences.
- with a

  argument — return a slice containing the elements at a range of indices.

The default subsequence type for collections is [`Slice<Self>`](https://developer.apple.com/reference/swift/slice), which wraps the original collection (similar to `IndexingIterator`) and stores the slice’s start and end index in terms of the base collection.

It can make sense for a collection to customize its `SubSequence` type, especially if it can be `Self` (i.e. a slice of the collection has the same type as the collection itself). A standard library type for which this is the case is `String.CharacterView`, which makes working with string slices [more convenient](https://oleb.net/blog/2016/08/swift-3-strings). A counterexample is [`Array`](https://developer.apple.com/reference/swift/array) whose slice type is [`ArraySlice`](https://developer.apple.com/reference/swift/arrayslice).

## [Index](https://developer.apple.com/reference/swift/indexablebase/index)

An index represents a position in the collection. Every collection has two special indices, [`startIndex`](https://developer.apple.com/reference/swift/indexablebase/1786423-startindex) and [`endIndex`](https://developer.apple.com/reference/swift/indexablebase/1782993-endindex). The `startIndex` designates the collection’s first element, and `endIndex` is the index that comes _after_ the last element in the collection. An index should be a dumb value that only stores the minimal amount of information required to describe an element’s position. In particular, indices should not keep a reference to their collection if at all possible. The only requirement for a collection’s `Index` is that it must be [`Comparable`](https://developer.apple.com/reference/swift/comparable), which is another way of saying that indices have a defined order.

We are used to indices being integers as is the case for arrays, but integer indices don’t work for every data structure. Again, take `String.CharacterView` as an example. Characters in Swift [are variable-size](https://oleb.net/blog/2016/08/swift-3-strings); if you wanted to use integer indices, you’d have two options:

1. This is very efficient; accessing an element at a given index is an

  operation. But there would be gaps in the index range. For example, if the character at index 0 had twice the normal size, the next character would be at index 2 — accessing an element at index 1 would either trigger a fatal error or be undefined behavior. This would be a huge violation of user expectations.
2. This is consistent with user expectations — there wouldn’t be any gaps in the index range. However, accessing an element at a given index is now an

  operation; the string must start at the beginning and traverse all elements before the given index to determine where the desired character is stored. This is a big no-no; users expect subscripting on an index to give direct element access in constant time.

As a result, `String.CharacterView.Index` is an opaque value that points to a position in the string’s internal storage buffer. It really is just a wrapper for a single `Int` offset, but that is an implementation detail that is of no interest to users of the collection.

Choosing the correct index type is a choice every collections needs to make individually. That’s why the `Index` type is the only associated type that doesn’t have a default.

## [IndexDistance](https://developer.apple.com/reference/swift/collection/indexdistance)

A signed integer type that represents the number of steps between two indices. There should be no reason to change this from the default [`Int`](https://developer.apple.com/reference/swift/int).

## [Indices](https://developer.apple.com/reference/swift/collection/indices)

The return type of the collection’s [`indices`](https://developer.apple.com/reference/swift/collection/1641719-indices) property. It represents a collection containing all indices that are valid for subscripting the base collection, in ascending order. Note that the [`endIndex`](https://developer.apple.com/reference/swift/indexablebase/1782993-endindex) is not included because it signifies the “past the end” position and thus is not a valid subscript argument.

In Swift 2, the `indices` property returned a [`Range<Index>`](http://swiftdoc.org/v2.2/type/Range/) that could be used to iterate over all valid indices in the collection. In Swift 3, `Range<Index>` is [no longer iterable](https://oleb.net/blog/2016/09/swift-3-ranges) because indices can no longer be advanced on their own (it is now [up to the collection to advance an index](https://github.com/apple/swift-evolution/blob/master/proposals/0065-collections-move-indices.md)). The `Indices` type replaces `Range<Index>` to keep index iterations working.

The default `Indices` type is the imaginatively named [`DefaultIndices<Self>`](https://developer.apple.com/reference/swift/defaultindices). Like `Slice`, it is a pretty simple wrapper for the base collection and a start and end index — it needs to keep a reference to the base collection to be able to advance the indices. This can cause a surprising performance issue if you mutate the collection while iterating over its indices: if the collection is implemented using [copy-on-write](http://chris.eidhof.nl/post/struct-semantics-in-swift/) (as all collections in the standard library are), the extra reference to the collection can trigger an unnecessary copy to be made when the loop is entered.

We cover copy-on-write extensively in the book. For now, it’s enough to know that if your custom collection can provide an alternative `Indices` type that does not need to keep a reference to the base collection, doing so is a worthwhile optimization. This is possible for all collections whose index math does not rely on the collection itself, like arrays. If your index is an integer type you can use [`CountableRange<Index>`](https://developer.apple.com/reference/swift/countablerange). This is how the definition would look for a custom queue type (we implement this type in the book):

```
extension Queue: Collection {
    ...
    
    typealias Indices = CountableRange<Int>
    
    var indices: CountableRange<Int> {
        return startIndex..<endIndex
    }
}
```

1. Feel free to treat the presence of `Indexable` and `IndexableBase` as an implementation detail. These protocols were introduced to work around the limitation that the type system doesn’t support recursive protocol constraints, i.e. constraints on `Collection`’s associated types that reference `Collection` itself.

  Allowing this is part of the highly anticipated [better generics](https://github.com/apple/swift/blob/master/docs/GenericsManifesto.md) support we will hopefully see within the next year. When it happens, we expect `Indexable` and `IndexableBase` to be removed and their functionality folded into `Collection`. [↩︎](#fnref:1)
