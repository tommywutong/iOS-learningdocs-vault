---
title: 'CFNumberFormatterCreateNumberFromString(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattercreatenumberfromstring(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattercreatenumberfromstring(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattercreatenumberfromstring%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:6cbe8cf6b2ee8d66'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterCreateNumberFromString(_:_:_:_:_:)

<sub>Function</sub>

Returns a number object representing a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterCreateNumberFromString(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ options: CFOptionFlags) -> CFNumber!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `formatter` — The number formatter to use.

- `string` — The string to parse.

- `rangep` — A reference to a range that specifies the substring of  `string` to be parsed. If `NULL`, the whole string is parsed. On return, contains the range of the actual extent of the parse (may be less than the given range).

- `options` — Specifies various configuration options to change the behavior of the parse. Currently, [kCFNumberFormatterParseIntegersOnly](cfnumberformatteroptionflags/parseintegersonly.md) is the only possible value for this parameter.

## Return Value

A new number that represents the given string. Returns `NULL` if there was a problem creating the number. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Formatting Values

- [CFNumberFormatterCreateStringWithNumber](<cfnumberformattercreatestringwithnumber(______).md>) — Returns a string representation of the given number using the specified number formatter.
- [CFNumberFormatterCreateStringWithValue](<cfnumberformattercreatestringwithvalue(________).md>) — Returns a string representation of the given number or value using the specified number formatter.
- [CFNumberFormatterGetDecimalInfoForCurrencyCode](<cfnumberformattergetdecimalinfoforcurrencycode(______).md>) — Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
- [CFNumberFormatterGetValueFromString](<cfnumberformattergetvaluefromstring(__________).md>) — Returns a number or value representing a given string.
