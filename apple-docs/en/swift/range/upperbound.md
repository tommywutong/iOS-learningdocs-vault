---
title: upperBound
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/range/upperbound
source_url: 'https://developer.apple.com/documentation/swift/range/upperbound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/upperbound.json'
content_hash: 'sha256:ea6629daef29a85e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# upperBound

<sub>Instance Property</sub>

The range’s upper bound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let upperBound: Bound
```

## Discussion

In an empty range, `upperBound` is equal to `lowerBound`. A `Range` instance does not contain its upper bound.

## See Also

### Inspecting a Range

- [isEmpty](isempty.md) — A Boolean value indicating whether the range contains no elements.
- [lowerBound](lowerbound.md) — The range’s lower bound.
