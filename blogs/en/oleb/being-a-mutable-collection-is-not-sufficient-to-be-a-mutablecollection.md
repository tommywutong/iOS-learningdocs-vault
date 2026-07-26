---
title: Being a Mutable Collection is not Sufficient to be a MutableCollection
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/02/why-is-dictionary-not-a-mutablecollection/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:98854566ca705915'
translated: false
---

> 原文：[Being a Mutable Collection is not Sufficient to be a MutableCollection](https://oleb.net/blog/2017/02/why-is-dictionary-not-a-mutablecollection/)　·　Ole Begemann

# Being a Mutable Collection is not Sufficient to be a MutableCollection

The [`Collection`](https://developer.apple.com/reference/swift/collection) protocol is the basis for collections in Swift. In addition to `Collection`, the standard library provides four protocols that collections can adopt to document additional capabilities. These protocols _refine_ `Collection` — any type that conforms to one of them must also conform to `Collection`.

[![Swift Collection Protocol Hierarchy](https://oleb.net/media/swift-3-collection-protocols-diagram-v2.png)](https://oleb.net/media/swift-3-collection-protocols-diagram-v2.png)

They are:

- **[`BidirectionalCollection`](https://developer.apple.com/reference/swift/bidirectionalcollection):** A collection that can be traversed forward _and_ backward. An example is [`String.CharacterView`](https://developer.apple.com/reference/swift/string.characterview).^[1](#fn:bidirec)

- **[`RandomAccessCollection`](https://developer.apple.com/reference/swift/randomaccesscollection):** A collection that can access any element in constant time. [`Array`](https://developer.apple.com/reference/swift/array) is the canonical example.
- **[`MutableCollection`](https://developer.apple.com/reference/swift/mutablecollection):** A collection that supports mutation of its elements through subscript assignment, i.e. `array[index] = newValue`.
- **[`RangeReplaceableCollection`](https://developer.apple.com/reference/swift/rangereplaceablecollection):** A collection that supports insertion and removal of arbitrary subranges of elements.

`RandomAccessCollection` refines `BidirectionalCollection` since it is a strict superset — any collection that can jump efficiently to an arbitrary index can be traversed backward. `RandomAccessCollection` provides no new APIs over `BidirectionalCollection`; there’s nothing you can do with the former that you couldn’t do with the latter. However, its stricter performance guarantees enable an entire class of algorithms that can only be implemented efficiently with random element access.

You might think that `RangeReplaceableCollection` should similarly refine `MutableCollection` because mutation can be modeled with insertion and removal, but that isn’t the case. These two protocols stand side by side — some types only conform to `MutableCollection` (an example is [`UnsafeMutableBufferPointer`](https://developer.apple.com/reference/swift/unsafemutablebufferpointer)), some only to `RangeReplaceableCollection` (e.g. `String.CharacterView`), and only some adopt both (`Array` and [`Data`](https://developer.apple.com/reference/foundation/data)).

Let’s look at a few examples to see why.

# `Set`

## `MutableCollection`

A [`MutableCollection`](https://developer.apple.com/reference/swift/mutablecollection) supports in-place element mutation. The single new API requirement it adds to `Collection` is that the [`subscript`](https://developer.apple.com/reference/swift/mutablecollection/1640969-subscript) now must also have a setter.

A [`Set`](https://developer.apple.com/reference/swift/set) is a `Collection` and it is certainly mutable. It seems therefore logical that it should conform to `MutableCollection`, yet it doesn’t. The reason why boils down to the protocol’s [semantics](https://oleb.net/blog/2016/12/protocols-have-semantics/).

`MutableCollection` allows changing the values of a collection’s elements, but the protocol’s documentation stipulates that the mutation must neither change the length of the collection nor the order of the elements. `Set` can’t satisfy either of these requirements.

Let’s start with preserving length. Sets don’t contain duplicate elements, so if you replace one element with a value that is already in the set, the set would have one less element after the mutation.

Sets are also unordered collections — the order of the elements is undefined as far as the code using the collection is concerned. However, _internally_ , sets do have a stable element order that’s defined by their implementation. When you mutate a `MutableCollection` via subscript assignment, the index of the mutated element must remain stable, i.e. the position of the index in the `indices` collection must not change. `Set` can’t meet this requirement because a `SetIndex` points to the bucket in the set’s internal storage where the corresponding element is stored, and that bucket can change when the element is mutated.

## `RangeReplaceableCollection`

[`RangeReplaceableCollection`](https://developer.apple.com/reference/swift/rangereplaceablecollection) adds two requirements to `Collection`: [an empty initializer](https://developer.apple.com/reference/swift/rangereplaceablecollection/1641467-init) that creates a new, empty collection, and the [`replaceSubrange(_:with:)`](https://developer.apple.com/reference/swift/rangereplaceablecollection/1641256-replacesubrange) method that replaces the elements in the given range with elements from another collection. The target range and the collection containing the new elements can have different lengths, and either one can be empty. The protocol uses this one method to provide default implementations for removing and inserting elements at arbitrary positions.

`Set` isn’t a `RangeReplaceableCollection` either. The main reason why is basically the same as for the missing `MutableCollection` conformance: it doesn’t satisfy the protocol’s [semantics](https://oleb.net/blog/2016/12/protocols-have-semantics/).

The documentation for [`replaceSubrange(_:with:)`](https://developer.apple.com/reference/swift/rangereplaceablecollection/1641256-replacesubrange) specifies that this method has the effect of removing the specified range of elements from the collection and inserting the new elements _at the same location_. This is fundamentally incompatible with the fact that any insertion or removal can change the internal location of any element in the set.

Moreover, even if `Set` could somehow maintain a stable _internal_ element order, `RangeReplaceableCollection` wouldn’t be a good semantic fit for it because most methods the protocol defines don’t make sense for a set. For example, the name of the [`append(_:)`](https://developer.apple.com/reference/swift/rangereplaceablecollection/1641557-append) method in `RangeReplaceableCollection` implies that it inserts an element at the end of the collection. The corresponding operation for `Set` is rightly called [`insert(_:)`](https://developer.apple.com/reference/swift/set/1541375-insert) since you can’t meaningfully append anything to an unordered collection.

# `Dictionary`

The story for [`Dictionary`](https://developer.apple.com/reference/swift/dictionary) is largely the same as for `Set`. Both are unordered collections based on a hash table implementation.^[2](#fn:gyb) Hence `Dictionary` can’t conform to `MutableCollection` and `RangeReplaceableCollection` for the same reasons `Set` can’t.

Another aspect is unique to dictionaries. A `Dictionary`’s element type — i.e. the associated [`Iterator.Element`](https://developer.apple.com/reference/swift/iteratorprotocol/element) type it specifies in its `Collection` conformance — is a [`(Key, Value)` tuple](https://developer.apple.com/reference/swift/dictionary/element):

```
struct Dictionary<Key: Hashable, Value>: Collection {
    typealias Element = (key: Key, value: Value)
    typealias Index = DictionaryIndex<Key, Value>

    subscript(position: Index) -> Element {
        ...
    }
    ...
}
```

This means that all APIs `Dictionary` inherits from `Collection` and `Sequence` treat these `(Key, Value)` pairs as the dictionary’s elements. This is why you get a `(Key, Value)` pair when you iterate over a `Dictionary` in a `for` loop.

The [`Index`](https://developer.apple.com/reference/swift/dictionary.index) is a completely separate type and not in any way related to the `Key` type. As a result, the dictionary [`subscript` you’re familiar with](https://developer.apple.com/reference/swift/dictionary/1540848-subscript) that takes a `Key` and returns an `Optional<Value>` is _not_ the subscript that’s provided by the `Collection` protocol. Rather, it is an addition that’s defined directly on `Dictionary` and totally unrelated to `Collection`. You’ll probably use the dictionary-specific subscript in most situations, but the `Collection` variant is still there:

```
let dict = ["Berlin": 1237, "New York": 1626]
dict["Berlin"] // returns Optional<Int>
for index in dict.indices {
    dict[index] // returns (key: String, value: Int) (not optional!)
}
```

All `Dictionary` would gain from conforming to `MutableCollection` and/or `RangeReplaceableCollection` would be methods that operate on `Index` values and `(Key, Value)` pairs, which is probably not compelling enough to invest anything in the conformance even if it were compatible with the type’s implementation.

# Conclusion

The `Sequence` and `Collection` protocols form the foundation of Swift’s collection types. The specialized collection types `BidirectionalCollection`, `RandomAccessCollection`, `MutableCollection`, and `RandomAccessCollection` provide very fine-grained control over the functionality and performance characteristics of your own custom types and algorithms. [Semantics](https://oleb.net/blog/2016/12/protocols-have-semantics/) are an imporant factor when deciding whether a type should conform to one or more of these protocols.

[In the next article](https://oleb.net/blog/2017/02/why-is-string-characterview-not-a-mutablecollection/) I’ll discuss another interesting type in the context of its conformance to the specialized collection protocols: [`String.CharacterView`](https://developer.apple.com/reference/swift/string.characterview).

1. While you can’t jump efficiently to an arbitrary position in a [`characters`](https://developer.apple.com/reference/swift/string/1540072-characters) collection (because [grapheme clusters are variable-length](https://oleb.net/blog/2016/08/swift-3-strings/)), it’s no problem to find the [`Character`](https://developer.apple.com/reference/swift/character) _before_ a given index. [↩︎](#fnref:bidirec)
2. `Dictionary` and `Set` are so similar that they share a single implementation in the standard library, using the [GYB templating language](https://forums.swift.org/t/what-are-swift-gyb-files/303/2) for code generation. You can find it in [`HashedCollections.swift.gyb`](https://github.com/apple/swift/blob/master/stdlib/public/core/HashedCollections.swift.gyb). [↩︎](#fnref:gyb)
