---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anyiterator/init(_:)-3m1u6'
source_url: 'https://developer.apple.com/documentation/swift/anyiterator/init(_:)-3m1u6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyiterator/init%28_%3A%29-3m1u6.json'
content_hash: 'sha256:9e6b1f7d424326ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyIterator](../anyiterator.md)

# init(_:)

<sub>Initializer</sub>

Creates an iterator that wraps a base iterator but whose type depends only on the base iterator’s element type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<I>(_ base: I) where Element == I.Element, I : IteratorProtocol
```

## Parameters

- `base` — An iterator to type-erase.

## Discussion

You can use `AnyIterator` to hide the type signature of a more complex iterator. For example, the `digits()` function in the following example creates an iterator over a collection that lazily maps the elements of a `Range<Int>` instance to strings. Instead of returning an iterator with a type that encapsulates the implementation of the collection, the `digits()` function first wraps the iterator in an `AnyIterator` instance.

```swift
func digits() -> AnyIterator<String> {
    let lazyStrings = (0..<10).lazy.map { String($0) }
    let iterator:
        LazyMapSequence<Range<Int>, String>.Iterator
        = lazyStrings.makeIterator()

    return AnyIterator(iterator)
}
```
