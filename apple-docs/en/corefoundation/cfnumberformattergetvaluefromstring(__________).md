---
title: 'CFNumberFormatterGetValueFromString(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattergetvaluefromstring(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattergetvaluefromstring(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattergetvaluefromstring%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7ad512017ad9986a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterGetValueFromString(_:_:_:_:_:)

<sub>Function</sub>

Returns a number or value representing a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterGetValueFromString(_ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ numberType: CFNumberType, _ valuePtr: UnsafeMutableRawPointer!) -> Bool
```

## Parameters

- `formatter` — The number formatter to use.

- `string` — The string to parse.

- `rangep` — A reference to a range that specifies the substring of  `string` to be parsed. If `NULL`, the whole string is parsed. Upon return, contains the range of the actual extent of the parse (may be less than the given range).

- `numberType` — The type of value that `valuePtr` references. Valid values are listed in [CFNumberType](cfnumbertype.md).

- `valuePtr` — Upon return, contains a number or value representing the string in the specified format. You are responsible for releasing this value.

## Return Value

`true` if the string was parsed successfully, otherwise `false`.

## See Also

### Formatting Values

- [CFNumberFormatterCreateNumberFromString](<cfnumberformattercreatenumberfromstring(__________).md>) — Returns a number object representing a given string.
- [CFNumberFormatterCreateStringWithNumber](<cfnumberformattercreatestringwithnumber(______).md>) — Returns a string representation of the given number using the specified number formatter.
- [CFNumberFormatterCreateStringWithValue](<cfnumberformattercreatestringwithvalue(________).md>) — Returns a string representation of the given number or value using the specified number formatter.
- [CFNumberFormatterGetDecimalInfoForCurrencyCode](<cfnumberformattergetdecimalinfoforcurrencycode(______).md>) — Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
