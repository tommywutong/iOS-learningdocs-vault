---
title: 'NSDecimalIsNotANumber(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalisnotanumber(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalisnotanumber(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalisnotanumber%28_%3A%29.json'
content_hash: 'sha256:0c1fb788af89bbfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalIsNotANumber(_:)

<sub>Function</sub>

Returns a Boolean that indicates whether a given decimal contains a valid number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSDecimalIsNotANumber(_ dcm: UnsafePointer<Decimal>) -> Bool
```

## Return Value

[false](../swift/false.md) if the value in `dcm` represents a valid number, otherwise [true](../swift/true.md).

## Discussion

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).
