---
title: 'scanHexFloat(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/scanner/scanhexfloat(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scanhexfloat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scanhexfloat%28_%3A%29.json'
content_hash: 'sha256:2794fea523b31a66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanHexFloat(_:)

<sub>Instance Method</sub>

Scans for a double value from a hexadecimal representation, returning a found value by reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scanHexFloat(_ result: UnsafeMutablePointer<Float>?) -> Bool
```

## Parameters

- `result` — Upon return, contains the scanned value. Contains `HUGE_VAL` or `–HUGE_VAL` on overflow, or `0.0` on underflow.

## Return Value

[true](../../swift/true.md) if the receiver finds a valid float-point representation, otherwise [false](../../swift/false.md). Overflow or underflow are both considered valid floating-point representations.

## Discussion

This corresponds to `%a` or `%A` formatting. The hexadecimal float representation must be preceded by `0x` or `0X`.

Skips past excess digits in the case of overflow, so the scanner’s position is past the entire floating-point representation.

Invoke this method with `NULL` as `result` to simply scan past a hexadecimal float representation.

## See Also

### Scanning Numeric Values

- [- scanDecimal:](<scandecimal(__).md>) — Scans for an `NSDecimal` value, returning a found value by reference. _(deprecated)_
- [- scanDouble:](<scandouble(__).md>) — Scans for a double value, returning a found value by reference. _(deprecated)_
- [- scanFloat:](<scanfloat(__).md>) — Scans for a float value, returning a found value by reference. _(deprecated)_
- [- scanHexDouble:](<scanhexdouble(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexInt:](<scanhexint32(__).md>) — Scans for an unsigned value from a hexadecimal representation, returning a found value by reference. _(deprecated)_
- [- scanHexLongLong:](<scanhexint64(__).md>) — Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [- scanInteger:](<scanint(__).md>) — Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [- scanInt:](<scanint32(__).md>) — Scans for an int value from a decimal representation, returning a found value by reference. _(deprecated)_
- [- scanLongLong:](<scanint64(__).md>) — Scans for a long long value from a decimal representation, returning a found value by reference.
- [- scanUnsignedLongLong:](<scanunsignedlonglong(__).md>) — Scans for an unsigned long long value from a decimal representation, returning a found value by reference.
