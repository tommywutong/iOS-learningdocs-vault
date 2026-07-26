---
title: 'attributeChanged(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/attributeinvalidationcondition/attributechanged(_:)-1vgwv'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/attributeinvalidationcondition/attributechanged(_:)-1vgwv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/attributeinvalidationcondition/attributechanged%28_%3A%29-1vgwv.json'
content_hash: 'sha256:d082bc096fecb716'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [AttributeInvalidationCondition](../attributeinvalidationcondition.md)

# attributeChanged(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func attributeChanged<T>(_ key: KeyPath<AttributeDynamicLookup, T>) -> AttributedString.AttributeInvalidationCondition where T : AttributedStringKey
```
