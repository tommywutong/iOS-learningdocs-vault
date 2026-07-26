---
title: 'init(format:arguments:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(format:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(format:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28format%3Aarguments%3A%29.json'
content_hash: 'sha256:895716b2d1f6cd25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(format:arguments:)

<sub>Initializer</sub>

Creates the expression with the specified expression format and arguments list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(format expressionFormat: String, arguments argList: CVaListPointer)
```

## Parameters

- `expressionFormat` — The expression format.

- `argList` — A list of arguments to be inserted into the `expressionFormat` string. The argument list is terminated by `nil`.

## Return Value

An initialized `NSExpression` object with the specified arguments.

## See Also

### Creating an Expression

- [- initWithExpressionType:](<init(expressiontype_).md>) — Creates the expression with the specified expression type.
- [+ expressionWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates the expression with the specified expression format and array of arguments.
- [init(format:_:)](<init(format___).md>) — Creates the expression with the expression format and arguments list you specify.
- [- initWithCoder:](<init(coder_).md>) — Creates an expression by decoding from the coder you specify.
