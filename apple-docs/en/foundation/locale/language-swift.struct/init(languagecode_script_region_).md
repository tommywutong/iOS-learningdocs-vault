---
title: 'init(languageCode:script:region:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/language-swift.struct/init(languagecode:script:region:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/init(languagecode:script:region:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/init%28languagecode%3Ascript%3Aregion%3A%29.json'
content_hash: 'sha256:184e503db4bd19fa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Language](../language-swift.struct.md)

# init(languageCode:script:region:)

<sub>Initializer</sub>

Creates a language from a given language code, script, and region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(languageCode: Locale.LanguageCode? = nil, script: Locale.Script? = nil, region: Locale.Region? = nil)
```

## Parameters

- `languageCode` — A language code, typically created from a two- or three-letter language code specified by ISO 639.

- `script` — The script to use for the new locale components instance.

- `region` — The region to use for the new components instance.

## See Also

### Creating a language

- [init(identifier:)](<init(identifier_).md>) — Creates a language from an identifier.
- [init(components:)](<init(components_).md>) — Creates a language from its component values.
- [Components](components.md) — A type that identifies a language by its various components.
