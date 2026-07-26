---
title: doubleValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/doublevalue
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/doublevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/doublevalue.json'
content_hash: 'sha256:13a6119feed5e023'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# doubleValue

<sub>Instance Property</sub>

The floating-point value of the string as a `double`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var doubleValue: Double { get }
```

## Discussion

This property doesn’t include any whitespace at the beginning of the string. This property is `HUGE_VAL` or `–HUGE_VAL` on overflow, `0.0` on underflow. This property is `0.0` if the string doesn’t begin with a valid text representation of a floating-point number.

This property uses formatting information stored in the non-localized value; use an [Scanner](../scanner.md) object for localized scanning of numeric values from a string.

## See Also

### Related Documentation

- [- scanDouble:](<../scanner/scandouble(__).md>) — Scans for a double value, returning a found value by reference. _(deprecated)_

### Getting Numeric Values

- [floatValue](floatvalue.md) — The floating-point value of the string as a `float`.
- [intValue](intvalue.md) — The integer value of the string.
- [integerValue](integervalue.md) — The `NSInteger` value of the string.
- [longLongValue](longlongvalue.md) — The `long long` value of the string.
- [boolValue](boolvalue.md) — The Boolean value of the string.
