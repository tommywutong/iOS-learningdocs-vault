---
title: 'predicateWithLeftExpression:rightExpression:customSelector:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscomparisonpredicate/predicatewithleftexpression:rightexpression:customselector:'
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/predicatewithleftexpression:rightexpression:customselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/predicatewithleftexpression%3Arightexpression%3Acustomselector%3A.json'
content_hash: 'sha256:6d626af448d9f0bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# predicateWithLeftExpression:rightExpression:customSelector:

<sub>Type Method</sub>

Returns a new predicate formed by combining the left and right expressions using a given selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSComparisonPredicate *) predicateWithLeftExpression:(NSExpression *) lhs rightExpression:(NSExpression *) rhs customSelector:(SEL) selector;
```

## Parameters

- `lhs` — The left hand side expression.

- `rhs` — The right hand side expression.

- `selector` — The selector to use for comparison. The method defined by the selector must take a single argument and return a `BOOL` value.

## Return Value

A new predicate formed by combining the left and right expressions using `selector`.

## See Also

### Related Documentation

- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)

### Creating Comparison Predicates

- [Displaying searchable content by using a search controller](../../uikit/displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [predicateWithLeftExpression:rightExpression:modifier:type:options:](predicatewithleftexpression_rightexpression_modifier_type_options_.md) — Creates and returns a predicate of a given type formed by combining given left and right expressions using a given modifier and options.
- [- initWithLeftExpression:rightExpression:customSelector:](<init(leftexpression_rightexpression_customselector_).md>) — Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [- initWithLeftExpression:rightExpression:modifier:type:options:](<init(leftexpression_rightexpression_modifier_type_options_).md>) — Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.
- [- initWithCoder:](<init(coder_).md>) — Creates a predicate by decoding from the coder you specify.
