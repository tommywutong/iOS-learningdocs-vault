---
title: Locale.Language.Components
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/language-swift.struct/components
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/components.json'
content_hash: 'sha256:b2b00930930bf4e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Language](../language-swift.struct.md)

# Locale.Language.Components

<sub>Structure</sub>

A type that identifies a language by its various components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Components
```

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a language components instance

- [init(identifier:)](<components/init(identifier_).md>) — Creates a language components instance from a language identifier.
- [init(language:)](<components/init(language_).md>) — Creates a language components instance from an existing language instance.
- [init(languageCode:script:region:)](<components/init(languagecode_script_region_).md>) — Creates a language components instance from a given language code, script, and region.

### Examining language component properties

- [languageCode](components/languagecode.md) — The language code that identifies this language.
- [LanguageCode](../languagecode-swift.struct.md) — An alphabetical code associated with a language.
- [region](components/region.md) — The region used with this language.
- [Region](../region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [script](components/script.md) — The written script used by this language.
- [Script](../script.md) — The written script used with a given language.

## See Also

### Creating a locale by components

- [init(components:)](<../init(components_).md>) — Creates a locale from the given components.
- [Components](../components.md) — A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode:script:languageRegion:)](<../init(languagecode_script_languageregion_).md>) — Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents:)](<../init(languagecomponents_).md>) — Creates a locale from the given language components.
