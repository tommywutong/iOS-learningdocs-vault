---
title: 'allSatisfy(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asynccompactmapsequence/allsatisfy(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asynccompactmapsequence/allsatisfy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asynccompactmapsequence/allsatisfy%28_%3A%29.json'
content_hash: 'sha256:839bc32986de6ecd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncCompactMapSequence](../asynccompactmapsequence.md)

# allSatisfy(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func allSatisfy(_ predicate: (Self.Element) async throws -> Bool) async rethrows -> Bool
```

## Parameters

- `predicate` — A closure that takes an element of the asynchronous sequence as its argument and returns a Boolean value that indicates whether the passed element satisfies a condition.

## Return Value

`true` if the sequence contains only elements that satisfy `predicate`; otherwise, `false`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `allSatisfy(_:)` method checks to see whether all elements produced by the sequence are less than `10`.

```swift
let allLessThanTen = await Counter(howHigh: 10)
    .allSatisfy { $0 < 10 }
print(allLessThanTen)
// Prints "false"
```

The predicate executes each time the asynchronous sequence produces an element, until either the predicate returns `false` or the sequence ends.

If the asynchronous sequence is empty, this method returns `true`.
