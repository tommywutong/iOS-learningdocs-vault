---
title: isEmpty
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/closedrange/isempty
source_url: 'https://developer.apple.com/documentation/swift/closedrange/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/closedrange/isempty.json'
content_hash: 'sha256:e5ffc73652eb477f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ClosedRange](../closedrange.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value indicating whether the range contains no elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

Because a closed range cannot represent an empty range, this property is always `false`.

## See Also

### Inspecting a Range

- [lowerBound](lowerbound.md) — The range’s lower bound.
- [upperBound](upperbound.md) — The range’s upper bound.
