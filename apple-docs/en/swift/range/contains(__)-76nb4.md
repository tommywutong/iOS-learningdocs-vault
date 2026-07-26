---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/range/contains(_:)-76nb4'
source_url: 'https://developer.apple.com/documentation/swift/range/contains(_:)-76nb4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range/contains%28_%3A%29-76nb4.json'
content_hash: 'sha256:fb3d2794858cf58e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Range](../range.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given element is contained within the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ element: Bound) -> Bool
```

## Parameters

- `element` — The element to check for containment.

## Return Value

`true` if `element` is contained in the range; otherwise, `false`.

## Discussion

Because `Range` represents a half-open range, a `Range` instance does not contain its upper bound. `element` is contained in the range if it is greater than or equal to the lower bound and less than the upper bound.
