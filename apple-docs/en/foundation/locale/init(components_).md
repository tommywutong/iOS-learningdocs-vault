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
doc_path: '/documentation/foundation/locale/init(components:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/init(components:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/init%28components%3A%29.json'
content_hash: 'sha256:9c84b7dbebd2637e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# init(components:)

<sub>Initializer</sub>

Creates a locale from the given components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(components: Locale.Components)
```

## Parameters

- `components` — A [Components](components.md) instance that provides the components to create a customized locale.

## Discussion

Use this initializer to create a locale with a unique combination of components, beyond the defaults provided by a language and country code.

For example, you can create a [Components](components.md) instance that uses UK language conventions, but US regional conventions for traits like currency and measurement. You then use the components to create a new [Locale](../locale.md) instance, like this:

```swift
var components = Locale.Components(languageCode: "en", languageRegion: "GB")
components.region = Locale.Region("US")
let en_GB_US = Locale(components: components)
```

## See Also

### Creating a locale by components

- [Components](components.md) — A type that represents the components of a locale, for use when creating a locale with specific overrides.
- [init(languageCode:script:languageRegion:)](<init(languagecode_script_languageregion_).md>) — Creates a locale with the specified language code, script, and region identifier.
- [init(languageComponents:)](<init(languagecomponents_).md>) — Creates a locale from the given language components.
- [Components](language-swift.struct/components.md) — A type that identifies a language by its various components.
