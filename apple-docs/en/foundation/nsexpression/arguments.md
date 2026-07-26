---
title: arguments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/arguments
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/arguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/arguments.json'
content_hash: 'sha256:082de6ad3c6a7876'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# arguments

<sub>Instance Property</sub>

The arguments for the expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var arguments: [NSExpression]? { get }
```

## Discussion

An expression’s arguments is the array of expressions that will be passed as parameters during invocation of the selector on the operand of a function expression.

Accessing this property raises an exception if it is not applicable to the expression.

## See Also

### Getting Information About an Expression

- [collection](collection.md) — The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
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
