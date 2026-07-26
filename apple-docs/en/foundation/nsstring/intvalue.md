---
title: intValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/intvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/intvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/intvalue.json'
content_hash: 'sha256:8195bcc4366188cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# intValue

<sub>Instance Property</sub>

The integer value of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var intValue: Int32 { get }
```

## Discussion

The integer value of the string, assuming a decimal representation and skipping whitespace at the beginning of the string. This property is `INT_MAX` or `INT_MIN` on overflow. This property is `0` if the string doesn’t begin with a valid decimal text representation of a number.

This property uses formatting information stored in the non-localized value; use an [Scanner](../scanner.md) object for localized scanning of numeric values from a string.

### Special Considerations

In macOS 10.5 and later, use [integerValue](integervalue.md) instead.

## See Also

### Related Documentation

- [- scanInt:](<../scanner/scanint32(__).md>) — Scans for an int value from a decimal representation, returning a found value by reference. _(deprecated)_

### Getting Numeric Values

- [doubleValue](doublevalue.md) — The floating-point value of the string as a `double`.
- [floatValue](floatvalue.md) — The floating-point value of the string as a `float`.
- [integerValue](integervalue.md) — The `NSInteger` value of the string.
- [longLongValue](longlongvalue.md) — The `long long` value of the string.
- [boolValue](boolvalue.md) — The Boolean value of the string.
