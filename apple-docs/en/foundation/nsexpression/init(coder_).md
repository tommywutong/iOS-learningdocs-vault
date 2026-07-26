---
title: 'init(coder:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(coder:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28coder%3A%29.json'
content_hash: 'sha256:7a8965353dc4c5ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(coder:)

<sub>Initializer</sub>

Creates an expression by decoding from the coder you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(coder: NSCoder)
```

## Parameters

- `coder` — The coder to read data from.

## See Also

### Creating an Expression

- [- initWithExpressionType:](<init(expressiontype_).md>) — Creates the expression with the specified expression type.
- [+ expressionWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates the expression with the specified expression format and array of arguments.
- [+ expressionWithFormat:arguments:](<init(format_arguments_).md>) — Creates the expression with the specified expression format and arguments list.
- [init(format:_:)](<init(format___).md>) — Creates the expression with the expression format and arguments list you specify.
