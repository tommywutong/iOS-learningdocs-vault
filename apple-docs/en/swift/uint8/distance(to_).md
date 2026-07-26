---
title: 'distance(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint8/distance(to:)'
source_url: 'https://developer.apple.com/documentation/swift/uint8/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/distance%28to%3A%29.json'
content_hash: 'sha256:effe9e423cecd30a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt8](../uint8.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the distance from this value to the given value, expressed as a stride.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: Self) -> Int
```

## Parameters

- `other` — The value to calculate the distance to.

## Return Value

The distance from this value to `other`.

## Discussion

For two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`.
