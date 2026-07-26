---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/collectiondifference/endindex
source_url: 'https://developer.apple.com/documentation/swift/collectiondifference/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectiondifference/endindex.json'
content_hash: 'sha256:cd37076bbe1bd076'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionDifference](../collectiondifference.md)

# endIndex

<sub>Instance Property</sub>

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: CollectionDifference<ChangeElement>.Index { get }
```

## Discussion

When you need a range that includes the last element of a collection, use the half-open range operator (`..<`) with `endIndex`. The `..<` operator creates a range that doesn’t include the upper bound, so it’s always safe to use with `endIndex`. For example:

```swift
let numbers = [10, 20, 30, 40, 50]
if let index = numbers.firstIndex(of: 30) {
    print(numbers[index ..< numbers.endIndex])
}
// Prints "[30, 40, 50]"
```

If the collection is empty, `endIndex` is equal to `startIndex`.
