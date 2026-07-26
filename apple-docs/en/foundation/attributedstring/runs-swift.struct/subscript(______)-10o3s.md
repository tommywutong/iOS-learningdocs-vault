---
title: 'subscript(_:_:_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:_:_:)-10o3s'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:_:_:)-10o3s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/runs-swift.struct/subscript%28_%3A_%3A_%3A%29-10o3s.json'
content_hash: 'sha256:336518dda9f7fbe3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [Runs](../runs-swift.struct.md)

# subscript(_:_:_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<T, U, V>(t: KeyPath<AttributeDynamicLookup, T>, u: KeyPath<AttributeDynamicLookup, U>, v: KeyPath<AttributeDynamicLookup, V>) -> AttributedString.Runs.AttributesSlice3<T, U, V> where T : AttributedStringKey, U : AttributedStringKey, V : AttributedStringKey, T.Value : Sendable, U.Value : Sendable, V.Value : Sendable { get }
```
