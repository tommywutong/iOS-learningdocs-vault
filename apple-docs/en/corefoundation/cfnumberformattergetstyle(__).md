---
title: 'CFNumberFormatterGetStyle(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattergetstyle(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattergetstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattergetstyle%28_%3A%29.json'
content_hash: 'sha256:fac41773649c96bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterGetStyle(_:)

<sub>Function</sub>

Returns the number style used to create the given number formatter object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterGetStyle(_ formatter: CFNumberFormatter!) -> CFNumberFormatterStyle
```

## Parameters

- `formatter` — The number formatter to examine.

## Return Value

The number style used to create `formatter`.

## See Also

### Examining a Number Formatter

- [CFNumberFormatterCopyProperty](<cfnumberformattercopyproperty(____).md>) — Returns a copy of a number formatter’s value for a given key.
- [CFNumberFormatterGetFormat](<cfnumberformattergetformat(__).md>) — Returns a format string for the given number formatter object.
- [CFNumberFormatterGetLocale](<cfnumberformattergetlocale(__).md>) — Returns the locale object used to create the given number formatter object.
