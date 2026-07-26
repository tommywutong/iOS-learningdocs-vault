---
title: 'CFNumberFormatterGetLocale(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattergetlocale(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattergetlocale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattergetlocale%28_%3A%29.json'
content_hash: 'sha256:a6dd0e9fc3ee9b9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterGetLocale(_:)

<sub>Function</sub>

Returns the locale object used to create the given number formatter object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterGetLocale(_ formatter: CFNumberFormatter!) -> CFLocale!
```

## Parameters

- `formatter` — The number formatter to examine.

## Return Value

The locale used to create `formatter`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a Number Formatter

- [CFNumberFormatterCopyProperty](<cfnumberformattercopyproperty(____).md>) — Returns a copy of a number formatter’s value for a given key.
- [CFNumberFormatterGetFormat](<cfnumberformattergetformat(__).md>) — Returns a format string for the given number formatter object.
- [CFNumberFormatterGetStyle](<cfnumberformattergetstyle(__).md>) — Returns the number style used to create the given number formatter object.
