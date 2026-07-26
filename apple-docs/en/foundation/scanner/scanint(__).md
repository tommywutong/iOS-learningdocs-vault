---
title: 'scanInt(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/scanner/scanint(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/scanner/scanint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner/scanint%28_%3A%29.json'
content_hash: 'sha256:a660bd25ee5e8fff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Scanner](../scanner.md)

# scanInt(_:)

<sub>Instance Method</sub>

Scans for an NSInteger value from a decimal representation, returning a found value by reference

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scanInt(_ result: UnsafeMutablePointer<Int>?) -> Bool
```

## Parameters

- `result` — Upon return, contains the scanned value. Contains `INT_MAX` or `INT_MIN` on overflow.

## Return Value

[true](../../swift/true.md) if the receiver finds a valid integer representation, otherwise [false](../../swift/false.md). Overflow is considered a valid integer representation.

## Discussion

Skips past excess digits in the case of overflow, so the receiver’s position is past the entire integer representation.

Invoke this method with `NULL` as `value` to simply scan past a decimal integer representation.

## See Also

### Related Documentation

- [integerValue](../nsstring/integervalue.md) — The `NSInteger` value of the string.

### Scanning Numeric Values

- [- scanDecimal:](<scandecimal(__).md>) — Scans for an `NSDecimal` value, returning a found value by reference. _(deprecated)_
- [- scanDouble:](<scandouble(__).md>) — Scans for a double value, returning a found value by reference. _(deprecated)_
- [- scanFloat:](<scanfloat(__).md>) — Scans for a float value, returning a found value by reference. _(deprecated)_
- [- scanHexDouble:](<scanhexdouble(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexFloat:](<scanhexfloat(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexInt:](<scanhexint32(__).md>) — Scans for an unsigned value from a hexadecimal representation, returning a found value by reference. _(deprecated)_
- [- scanHexLongLong:](<scanhexint64(__).md>) — Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [- scanInt:](<scanint32(__).md>) — Scans for an int value from a decimal representation, returning a found value by reference. _(deprecated)_
- [- scanLongLong:](<scanint64(__).md>) — Scans for a long long value from a decimal representation, returning a found value by reference.
- [- scanUnsignedLongLong:](<scanunsignedlonglong(__).md>) — Scans for an unsigned long long value from a decimal representation, returning a found value by reference.
