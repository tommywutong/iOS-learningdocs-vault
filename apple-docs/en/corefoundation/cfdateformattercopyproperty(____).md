---
title: 'CFDateFormatterCopyProperty(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattercopyproperty(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattercopyproperty(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattercopyproperty%28_%3A_%3A%29.json'
content_hash: 'sha256:d26075e55439c7f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterCopyProperty(_:_:)

<sub>Function</sub>

Returns a copy of a date formatter’s value for a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterCopyProperty(_ formatter: CFDateFormatter!, _ key: CFDateFormatterKey!) -> CFTypeRef!
```

## Parameters

- `formatter` — The date formatter to examine.

- `key` — The property key for the value to obtain. See [Date Formatter Property Keys](date-formatter-property-keys.md) for a description of possible values for this parameter.

## Return Value

A CFType object that is a copy of the property value for `key`, or `NULL` if there is no value specified for `key`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting Information About a Date Formatter

- [CFDateFormatterGetDateStyle](<cfdateformattergetdatestyle(__).md>) — Returns the date style used to create the given date formatter object.
- [CFDateFormatterGetFormat](<cfdateformattergetformat(__).md>) — Returns a format string for the given date formatter object.
- [CFDateFormatterGetLocale](<cfdateformattergetlocale(__).md>) — Returns the locale object used to create the given date formatter object.
- [CFDateFormatterGetTimeStyle](<cfdateformattergettimestyle(__).md>) — Returns the time style used to create the given date formatter object.
