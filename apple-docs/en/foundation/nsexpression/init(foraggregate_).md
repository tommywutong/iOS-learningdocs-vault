---
title: 'init(forAggregate:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(foraggregate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(foraggregate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28foraggregate%3A%29.json'
content_hash: 'sha256:2519d12e1b84b936'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(forAggregate:)

<sub>Initializer</sub>

Creates an aggregate expression for a specified collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forAggregate subexpressions: [NSExpression])
```

## Parameters

- `subexpressions` — A collection object (an instance of `NSArray`, `NSSet`, or `NSDictionary`) that contains further expressions.

## Return Value

A new expression that contains the expressions in `collection`.

## See Also

### Creating a Collection Expression

- [+ expressionForUnionSet:with:](<init(forunionset_with_).md>) — Creates an expression object that represents the union of a specified set and collection.
- [+ expressionForIntersectSet:with:](<init(forintersectset_with_).md>) — Creates an expression object that represents the intersection of a specified set and collection.
- [+ expressionForMinusSet:with:](<init(forminusset_with_).md>) — Creates an expression object that represents the subtraction of a specified collection from a specified set.
