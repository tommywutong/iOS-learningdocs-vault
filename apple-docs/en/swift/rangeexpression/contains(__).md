---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeexpression/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeexpression/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeexpression/contains%28_%3A%29.json'
content_hash: 'sha256:623505d0e7605690'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeExpression](../rangeexpression.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the given element is contained within the range expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ element: Self.Bound) -> Bool
```

## Parameters

- `element` — The element to check for containment.

## Return Value

`true` if `element` is contained in the range expression; otherwise, `false`.
