---
title: 'init(components:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/language-swift.struct/init(components:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/init(components:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/init%28components%3A%29.json'
content_hash: 'sha256:ea0649e54322727c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Language](../language-swift.struct.md)

# init(components:)

<sub>Initializer</sub>

Creates a language from its component values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(components: Locale.Language.Components)
```

## Parameters

- `components` — A [Components](components.md) instance that provides a custom language code, region, and script for the new [Language](../language-swift.struct.md) instance.

## See Also

### Creating a language

- [init(identifier:)](<init(identifier_).md>) — Creates a language from an identifier.
- [Components](components.md) — A type that identifies a language by its various components.
- [init(languageCode:script:region:)](<init(languagecode_script_region_).md>) — Creates a language from a given language code, script, and region.
