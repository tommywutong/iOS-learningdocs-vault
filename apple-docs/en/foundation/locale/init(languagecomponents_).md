---
title: 'init(languageComponents:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/init(languagecomponents:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/init(languagecomponents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/init%28languagecomponents%3A%29.json'
content_hash: 'sha256:91c771d4fd3619dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# init(languageComponents:)

<sub>Initializer</sub>

Creates a locale from the given language components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(languageComponents: Locale.Language.Components)
```

## Parameters

- `languageComponents` — A [Components](language-swift.struct/components.md) instance that provides language components that identify a locale.

## See Also

### Creating a locale by components

- [init(components:)](<init(components_).md>) — Creates a locale from the given components.
- [Components](components.md) — A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode:script:languageRegion:)](<init(languagecode_script_languageregion_).md>) — Creates a locale with the specified language code, script, and region identifier.
- [Components](language-swift.struct/components.md) — A type that identifies a language by its various components.
