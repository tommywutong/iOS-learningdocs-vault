---
title: 'init(localized:options:including:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(localized:options:including:)-4cbfv'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(localized:options:including:)-4cbfv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28localized%3Aoptions%3Aincluding%3A%29-4cbfv.json'
content_hash: 'sha256:60658de71195b7eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(localized:options:including:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(localized resource: LocalizedStringResource, options: AttributedString.LocalizationOptions, including scope: KeyPath<AttributeScopes, S.Type>) where S : AttributeScope
```
