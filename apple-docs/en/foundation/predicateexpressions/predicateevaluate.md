---
title: PredicateExpressions.PredicateEvaluate
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.0+, watchOS 10.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/predicateevaluate
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/predicateevaluate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/predicateevaluate.json'
content_hash: 'sha256:d064ba61a468435d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.PredicateEvaluate

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PredicateEvaluate<Condition, each Input> where Condition : PredicateExpression, repeat each Input : PredicateExpression, Condition.Output == Predicate<repeat (each Input).Output>
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(predicate:input:)](<predicateevaluate/init(predicate_input_).md>)

### Instance Properties

- [input](predicateevaluate/input.md)
- [predicate](predicateevaluate/predicate.md)
