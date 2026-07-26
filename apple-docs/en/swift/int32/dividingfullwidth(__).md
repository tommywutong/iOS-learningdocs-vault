---
title: 'dividingFullWidth(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int32/dividingfullwidth(_:)'
source_url: 'https://developer.apple.com/documentation/swift/int32/dividingfullwidth(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int32/dividingfullwidth%28_%3A%29.json'
content_hash: 'sha256:6b246a458cc0ca40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int32](../int32.md)

# dividingFullWidth(_:)

<sub>Instance Method</sub>

Returns a tuple containing the quotient and remainder of dividing the given value by this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dividingFullWidth(_ dividend: (high: Int32, low: Int32.Magnitude)) -> (quotient: Int32, remainder: Int32)
```

## Parameters

- `dividend` — A tuple containing the high and low parts of a double-width integer. The `high` component of the value carries the sign, if the type is signed.

## Return Value

A tuple containing the quotient and remainder of `dividend` divided by this value.

## Discussion

The resulting quotient must be representable within the bounds of the type. If the quotient of dividing `dividend` by this value is too large to represent in the type, a runtime error will occur.
