---
title: PredicateExpressions.CollectionRangeSubscript
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/collectionrangesubscript
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/collectionrangesubscript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/collectionrangesubscript.json'
content_hash: 'sha256:b392e9a22406b904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.CollectionRangeSubscript

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CollectionRangeSubscript<Wrapped, Range> where Wrapped : PredicateExpression, Range : PredicateExpression, Wrapped.Output : Collection, Range.Output == Range<Wrapped.Output.Index>
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(wrapped:range:)](<collectionrangesubscript/init(wrapped_range_).md>)

### Instance Properties

- [range](collectionrangesubscript/range.md)
- [wrapped](collectionrangesubscript/wrapped.md)
