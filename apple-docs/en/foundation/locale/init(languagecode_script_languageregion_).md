---
title: 'init(languageCode:script:languageRegion:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/init(languagecode:script:languageregion:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/init(languagecode:script:languageregion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/init%28languagecode%3Ascript%3Alanguageregion%3A%29.json'
content_hash: 'sha256:7e77e3cbdf5feb36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# init(languageCode:script:languageRegion:)

<sub>Initializer</sub>

Creates a locale with the specified language code, script, and region identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(languageCode: Locale.LanguageCode? = nil, script: Locale.Script? = nil, languageRegion: Locale.Region? = nil)
```

## Parameters

- `languageCode` — A language code, typically created from a two- or three-letter language code specified by ISO 639.

- `script` — The script to use for the new locale components instance.

- `languageRegion` — A language region, typically created from a two-letter BCP 47 region subtag like `US`.

## See Also

### Creating a locale by components

- [init(components:)](<init(components_).md>) — Creates a locale from the given components.
- [Components](components.md) — A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageComponents:)](<init(languagecomponents_).md>) — Creates a locale from the given language components.
- [Components](language-swift.struct/components.md) — A type that identifies a language by its various components.
