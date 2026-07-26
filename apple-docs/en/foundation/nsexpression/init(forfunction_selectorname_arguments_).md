---
title: 'init(forFunction:selectorName:arguments:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(forfunction:selectorname:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(forfunction:selectorname:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28forfunction%3Aselectorname%3Aarguments%3A%29.json'
content_hash: 'sha256:fefb6a5a4f76eeac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(forFunction:selectorName:arguments:)

<sub>Initializer</sub>

Creates an expression that returns the result of invoking a selector with a specified name using specified arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forFunction target: NSExpression, selectorName name: String, arguments parameters: [Any]?)
```

## Parameters

- `target` — An `NSExpression` object which will evaluate an object on which the selector identified by `name` may be invoked.

- `name` — The name of the method to be invoked.

- `parameters` — An array containing `NSExpression` objects which can be evaluated to provide parameters for the method specified by `name`.

## Return Value

An expression which will return the result of invoking the selector named `name` on the result of evaluating the target expression with the parameters specified by evaluating the elements of `parameters`.

## Discussion

See the description of [+ expressionForFunction:arguments:](<init(forfunction_arguments_).md>) for examples of how to construct the parameter array.

### Special Considerations

This method throws an exception immediately if the selector is unknown; it throws at runtime if the parameters are incorrect.

This expression effectively allows your application to invoke any method on any object it can navigate to at runtime. You must consider the security implications of this type of evaluation.

## See Also

### Creating an Expression for a Function

- [+ expressionForFunction:arguments:](<init(forfunction_arguments_).md>) — Creates an expression that invokes one of the predefined functions.
