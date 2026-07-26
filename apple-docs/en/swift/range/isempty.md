---
title: isEmpty
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/range/isempty
source_url: 'https://developer.apple.com/documentation/swift/range/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/isempty.json'
content_hash: 'sha256:9d4c7edd09be3bf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value indicating whether the range contains no elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

An empty `Range` instance has equal lower and upper bounds.

```swift
let empty: Range = 10..<10
print(empty.isEmpty)
// Prints "true"
```

## See Also

### Inspecting a Range

- [lowerBound](lowerbound.md) — The range’s lower bound.
- [upperBound](upperbound.md) — The range’s upper bound.
