---
title: 'lineDirection(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/linedirection(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/linedirection(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/linedirection%28forlanguage%3A%29.json'
content_hash: 'sha256:be45f5d02f1600ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# lineDirection(forLanguage:)

<sub>Type Method</sub>

Returns the direction of the sequence of lines for the specified ISO language code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func lineDirection(forLanguage isoLangCode: String) -> NSLocale.LanguageDirection
```

## Parameters

- `isoLangCode` — The ISO language code.

## Return Value

Returns the direction in which lines appear in the specified language. See [LanguageDirection](languagedirection.md) for possible values. If the appropriate direction can’t be determined [NSLocaleLanguageDirectionUnknown](languagedirection/unknown.md) is returned.

## See Also

### Getting Line and Character Direction for a Language

- [+ characterDirectionForLanguage:](<characterdirection(forlanguage_).md>) — Returns the direction of the sequence of characters in a line for the specified ISO language code.
- [LanguageDirection](languagedirection.md) — The directions that a language may take across a page of text.
