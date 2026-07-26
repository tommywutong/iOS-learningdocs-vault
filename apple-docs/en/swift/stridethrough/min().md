---
title: min()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/stridethrough/min()
source_url: 'https://developer.apple.com/documentation/swift/stridethrough/min()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stridethrough/min%28%29.json'
content_hash: 'sha256:d06f7439d7cdf3e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StrideThrough](../stridethrough.md)

# min()

<sub>Instance Method</sub>

Returns the minimum element in the sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@warn_unqualified_access func min() -> Self.Element?
```

## Return Value

The sequence’s minimum element. If the sequence has no elements, returns `nil`.

## Discussion

This example finds the smallest value in an array of height measurements.

```swift
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let lowestHeight = heights.min()
print(lowestHeight)
// Prints "Optional(58.5)"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.
