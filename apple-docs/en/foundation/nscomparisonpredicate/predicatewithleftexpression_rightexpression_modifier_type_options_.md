---
title: 'predicateWithLeftExpression:rightExpression:modifier:type:options:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscomparisonpredicate/predicatewithleftexpression:rightexpression:modifier:type:options:'
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/predicatewithleftexpression:rightexpression:modifier:type:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/predicatewithleftexpression%3Arightexpression%3Amodifier%3Atype%3Aoptions%3A.json'
content_hash: 'sha256:f5fcce805c2ba8c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# predicateWithLeftExpression:rightExpression:modifier:type:options:

<sub>Type Method</sub>

Creates and returns a predicate of a given type formed by combining given left and right expressions using a given modifier and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSComparisonPredicate *) predicateWithLeftExpression:(NSExpression *) lhs rightExpression:(NSExpression *) rhs modifier:(NSComparisonPredicateModifier) modifier type:(NSPredicateOperatorType) type options:(NSComparisonPredicateOptions) options;
```

## Parameters

- `lhs` — The left hand expression.

- `rhs` — The right hand expression.

- `modifier` — The modifier to apply.

- `type` — The predicate operator type.

- `options` — The options to apply (see [Options](options-swift.struct.md)). For no options, pass `0`.

## Return Value

A new predicate of type `type` formed by combining the given left and right expressions using the `modifier` and `options`.

## See Also

### Creating Comparison Predicates

- [Displaying searchable content by using a search controller](../../uikit/displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [predicateWithLeftExpression:rightExpression:customSelector:](predicatewithleftexpression_rightexpression_customselector_.md) — Returns a new predicate formed by combining the left and right expressions using a given selector.
- [- initWithLeftExpression:rightExpression:customSelector:](<init(leftexpression_rightexpression_customselector_).md>) — Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [- initWithLeftExpression:rightExpression:modifier:type:options:](<init(leftexpression_rightexpression_modifier_type_options_).md>) — Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.
- [- initWithCoder:](<init(coder_).md>) — Creates a predicate by decoding from the coder you specify.
