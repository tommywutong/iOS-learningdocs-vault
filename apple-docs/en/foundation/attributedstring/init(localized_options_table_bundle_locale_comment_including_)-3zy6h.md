---
title: 'init(localized:options:table:bundle:locale:comment:including:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(localized:options:table:bundle:locale:comment:including:)-3zy6h'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(localized:options:table:bundle:locale:comment:including:)-3zy6h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28localized%3Aoptions%3Atable%3Abundle%3Alocale%3Acomment%3Aincluding%3A%29-3zy6h.json'
content_hash: 'sha256:10f9973842ca09fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(localized:options:table:bundle:locale:comment:including:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(localized key: String.LocalizationValue, options: AttributedString.LocalizationOptions, table: String? = nil, bundle: Bundle? = nil, locale: Locale? = nil, comment: StaticString? = nil, including scope: KeyPath<AttributeScopes, S.Type>) where S : AttributeScope
```
