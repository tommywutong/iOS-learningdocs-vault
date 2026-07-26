---
title: PredicateExpressions.Arithmetic
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/arithmetic
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/arithmetic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/arithmetic.json'
content_hash: 'sha256:91c491121e33d1af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.Arithmetic

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Arithmetic<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : Numeric, LHS.Output == RHS.Output
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(lhs:rhs:op:)](<arithmetic/init(lhs_rhs_op_).md>)

### Instance Properties

- [lhs](arithmetic/lhs.md)
- [op](arithmetic/op.md)
- [rhs](arithmetic/rhs.md)
