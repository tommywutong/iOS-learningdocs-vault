---
title: 'CFLocaleGetLanguageLineDirection(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalegetlanguagelinedirection(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalegetlanguagelinedirection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalegetlanguagelinedirection%28_%3A%29.json'
content_hash: 'sha256:e7dd974506e7b806'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleGetLanguageLineDirection(_:)

<sub>Function</sub>

Returns the line direction for the specified ISO language code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleGetLanguageLineDirection(_ isoLangCode: CFString!) -> CFLocaleLanguageDirection
```

## Parameters

- `isoLangCode` — The ISO language code.

## Return Value

The line direction for the language. See [CFLocaleLanguageDirection](cflocalelanguagedirection.md) for possible values. If the appropriate direction can’t be determined, [kCFLocaleLanguageDirectionUnknown](cflocalelanguagedirection/unknown.md) is returned.

## See Also

### Getting Line and Character Direction for a Language

- [CFLocaleGetLanguageCharacterDirection](<cflocalegetlanguagecharacterdirection(__).md>) — Returns the character direction for the specified ISO language code.
