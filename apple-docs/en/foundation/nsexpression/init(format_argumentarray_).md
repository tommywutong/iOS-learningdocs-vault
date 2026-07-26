---
title: 'init(format:argumentArray:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(format:argumentarray:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(format:argumentarray:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28format%3Aargumentarray%3A%29.json'
content_hash: 'sha256:b3e8e67a2daae3d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(format:argumentArray:)

<sub>Initializer</sub>

Creates the expression with the specified expression format and array of arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(format expressionFormat: String, argumentArray arguments: [Any])
```

## Parameters

- `expressionFormat` — The expression format.

- `arguments` — An array of arguments to be used with the `expressionFormat` string.

## Return Value

An initialized `NSExpression` object with the specified arguments.

## See Also

### Creating an Expression

- [- initWithExpressionType:](<init(expressiontype_).md>) — Creates the expression with the specified expression type.
- [+ expressionWithFormat:arguments:](<init(format_arguments_).md>) — Creates the expression with the specified expression format and arguments list.
- [init(format:_:)](<init(format___).md>) — Creates the expression with the expression format and arguments list you specify.
- [- initWithCoder:](<init(coder_).md>) — Creates an expression by decoding from the coder you specify.
