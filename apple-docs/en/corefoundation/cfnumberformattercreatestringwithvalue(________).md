---
title: 'CFNumberFormatterCreateStringWithValue(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattercreatestringwithvalue(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattercreatestringwithvalue(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattercreatestringwithvalue%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b65fe97c4eee5761'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterCreateStringWithValue(_:_:_:_:)

<sub>Function</sub>

Returns a string representation of the given number or value using the specified number formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterCreateStringWithValue(_ allocator: CFAllocator!, _ formatter: CFNumberFormatter!, _ numberType: CFNumberType, _ valuePtr: UnsafeRawPointer!) -> CFString!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `formatter` — The number formatter to use.

- `numberType` — The type of value that `valuePtr` references. Valid values are listed in [CFNumberType](cfnumbertype.md).

- `valuePtr` — A pointer to the value to be converted.

## Return Value

A new string that represents the given number or value formatted by `formatter`. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Formatting Values

- [CFNumberFormatterCreateNumberFromString](<cfnumberformattercreatenumberfromstring(__________).md>) — Returns a number object representing a given string.
- [CFNumberFormatterCreateStringWithNumber](<cfnumberformattercreatestringwithnumber(______).md>) — Returns a string representation of the given number using the specified number formatter.
- [CFNumberFormatterGetDecimalInfoForCurrencyCode](<cfnumberformattergetdecimalinfoforcurrencycode(______).md>) — Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
- [CFNumberFormatterGetValueFromString](<cfnumberformattergetvaluefromstring(__________).md>) — Returns a number or value representing a given string.
