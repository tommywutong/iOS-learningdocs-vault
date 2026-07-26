---
title: preferredLanguages
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/preferredlanguages
source_url: 'https://developer.apple.com/documentation/foundation/locale/preferredlanguages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/preferredlanguages.json'
content_hash: 'sha256:1872f110c68c5606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# preferredLanguages

<sub>Type Property</sub>

A list of the user’s preferred languages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var preferredLanguages: [String] { get }
```

## Discussion

> [!note] Note
> [Bundle](../bundle.md) is responsible for determining the language that your application will run in, based on the result of this API and combined with the languages your application supports.
