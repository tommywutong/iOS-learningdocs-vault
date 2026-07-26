---
title: 'init(block:arguments:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(block:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(block:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28block%3Aarguments%3A%29.json'
content_hash: 'sha256:4bbeb0635830f910'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(block:arguments:)

<sub>Initializer</sub>

Creates an expression object that uses the block for evaluating objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(block: @escaping (Any?, [NSExpression], NSMutableDictionary?) -> Any, arguments: [NSExpression]?)
```

## Parameters

- `block` — The Block is applied to the object to be evaluated. The Block takes three arguments and returns a value: - **evaluatedObject** — The object to be evaluated. - **expressions** — An array of predicate expressions that evaluates to a collection. - **context** — A dictionary that the expression can use to store temporary state for one predicate evaluation. Note that `context` is mutable, and that it can only be accessed during the evaluation of the expression. You must not attempt to retain it for use elsewhere. ] The Block returns the `evaluatedObject`.

- `arguments` — An array containing `NSExpression` objects that will be used as parameters during the invocation of selector. For a selector taking no parameters, the array should be empty. For a selector taking one or more parameters, the array should contain one `NSExpression` object which will evaluate to an instance of the appropriate type for each parameter. If there is a mismatch between the number of parameters expected and the number you provide during evaluation, an exception may be raised or missing parameters may simply be replaced by `nil` (which occurs depends on how many parameters are provided, and whether you have over- or underflow). See [+ expressionForFunction:arguments:](<init(forfunction_arguments_).md>) for a complete list of arguments.

## Return Value

An expression that filters a collection using the specified Block.

## See Also

### Related Documentation

- [expressionBlock](expressionblock.md) — The block that executes to evaluate the expression.
