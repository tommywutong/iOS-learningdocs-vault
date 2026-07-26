---
title: 'number(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatter/number(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/number(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/number%28from%3A%29.json'
content_hash: 'sha256:ac486b49fa5e1c47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# number(from:)

<sub>Instance Method</sub>

Returns an [NSNumber](../nsnumber.md) object created by parsing a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func number(from string: String) -> NSNumber?
```

## Parameters

- `string` — An [NSString](../nsstring.md) object that is parsed to generate the returned number object.

## Return Value

An [NSNumber](../nsnumber.md) object created by parsing `string` using the receiver’s format, or `nil` if no single number could be parsed.

## Discussion

If a string contains any characters other than numerical digits or locale-appropriate group or decimal separators, parsing will fail.

Any leading or trailing space separator characters in a string are ignored. For example, the strings “ 5”, “5 “, and “5” all produce the number `5`.

## See Also

### Converting Between Numbers and Strings

- [- getObjectValue:forString:range:error:](<getobjectvalue(__for_range_).md>) — Returns by reference a cell-content object after creating it from a range of characters in a given string.
- [- stringFromNumber:](<string(from_).md>) — Returns a string containing the formatted value of the provided number object.
- [+ localizedStringFromNumber:numberStyle:](<localizedstring(from_number_).md>) — Returns a localized number string with the specified style.
