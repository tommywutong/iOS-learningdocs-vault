---
title: 'init(language:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/language-swift.struct/components/init(language:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/language-swift.struct/components/init(language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/language-swift.struct/components/init%28language%3A%29.json'
content_hash: 'sha256:02401ea979c5ef3c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Locale](../../../locale.md) · [Language](../../language-swift.struct.md) · [Components](../components.md)

# init(language:)

<sub>Initializer</sub>

Creates a language components instance from an existing language instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(language: Locale.Language)
```

## Parameters

- `language` — A [Language](../../language-swift.struct.md) instance. This initializer copies over the language code, script, and region from the provided language.

## See Also

### Creating a language components instance

- [init(identifier:)](<init(identifier_).md>) — Creates a language components instance from a language identifier.
- [init(languageCode:script:region:)](<init(languagecode_script_region_).md>) — Creates a language components instance from a given language code, script, and region.
