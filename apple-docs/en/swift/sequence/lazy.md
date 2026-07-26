---
title: lazy
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/sequence/lazy
source_url: 'https://developer.apple.com/documentation/swift/sequence/lazy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/lazy.json'
content_hash: 'sha256:9565e9f237f20c51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# lazy

<sub>Instance Property</sub>

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lazy: LazySequence<Self> { get }
```

## See Also

### Transforming a Sequence

- [map(_:)](<map(__).md>) — Returns an array containing the results of mapping the given closure over the sequence’s elements.
- [compactMap(_:)](<compactmap(__).md>) — Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [flatMap(_:)](<flatmap(__)-jo2y.md>) — Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [reduce(_:_:)](<reduce(____).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [reduce(into:_:)](<reduce(into___).md>) — Returns the result of combining the elements of the sequence using the given closure.
- [flatMap(_:)](<flatmap(__)-383uq.md>)
