---
title: 'subscript(_:_:_:_:_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:_:_:_:_:)-o61e'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:_:_:_:_:)-o61e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/runs-swift.struct/subscript%28_%3A_%3A_%3A_%3A_%3A%29-o61e.json'
content_hash: 'sha256:3e323858c5258bc6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [Runs](../runs-swift.struct.md)

# subscript(_:_:_:_:_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<T, U, V, W, X>(t: T.Type, u: U.Type, v: V.Type, w: W.Type, x: X.Type) -> AttributedString.Runs.AttributesSlice5<T, U, V, W, X> where T : AttributedStringKey, U : AttributedStringKey, V : AttributedStringKey, W : AttributedStringKey, X : AttributedStringKey, T.Value : Sendable, U.Value : Sendable, V.Value : Sendable, W.Value : Sendable, X.Value : Sendable { get }
```
