---
title: Element
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncsequence/element
source_url: 'https://developer.apple.com/documentation/swift/asyncsequence/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncsequence/element.json'
content_hash: 'sha256:f4038dc590c9dcb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncSequence](../asyncsequence.md)

# Element

<sub>Associated Type</sub>

The type of element produced by this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Element where Self.Element == Self.AsyncIterator.Element
```

## See Also

### Creating an Iterator

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIterator](asynciterator.md) — The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [AsyncIteratorProtocol](../asynciteratorprotocol.md) — A type that asynchronously supplies the values of a sequence one at a time.
