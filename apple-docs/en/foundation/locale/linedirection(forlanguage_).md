---
title: 'lineDirection(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 8.0+（16.0 起废弃）, macOS 10.10+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+, watchOS 2.0+（9.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/locale/linedirection(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/linedirection(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/linedirection%28forlanguage%3A%29.json'
content_hash: 'sha256:5614493b3758e0ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# lineDirection(forLanguage:)

<sub>Type Method</sub>

Returns the line direction for a specified language code.

> [!warning] Deprecated
> Use `Locale.Language(identifier:).lineLayoutDirection`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func lineDirection(forLanguage isoLangCode: String) -> Locale.LanguageDirection
```

## See Also

### Getting line and character direction for a language

- [characterDirection(forLanguage:)](<characterdirection(forlanguage_).md>) — Returns the character direction for a specified language code. _(deprecated)_
- [LanguageDirection](languagedirection.md) — An alias for the standard set of language directions.
- [LanguageDirection](../nslocale/languagedirection.md) — The directions that a language may take across a page of text.
