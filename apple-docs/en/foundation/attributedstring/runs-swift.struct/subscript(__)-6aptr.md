---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:)-6aptr'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:)-6aptr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/runs-swift.struct/subscript%28_%3A%29-6aptr.json'
content_hash: 'sha256:806073de8cf6e2e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [Runs](../runs-swift.struct.md)

# subscript(_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<T>(keyPath: KeyPath<AttributeDynamicLookup, T>) -> AttributedString.Runs.AttributesSlice1<T> where T : AttributedStringKey, T.Value : Sendable { get }
```
