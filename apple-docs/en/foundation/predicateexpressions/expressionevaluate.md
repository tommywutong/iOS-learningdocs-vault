---
title: PredicateExpressions.ExpressionEvaluate
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/expressionevaluate
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/expressionevaluate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/expressionevaluate.json'
content_hash: 'sha256:c544a546d5107535'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.ExpressionEvaluate

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ExpressionEvaluate<Transformation, each Input, Output> where Transformation : PredicateExpression, repeat each Input : PredicateExpression, Transformation.Output == Expression<repeat (each Input).Output, Output>
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(expression:input:)](<expressionevaluate/init(expression_input_).md>)

### Instance Properties

- [expression](expressionevaluate/expression.md)
- [input](expressionevaluate/input.md)
