---
title: decimalValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnumber/decimalvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsnumber/decimalvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnumber/decimalvalue.json'
content_hash: 'sha256:f6621afe6e77b91e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNumber](../nsnumber.md)

# decimalValue

<sub>Instance Property</sub>

The number object’s value expressed as an [Decimal](../decimal.md) structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var decimalValue: Decimal { get }
```

## Discussion

The [Decimal](../decimal.md) value isn’t guaranteed to be exact for `float` and `double` values.

## See Also

### Accessing Numeric Values

- [boolValue](boolvalue.md) — The number object’s value expressed as a Boolean value.
- [charValue](int8value.md) — The number object’s value expressed as a `char`.
- [doubleValue](doublevalue.md) — The number object’s value expressed as a `double`, converted as necessary.
- [floatValue](floatvalue.md) — The number object’s value expressed as a `float`, converted as necessary.
- [intValue](int32value.md) — The number object’s value expressed as an `int`, converted as necessary.
- [integerValue](intvalue-95zzp.md) — The number object’s value expressed as an `NSInteger` object, converted as necessary.
- [longLongValue](int64value.md) — The number object’s value expressed as a `long long`, converted as necessary.
- [shortValue](int16value.md) — The number object’s value expressed as a `short`, converted as necessary.
- [unsignedCharValue](uint8value.md) — The number object’s value expressed as an unsigned `char`, converted as necessary.
- [unsignedIntegerValue](uintvalue.md) — The number object’s value expressed as an `NSUInteger` object, converted as necessary.
- [unsignedIntValue](uint32value.md) — The number object’s value expressed as an unsigned `int`, converted as necessary.
- [unsignedLongLongValue](uint64value.md) — The number object’s value expressed as an unsigned `long long`, converted as necessary.
- [unsignedShortValue](uint16value.md) — The number object’s value expressed as an unsigned `short`, converted as necessary.
