---
title: 'init(format:_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(format:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(format:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28format%3A_%3A%29.json'
content_hash: 'sha256:bdd7f642a74b2b80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(format:_:)

<sub>Initializer</sub>

Creates the expression with the expression format and arguments list you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(format expressionFormat: String, _ args: any CVarArg...)
```

## Parameters

- `expressionFormat` — The expression format.

- `args` — A list of arguments to insert into the `expressionFormat` string.

## See Also

### Creating an Expression

- [- initWithExpressionType:](<init(expressiontype_).md>) — Creates the expression with the specified expression type.
- [+ expressionWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates the expression with the specified expression format and array of arguments.
- [+ expressionWithFormat:arguments:](<init(format_arguments_).md>) — Creates the expression with the specified expression format and arguments list.
- [- initWithCoder:](<init(coder_).md>) — Creates an expression by decoding from the coder you specify.
