---
title: 'init(forUnionSet:with:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(forunionset:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(forunionset:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28forunionset%3Awith%3A%29.json'
content_hash: 'sha256:bc0c299079717897'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(forUnionSet:with:)

<sub>Initializer</sub>

Creates an expression object that represents the union of a specified set and collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forUnionSet left: NSExpression, with right: NSExpression)
```

## Parameters

- `left` — An expression that evaluates to an `NSSet` object.

- `right` — An expression that evaluates to a collection object (an instance of `NSArray`, `NSSet`, or `NSDictionary`).

## Return Value

An new `NSExpression` object that represents the union of `left` and `right`.

## See Also

### Creating a Collection Expression

- [+ expressionForAggregate:](<init(foraggregate_).md>) — Creates an aggregate expression for a specified collection.
- [+ expressionForIntersectSet:with:](<init(forintersectset_with_).md>) — Creates an expression object that represents the intersection of a specified set and collection.
- [+ expressionForMinusSet:with:](<init(forminusset_with_).md>) — Creates an expression object that represents the subtraction of a specified collection from a specified set.
