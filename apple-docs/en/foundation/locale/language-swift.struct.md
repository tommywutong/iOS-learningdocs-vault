---
title: Locale.Language
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/language-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct.json'
content_hash: 'sha256:2e677d77884e90c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Language

<sub>Structure</sub>

A type that represents a language, as used in a locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Language
```

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a language

- [init(identifier:)](<language-swift.struct/init(identifier_).md>) — Creates a language from an identifier.
- [init(components:)](<language-swift.struct/init(components_).md>) — Creates a language from its component values.
- [Components](language-swift.struct/components.md) — A type that identifies a language by its various components.
- [init(languageCode:script:region:)](<language-swift.struct/init(languagecode_script_region_).md>) — Creates a language from a given language code, script, and region.

### Examining language properties

- [languageCode](language-swift.struct/languagecode.md) — The language code that identifies the language.
- [LanguageCode](languagecode-swift.struct.md) — An alphabetical code associated with a language.
- [region](language-swift.struct/region.md) — The region used with the language.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [script](language-swift.struct/script.md) — The written script of the language.
- [Script](script.md) — The written script used with a given language.
- [characterDirection](language-swift.struct/characterdirection.md) — The ordering of characters within a line.
- [LanguageDirection](languagedirection.md) — An alias for the standard set of language directions.

### Examining language relationships

- [parent](language-swift.struct/parent.md) — The parent language of this language, if available.
- [hasCommonParent(with:)](<language-swift.struct/hascommonparent(with_).md>) — Returns a Boolean value that indicates if the given language shares a common parent with this language.
- [isEquivalent(to:)](<language-swift.struct/isequivalent(to_).md>) — Returns a Boolean value that indicates whether this language and another language are equivalent after expanding missing components.

### Using system languages

- [systemLanguages](language-swift.struct/systemlanguages.md) — An array of the system’s supported languages.

### Instance Properties

- [lineLayoutDirection](language-swift.struct/linelayoutdirection.md) — Ordering of lines within a page. For example, top-to-bottom for English; right-to-left for Mongolian in the Mongolian Script
- [maximalIdentifier](language-swift.struct/maximalidentifier.md) — Returns a BCP-47 identifier that always includes the script: “zh-Hant-TW”, “en-Latn-US”
- [minimalIdentifier](language-swift.struct/minimalidentifier.md) — Returns a BCP-47 identifier in a minimalist form. Script and region may be omitted. For example, “zh-TW”, “en”

## See Also

### Getting language components

- [language](language-swift.property.md) — The language of a locale.
