---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatter/string(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/string(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/string%28from%3A%29.json'
content_hash: 'sha256:044a4bd07c00e2fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# string(from:)

<sub>Instance Method</sub>

Returns a string containing the formatted value of the provided number object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from number: NSNumber) -> String?
```

## Parameters

- `number` — An [NSNumber](../nsnumber.md) object that is parsed to create the returned string object.

## Return Value

A string containing the formatted value of `number` using the receiver’s current settings.

## See Also

### Converting Between Numbers and Strings

- [- getObjectValue:forString:range:error:](<getobjectvalue(__for_range_).md>) — Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [- numberFromString:](<number(from_).md>) — Returns an [NSNumber](../nsnumber.md) object created by parsing a given string.
- [+ localizedStringFromNumber:numberStyle:](<localizedstring(from_number_).md>) — Returns a localized number string with the specified style.
