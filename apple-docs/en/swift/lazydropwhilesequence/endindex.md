---
title: endIndex
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazydropwhilesequence/endindex
source_url: 'https://developer.apple.com/documentation/swift/lazydropwhilesequence/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazydropwhilesequence/endindex.json'
content_hash: 'sha256:ce558bd19e7f1e17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyDropWhileSequence](../lazydropwhilesequence.md)

# endIndex

<sub>Instance Property</sub>

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: LazyDropWhileSequence<Base>.Index { get }
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
