---
title: PredicateExpressions.CollectionIndexSubscript
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/collectionindexsubscript
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/collectionindexsubscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/collectionindexsubscript.json'
content_hash: 'sha256:dab3ddbd0a15152a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.CollectionIndexSubscript

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CollectionIndexSubscript<Wrapped, Index> where Wrapped : PredicateExpression, Index : PredicateExpression, Wrapped.Output : Collection, Index.Output == Wrapped.Output.Index
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(wrapped:index:)](<collectionindexsubscript/init(wrapped_index_).md>)

### Instance Properties

- [index](collectionindexsubscript/index.md)
- [wrapped](collectionindexsubscript/wrapped.md)
