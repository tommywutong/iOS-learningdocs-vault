---
title: max()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/unicodescalarview/max()
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/max()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/max%28%29.json'
content_hash: 'sha256:3a5d2a8d8f1a5624'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# max()

<sub>Instance Method</sub>

Returns the maximum element in the sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@warn_unqualified_access func max() -> Self.Element?
```

## Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

## Discussion

This example finds the largest value in an array of height measurements.

```swift
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let greatestHeight = heights.max()
print(greatestHeight)
// Prints "Optional(67.5)"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.
