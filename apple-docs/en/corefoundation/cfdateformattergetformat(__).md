---
title: 'CFDateFormatterGetFormat(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattergetformat(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattergetformat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattergetformat%28_%3A%29.json'
content_hash: 'sha256:ce0b8ee03982aea4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterGetFormat(_:)

<sub>Function</sub>

Returns a format string for the given date formatter object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterGetFormat(_ formatter: CFDateFormatter!) -> CFString!
```

## Parameters

- `formatter` — The date formatter to examine.

## Return Value

The format string for `formatter` as was specified by calling the [CFDateFormatterSetFormat](<cfdateformattersetformat(____).md>) function, or derived from the date formatter’s date or time styles. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting Information About a Date Formatter

- [CFDateFormatterCopyProperty](<cfdateformattercopyproperty(____).md>) — Returns a copy of a date formatter’s value for a given key.
- [CFDateFormatterGetDateStyle](<cfdateformattergetdatestyle(__).md>) — Returns the date style used to create the given date formatter object.
- [CFDateFormatterGetLocale](<cfdateformattergetlocale(__).md>) — Returns the locale object used to create the given date formatter object.
- [CFDateFormatterGetTimeStyle](<cfdateformattergettimestyle(__).md>) — Returns the time style used to create the given date formatter object.
