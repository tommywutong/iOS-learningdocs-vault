---
title: 'characterDirection(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 8.0+（16.0 起废弃）, macOS 10.10+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+, watchOS 2.0+（9.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/locale/characterdirection(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/characterdirection(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/characterdirection%28forlanguage%3A%29.json'
content_hash: 'sha256:d24a0db95d7ec5f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# characterDirection(forLanguage:)

<sub>Type Method</sub>

Returns the character direction for a specified language code.

> [!warning] Deprecated
> Use `Locale.Language(identifier:).characterDirection`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func characterDirection(forLanguage isoLangCode: String) -> Locale.LanguageDirection
```

## See Also

### Getting line and character direction for a language

- [lineDirection(forLanguage:)](<linedirection(forlanguage_).md>) — Returns the line direction for a specified language code. _(deprecated)_
- [LanguageDirection](languagedirection.md) — An alias for the standard set of language directions.
- [LanguageDirection](../nslocale/languagedirection.md) — The directions that a language may take across a page of text.
