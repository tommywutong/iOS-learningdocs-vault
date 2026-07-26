---
title: right
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/right
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/right'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/right.json'
content_hash: 'sha256:ef986ffe59f93c46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# right

<sub>Instance Property</sub>

The right expression of an aggregate expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var right: NSExpression { get }
```

## Discussion

Accessing this property raises an exception if it is not applicable to the expression.

## See Also

### Getting Information About an Expression

- [arguments](arguments.md) — The arguments for the expression.
- [collection](collection.md) — The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [constantValue](constantvalue.md) — The constant value of the expression.
- [expressionType](expressiontype-swift.property.md) — The expression type for the expression.
- [ExpressionType](expressiontype-swift.enum.md) — Defines the possible types of an expression.
- [function](function.md) — The function for the expression.
- [keyPath](keypath.md) — The key path for the expression.
- [operand](operand.md) — The operand for the expression.
- [predicate](predicate.md) — The predicate of a subquery expression.
- [leftExpression](left.md) — The left expression of an aggregate expression.
- [variable](variable.md) — The variable for the expression.
