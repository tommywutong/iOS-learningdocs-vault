---
title: PredicateExpressions.UnaryMinus
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/unaryminus
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/unaryminus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/unaryminus.json'
content_hash: 'sha256:d6429fdb2c3bae6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.UnaryMinus

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UnaryMinus<Wrapped> where Wrapped : PredicateExpression, Wrapped.Output : SignedNumeric
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(_:)](<unaryminus/init(__).md>)

### Instance Properties

- [wrapped](unaryminus/wrapped.md)
