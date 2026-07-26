---
title: 'advanced(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint8/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/swift/uint8/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/advanced%28by%3A%29.json'
content_hash: 'sha256:4ec4da2f4c7a7d79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt8](../uint8.md)

# advanced(by:)

<sub>Instance Method</sub>

Returns a value that is offset the specified distance from this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by n: Int) -> Self
```

## Parameters

- `n` — The distance to advance this value.

## Return Value

A value that is offset from this value by `n`.

## Discussion

Use the `advanced(by:)` method in generic code to offset a value by a specified distance. If you’re working directly with numeric values, use the addition operator (`+`) instead of this method.

For a value `x`, a distance `n`, and a value `y = x.advanced(by: n)`, `x.distance(to: y) == n`.
