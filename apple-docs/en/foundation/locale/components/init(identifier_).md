---
title: 'init(identifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/components/init(identifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/components/init(identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/components/init%28identifier%3A%29.json'
content_hash: 'sha256:dbbe5355da050045'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Components](../components.md)

# init(identifier:)

<sub>Initializer</sub>

Creates a locale components instance with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(identifier: String)
```

## Parameters

- `identifier` — A BCP-47 language identifier such as `en-u-nu-thai-ca-buddhist` or an ICU-style identifier such as `en@calendar=buddhist;numbers=thai`.

## See Also

### Creating a locale components instance

- [init(languageCode:script:languageRegion:)](<init(languagecode_script_languageregion_).md>) — Creates a locale components instance with the specified language code, script, and region identifier.
- [init(locale:)](<init(locale_).md>) — Creates a language components instance from an existing locale.
