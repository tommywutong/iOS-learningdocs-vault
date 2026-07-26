---
title: 'CFNumberFormatterCopyProperty(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattercopyproperty(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattercopyproperty(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattercopyproperty%28_%3A_%3A%29.json'
content_hash: 'sha256:18023db1b34b20c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterCopyProperty(_:_:)

<sub>Function</sub>

Returns a copy of a number formatter’s value for a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterCopyProperty(_ formatter: CFNumberFormatter!, _ key: CFNumberFormatterKey!) -> CFTypeRef!
```

## Parameters

- `formatter` — The number formatter to examine.

- `key` — A property key. See [Number Formatter Property Keys](number-formatter-property-keys.md) for valid values.

## Return Value

A `CFType` object that is a copy of the property value for `key`. Returns `NULL` if there is no value specified for `key`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Examining a Number Formatter

- [CFNumberFormatterGetFormat](<cfnumberformattergetformat(__).md>) — Returns a format string for the given number formatter object.
- [CFNumberFormatterGetLocale](<cfnumberformattergetlocale(__).md>) — Returns the locale object used to create the given number formatter object.
- [CFNumberFormatterGetStyle](<cfnumberformattergetstyle(__).md>) — Returns the number style used to create the given number formatter object.
