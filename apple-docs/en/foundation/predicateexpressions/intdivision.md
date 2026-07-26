---
title: PredicateExpressions.IntDivision
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/intdivision
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/intdivision'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/intdivision.json'
content_hash: 'sha256:95d148349de04909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.IntDivision

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IntDivision<LHS, RHS> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output : BinaryInteger, LHS.Output == RHS.Output
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(lhs:rhs:)](<intdivision/init(lhs_rhs_).md>)

### Instance Properties

- [lhs](intdivision/lhs.md)
- [rhs](intdivision/rhs.md)
