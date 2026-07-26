---
title: floatValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/floatvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/floatvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/floatvalue.json'
content_hash: 'sha256:f45edbf251e22a79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# floatValue

<sub>Instance Property</sub>

The floating-point value of the string as a `float`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var floatValue: Float { get }
```

## Discussion

This property doesn’t include whitespace at the beginning of the string. This property is `HUGE_VAL` or `–HUGE_VAL` on overflow, `0.0` on underflow. This property is `0.0` if the string doesn’t begin with a valid text representation of a floating-point number.

This method uses formatting information stored in the non-localized value; use an [Scanner](../scanner.md) object for localized scanning of numeric values from a string.

## See Also

### Related Documentation

- [- scanFloat:](<../scanner/scanfloat(__).md>) — Scans for a float value, returning a found value by reference. _(deprecated)_

### Getting Numeric Values

- [doubleValue](doublevalue.md) — The floating-point value of the string as a `double`.
- [intValue](intvalue.md) — The integer value of the string.
- [integerValue](integervalue.md) — The `NSInteger` value of the string.
- [longLongValue](longlongvalue.md) — The `long long` value of the string.
- [boolValue](boolvalue.md) — The Boolean value of the string.
