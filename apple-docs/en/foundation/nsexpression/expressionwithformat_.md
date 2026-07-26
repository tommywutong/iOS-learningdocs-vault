---
title: 'expressionWithFormat:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/expressionwithformat:'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/expressionwithformat:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/expressionwithformat%3A.json'
content_hash: 'sha256:25c89bc23e39ddde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# expressionWithFormat:

<sub>Type Method</sub>

Creates the expression with the specified expression arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSExpression *) expressionWithFormat:(NSString *) expressionFormat;
```

## Parameters

- `expressionFormat` — The expression format.

## Return Value

An initialized `NSExpression` object with the specified format.

## Discussion

After `expressionFormat`, pass a comma-separated list of arguments to substitute into format as variadic arguments. The list is terminated by `nil`.

## See Also

### Creating an Expression

- [- initWithExpressionType:](<init(expressiontype_).md>) — Creates the expression with the specified expression type.
- [+ expressionWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates the expression with the specified expression format and array of arguments.
- [+ expressionWithFormat:arguments:](<init(format_arguments_).md>) — Creates the expression with the specified expression format and arguments list.
- [- initWithCoder:](<init(coder_).md>) — Creates an expression by decoding from the coder you specify.
