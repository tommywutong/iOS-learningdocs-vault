---
title: 'scanDecimal(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/scanner/scandecimal(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scandecimal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scandecimal%28_%3A%29.json'
content_hash: 'sha256:a84dcdabdff4af2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanDecimal(_:)

<sub>Instance Method</sub>

Scans for an `NSDecimal` value, returning a found value by reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scanDecimal(_ dcm: UnsafeMutablePointer<Decimal>?) -> Bool
```

## Parameters

- `dcm` — Upon return, contains the scanned value. See the [NSDecimalNumber](../nsdecimalnumber.md) class specification for more information about `NSDecimal` values.

## Return Value

[true](../../swift/true.md) if the receiver finds a valid `NSDecimal` representation, otherwise [false](../../swift/false.md).

## Discussion

Invoke this method with `NULL` as `decimalValue` to simply scan past an `NSDecimal` representation.

## See Also

### Scanning Numeric Values

- [- scanDouble:](<scandouble(__).md>) — Scans for a double value, returning a found value by reference. _(deprecated)_
- [- scanFloat:](<scanfloat(__).md>) — Scans for a float value, returning a found value by reference. _(deprecated)_
- [- scanHexDouble:](<scanhexdouble(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexFloat:](<scanhexfloat(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexInt:](<scanhexint32(__).md>) — Scans for an unsigned value from a hexadecimal representation, returning a found value by reference. _(deprecated)_
- [- scanHexLongLong:](<scanhexint64(__).md>) — Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [- scanInteger:](<scanint(__).md>) — Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [- scanInt:](<scanint32(__).md>) — Scans for an int value from a decimal representation, returning a found value by reference. _(deprecated)_
- [- scanLongLong:](<scanint64(__).md>) — Scans for a long long value from a decimal representation, returning a found value by reference.
- [- scanUnsignedLongLong:](<scanunsignedlonglong(__).md>) — Scans for an unsigned long long value from a decimal representation, returning a found value by reference.
