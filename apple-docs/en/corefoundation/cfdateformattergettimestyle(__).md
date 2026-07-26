---
title: 'CFDateFormatterGetTimeStyle(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattergettimestyle(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattergettimestyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattergettimestyle%28_%3A%29.json'
content_hash: 'sha256:4ea08dca9817a2da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterGetTimeStyle(_:)

<sub>Function</sub>

Returns the time style used to create the given date formatter object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterGetTimeStyle(_ formatter: CFDateFormatter!) -> CFDateFormatterStyle
```

## Parameters

- `formatter` — The date formatter to examine.

## Return Value

The time style used to create `formatter`.

## See Also

### Getting Information About a Date Formatter

- [CFDateFormatterCopyProperty](<cfdateformattercopyproperty(____).md>) — Returns a copy of a date formatter’s value for a given key.
- [CFDateFormatterGetDateStyle](<cfdateformattergetdatestyle(__).md>) — Returns the date style used to create the given date formatter object.
- [CFDateFormatterGetFormat](<cfdateformattergetformat(__).md>) — Returns a format string for the given date formatter object.
- [CFDateFormatterGetLocale](<cfdateformattergetlocale(__).md>) — Returns the locale object used to create the given date formatter object.
