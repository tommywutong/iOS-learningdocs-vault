---
title: 'subscript(_:_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:_:)-3taux'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.struct/subscript(_:_:)-3taux'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/runs-swift.struct/subscript%28_%3A_%3A%29-3taux.json'
content_hash: 'sha256:77720e4da3ede187'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [Runs](../runs-swift.struct.md)

# subscript(_:_:)

<sub>Instance Subscript</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<T, U>(t: T.Type, u: U.Type) -> AttributedString.Runs.AttributesSlice2<T, U> where T : AttributedStringKey, U : AttributedStringKey, T.Value : Sendable, U.Value : Sendable { get }
```
