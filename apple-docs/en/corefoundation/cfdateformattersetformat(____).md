---
title: 'CFDateFormatterSetFormat(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattersetformat(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattersetformat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattersetformat%28_%3A_%3A%29.json'
content_hash: 'sha256:da1f738f46b8dcd2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterSetFormat(_:_:)

<sub>Function</sub>

Sets the format string of the given date formatter to the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterSetFormat(_ formatter: CFDateFormatter!, _ formatString: CFString!)
```

## Parameters

- `formatter` — The date formatter to modify.

- `formatString` — The format string for `formatter`. The syntax of this string is defined by [Unicode Technical Standard #35](http://www.unicode.org/reports/tr35/tr35-31/tr35-dates.html#Date_Format_Patterns)..

## Discussion

The format string may override other properties previously set using other functions. If this function is not called, the default value of the format string is derived from the date formatter’s date and time styles.

## See Also

### Configuring a Date Formatter

- [CFDateFormatterSetProperty](<cfdateformattersetproperty(______).md>) — Sets a date formatter property using a key-value pair.
