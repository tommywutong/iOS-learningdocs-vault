---
title: Element
framework: Swift
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/sequence/element
source_url: 'https://developer.apple.com/documentation/swift/sequence/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/element.json'
content_hash: 'sha256:ab359717b36930b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# Element

<sub>Associated Type</sub>

A type representing the sequence’s elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Element where Self.Element == Self.Iterator.Element
```

## See Also

### Creating an Iterator

- [makeIterator()](<makeiterator().md>) — Returns an iterator over the elements of this sequence.
- [Iterator](iterator.md) — A type that provides the sequence’s iteration interface and encapsulates its iteration state.
