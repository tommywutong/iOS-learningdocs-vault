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
doc_path: '/documentation/foundation/nsnumber/description(withlocale:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsnumber/description(withlocale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnumber/description%28withlocale%3A%29.json'
content_hash: 'sha256:dbe75a5591ef9132'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNumber](../nsnumber.md)

# description(withLocale:)

<sub>Instance Method</sub>

Returns a string that represents the contents of the number object for a given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(withLocale locale: Any?) -> String
```

## Parameters

- `locale` — An object containing locale information with which to format the description. Use `nil` if you don’t want the description formatted.

## Return Value

A string that represents the contents of the number object formatted using the locale information in `locale`.

## Discussion

For example, if you have an `NSNumber` object that has the integer value 522, sending it the [- descriptionWithLocale:](<description(withlocale_).md>) message returns the string “522”.

To obtain the string representation, this method invokes `NSString`’s   [initWithFormat:locale:](../nsstring/initwithformat_locale_.md) method, supplying the format based on the type the `NSNumber` object was created with:

| Data Type | Format Specification |
|---|---|
| char | %i |
| double | %0.16g |
| float | %0.7g |
| int | %i |
| long | %li |
| long long | %lli |
| short | %hi |
| unsigned char | %u |
| unsigned int | %u |
| unsigned long | %lu |
| unsigned long long | %llu |
| unsigned short | %hu |

## See Also

### Retrieving String Representations

- [stringValue](stringvalue.md) — The number object’s value expressed as a human-readable string.
