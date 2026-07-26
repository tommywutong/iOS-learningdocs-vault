---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-7vcf2'
source_url: 'https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-7vcf2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedynamiclookup/subscript%28dynamicmember%3A%29-7vcf2.json'
content_hash: 'sha256:79dd0153a48ea127'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeDynamicLookup](../attributedynamiclookup.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.AccessibilityAttributes, T>) -> T where T : AttributedStringKey { get }
```
