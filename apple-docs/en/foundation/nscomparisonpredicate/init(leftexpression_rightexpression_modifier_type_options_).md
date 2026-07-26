---
title: 'init(leftExpression:rightExpression:modifier:type:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscomparisonpredicate/init(leftexpression:rightexpression:modifier:type:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonpredicate/init(leftexpression:rightexpression:modifier:type:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonpredicate/init%28leftexpression%3Arightexpression%3Amodifier%3Atype%3Aoptions%3A%29.json'
content_hash: 'sha256:5bcc4326bc902756'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSComparisonPredicate](../nscomparisonpredicate.md)

# init(leftExpression:rightExpression:modifier:type:options:)

<sub>Initializer</sub>

Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(leftExpression lhs: NSExpression, rightExpression rhs: NSExpression, modifier: NSComparisonPredicate.Modifier, type: NSComparisonPredicate.Operator, options: NSComparisonPredicate.Options = [])
```

## Parameters

- `lhs` — The left hand expression.

- `rhs` — The right hand expression.

- `modifier` — The modifier to apply.

- `type` — The predicate operator type.

- `options` — The options to apply (see [Options](options-swift.struct.md)). For no options, pass `0`.

## Return Value

The receiver, initialized to a predicate of type `type` formed by combining the left and right expressions using the `modifier` and `options`.

## See Also

### Creating Comparison Predicates

- [Displaying searchable content by using a search controller](../../uikit/displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [- initWithLeftExpression:rightExpression:customSelector:](<init(leftexpression_rightexpression_customselector_).md>) — Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [- initWithCoder:](<init(coder_).md>) — Creates a predicate by decoding from the coder you specify.
