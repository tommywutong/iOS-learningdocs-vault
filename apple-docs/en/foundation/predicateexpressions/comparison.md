---
title: PredicateExpressions.Comparison
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/comparison
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/comparison'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/comparison.json'
content_hash: 'sha256:e7424bb222d920e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.Comparison

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Comparison<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Comparable, LHS.Output == RHS.Output
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(lhs:rhs:op:)](<comparison/init(lhs_rhs_op_).md>)

### Instance Properties

- [lhs](comparison/lhs.md)
- [op](comparison/op.md)
- [rhs](comparison/rhs.md)
