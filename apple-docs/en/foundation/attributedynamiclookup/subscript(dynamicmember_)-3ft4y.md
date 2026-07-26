---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-3ft4y'
source_url: 'https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-3ft4y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedynamiclookup/subscript%28dynamicmember%3A%29-3ft4y.json'
content_hash: 'sha256:2b26ec84c6f4de91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeDynamicLookup](../attributedynamiclookup.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.SpeechAttributes, T>) -> T where T : AttributedStringKey { get }
```
