---
title: collection
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/collection
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/collection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/collection.json'
content_hash: 'sha256:750c7eec86f88415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# collection

<sub>Instance Property</sub>

The collection of expressions in an aggregate expression, or the collection element of a subquery expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var collection: Any { get }
```

## Discussion

Accessing this property raises an exception if it is not applicable to the expression.

## See Also

### Getting Information About an Expression

- [arguments](arguments.md) — The arguments for the expression.
- [constantValue](constantvalue.md) — The constant value of the expression.
- [expressionType](expressiontype-swift.property.md) — The expression type for the expression.
- [ExpressionType](expressiontype-swift.enum.md) — Defines the possible types of an expression.
- [function](function.md) — The function for the expression.
- [keyPath](keypath.md) — The key path for the expression.
- [operand](operand.md) — The operand for the expression.
- [predicate](predicate.md) — The predicate of a subquery expression.
- [leftExpression](left.md) — The left expression of an aggregate expression.
- [rightExpression](right.md) — The right expression of an aggregate expression.
- [variable](variable.md) — The variable for the expression.
