---
title: 'init(leftExpression:rightExpression:customSelector:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscomparisonpredicate/init(leftexpression:rightexpression:customselector:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/init(leftexpression:rightexpression:customselector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/init%28leftexpression%3Arightexpression%3Acustomselector%3A%29.json'
content_hash: 'sha256:ce9bad80f91a26a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# init(leftExpression:rightExpression:customSelector:)

<sub>Initializer</sub>

Creates a predicate that you form by combining specified left and right expressions using a specified selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, customSelector selector: Selector)
```

## Parameters

- `lhs` — The left hand expression.

- `rhs` — The right hand expression.

- `selector` — The selector to use. The method defined by the selector must take a single argument and return a `BOOL` value.

## Return Value

The receiver, initialized by combining the left and right expressions using `selector`.

## See Also

### Creating Comparison Predicates

- [Displaying searchable content by using a search controller](../../uikit/displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [- initWithLeftExpression:rightExpression:modifier:type:options:](<init(leftexpression_rightexpression_modifier_type_options_).md>) — Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.
- [- initWithCoder:](<init(coder_).md>) — Creates a predicate by decoding from the coder you specify.
