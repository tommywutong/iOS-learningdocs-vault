---
title: 'compare(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/compare(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/compare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/compare%28_%3A%29.json'
content_hash: 'sha256:07e04c03a3314396'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# compare(_:)

<sub>Instance Method</sub>

Compares this decimal number and another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ decimalNumber: NSNumber) -> ComparisonResult
```

## Parameters

- `decimalNumber` — The number with which to compare the receiver. This value must not be `nil`. If this value is `nil`, the behavior is undefined and may change in future versions of macOS.

## Return Value

`NSOrderedAscending` if the value of `decimalNumber` is greater than the receiver; `NSOrderedSame` if they’re equal; and `NSOrderedDescending` if the value of `decimalNumber` is less than the receiver.
