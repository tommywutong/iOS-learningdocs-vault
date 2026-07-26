---
title: boolValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/boolvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/boolvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/boolvalue.json'
content_hash: 'sha256:fc10ed8a3cf66999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# boolValue

<sub>Instance Property</sub>

The Boolean value of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boolValue: Bool { get }
```

## Discussion

This property is [true](../../swift/true.md) on encountering one of “Y”, “y”, “T”, “t”, or a digit 1-9—the method ignores any trailing characters. This property is [false](../../swift/false.md) if the receiver doesn’t begin with a valid decimal text representation of a number.

The property assumes a decimal representation and skips whitespace at the beginning of the string. It also skips initial whitespace characters, or optional -/+ sign followed by zeroes.

## See Also

### Related Documentation

- [- scanInt:](<../scanner/scanint32(__).md>) — Scans for an int value from a decimal representation, returning a found value by reference. _(deprecated)_

### Getting Numeric Values

- [doubleValue](doublevalue.md) — The floating-point value of the string as a `double`.
- [floatValue](floatvalue.md) — The floating-point value of the string as a `float`.
- [intValue](intvalue.md) — The integer value of the string.
- [integerValue](integervalue.md) — The `NSInteger` value of the string.
- [longLongValue](longlongvalue.md) — The `long long` value of the string.
