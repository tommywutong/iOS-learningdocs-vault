---
title: 'CFNumberFormatterGetFormat(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattergetformat(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattergetformat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattergetformat%28_%3A%29.json'
content_hash: 'sha256:31e57bce300022ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterGetFormat(_:)

<sub>Function</sub>

Returns a format string for the given number formatter object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterGetFormat(_ formatter: CFNumberFormatter!) -> CFString!
```

## Parameters

- `formatter` — The number formatter to examine.

## Return Value

The format string for `formatter` as was specified by calling the [CFNumberFormatterSetFormat](<cfnumberformattersetformat(____).md>) function, or derived from the number formatter’s style. See [Creating and Using CFNumberFormatter Objects](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/dfCreatingCFNumberFormatters.html#//apple_ref/doc/uid/TP40002342) for more information. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a Number Formatter

- [CFNumberFormatterCopyProperty](<cfnumberformattercopyproperty(____).md>) — Returns a copy of a number formatter’s value for a given key.
- [CFNumberFormatterGetLocale](<cfnumberformattergetlocale(__).md>) — Returns the locale object used to create the given number formatter object.
- [CFNumberFormatterGetStyle](<cfnumberformattergetstyle(__).md>) — Returns the number style used to create the given number formatter object.
