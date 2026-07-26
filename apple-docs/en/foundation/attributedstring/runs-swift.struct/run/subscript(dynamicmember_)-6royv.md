---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/runs-swift.struct/run/subscript(dynamicmember:)-6royv'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.struct/run/subscript(dynamicmember:)-6royv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/runs-swift.struct/run/subscript%28dynamicmember%3A%29-6royv.json'
content_hash: 'sha256:3f99b7501c0c65bc'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [AttributedString](../../../attributedstring.md) · [Runs](../../runs-swift.struct.md) · [Run](../run.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get }
```
