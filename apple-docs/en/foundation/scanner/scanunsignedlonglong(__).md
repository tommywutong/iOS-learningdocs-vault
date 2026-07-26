---
title: 'scanUnsignedLongLong(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/scanner/scanunsignedlonglong(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scanunsignedlonglong(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scanunsignedlonglong%28_%3A%29.json'
content_hash: 'sha256:8868e05dc3e934f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanUnsignedLongLong(_:)

<sub>Instance Method</sub>

Scans for an unsigned long long value from a decimal representation, returning a found value by reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scanUnsignedLongLong(_ result: UnsafeMutablePointer<UInt64>?) -> Bool
```

## Parameters

- `result` — Upon return, contains the scanned value. Contains `ULLONG_MAX` on overflow.

## Return Value

[true](../../swift/true.md) if the receiver finds a valid decimal integer representation, otherwise [false](../../swift/false.md). Overflow is considered a valid decimal integer representation.

## Discussion

All overflow digits are skipped. Skips past excess digits in the case of overflow, so the receiver’s position is past the entire decimal representation.

Invoke this method with `NULL` as `unsignedLongLongValue` to simply scan past an unsigned long decimal integer representation.

## See Also

### Scanning Numeric Values

- [- scanDecimal:](<scandecimal(__).md>) — Scans for an `NSDecimal` value, returning a found value by reference. _(deprecated)_
- [- scanDouble:](<scandouble(__).md>) — Scans for a double value, returning a found value by reference. _(deprecated)_
- [- scanFloat:](<scanfloat(__).md>) — Scans for a float value, returning a found value by reference. _(deprecated)_
- [- scanHexDouble:](<scanhexdouble(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexFloat:](<scanhexfloat(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexInt:](<scanhexint32(__).md>) — Scans for an unsigned value from a hexadecimal representation, returning a found value by reference. _(deprecated)_
- [- scanHexLongLong:](<scanhexint64(__).md>) — Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [- scanInteger:](<scanint(__).md>) — Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [- scanInt:](<scanint32(__).md>) — Scans for an int value from a decimal representation, returning a found value by reference. _(deprecated)_
- [- scanLongLong:](<scanint64(__).md>) — Scans for a long long value from a decimal representation, returning a found value by reference.
