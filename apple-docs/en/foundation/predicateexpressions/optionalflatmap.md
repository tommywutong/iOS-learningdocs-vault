---
title: PredicateExpressions.OptionalFlatMap
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/optionalflatmap
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/optionalflatmap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/optionalflatmap.json'
content_hash: 'sha256:9cc2a5ff6007757a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.OptionalFlatMap

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OptionalFlatMap<LHS, Wrapped, RHS, Result> where LHS : PredicateExpression, RHS : PredicateExpression, LHS.Output == Wrapped?
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(_:_:)](<optionalflatmap/init(____)-3sqz7.md>)
- [init(_:_:)](<optionalflatmap/init(____)-fnq2.md>)

### Instance Properties

- [transform](optionalflatmap/transform.md)
- [variable](optionalflatmap/variable.md)
- [wrapped](optionalflatmap/wrapped.md)
