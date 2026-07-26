---
title: 'NSDecimalCopy(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalcopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalcopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalcopy%28_%3A_%3A%29.json'
content_hash: 'sha256:b248501d8c919113'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalCopy(_:_:)

<sub>Function</sub>

Copies the value of a decimal number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSDecimalCopy(_ destination: UnsafeMutablePointer<Decimal>, _ source: UnsafePointer<Decimal>)
```

## Parameters

- `destination` — A [Decimal](decimal.md) reference that receives the copied value.

- `source` — A source [Decimal](decimal.md) to copy.

## Discussion

Copies the value in `source` to `destination`.

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).

## See Also

### Creating a decimal from another decimal

- [init(signOf:magnitudeOf:)](<decimal/init(signof_magnitudeof_).md>) — Creates and initializes a decimal with the sign and magnitude of the given decimals.
