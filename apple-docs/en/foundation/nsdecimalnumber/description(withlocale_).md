---
title: 'description(withLocale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/description(withlocale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/description(withlocale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/description%28withlocale%3A%29.json'
content_hash: 'sha256:7f345635df08c38b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# description(withLocale:)

<sub>Instance Method</sub>

Returns a string representation of the decimal number appropriate for the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?) -> String
```

## Parameters

- `locale` — Either an instance of [NSLocale](../nslocale.md) or a dictionary with a string value corresponding to the [NSLocaleDecimalSeparator](../nslocale/key/decimalseparator.md) key.

## Discussion

This is a convenience method for calling the [NSDecimalString](<../nsdecimalstring(____).md>) function.

## See Also

### Accessing the Value

- [decimalValue](decimalvalue.md) — The decimal number’s value, expressed as an [Decimal](../decimal.md) structure.
- [doubleValue](doublevalue.md) — The decimal number’s closest approximate `double` value.
- [objCType](objctype.md) — A C string containing the Objective-C type for the data contained in the decimal number object.
