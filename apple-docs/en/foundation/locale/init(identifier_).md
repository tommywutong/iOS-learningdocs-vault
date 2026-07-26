---
title: 'init(identifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/locale/init(identifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/locale/init(identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/init%28identifier%3A%29.json'
content_hash: 'sha256:e5804f8cdd665173'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# init(identifier:)

<sub>Initializer</sub>

Creates a locale with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(identifier: String)
```

## Parameters

- `identifier` — A BCP-47 language identifier such as `en_US` or `en-u-nu-thai-ca-buddhist`, or an ICU-style identifier such as `en@calendar=buddhist;numbers=thai`.
