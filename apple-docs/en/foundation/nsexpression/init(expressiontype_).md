---
title: 'init(expressionType:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(expressiontype:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(expressiontype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28expressiontype%3A%29.json'
content_hash: 'sha256:ab814cc33745486b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(expressionType:)

<sub>Initializer</sub>

Creates the expression with the specified expression type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(expressionType type: NSExpression.ExpressionType)
```

## Parameters

- `type` — The type of the new expression, as defined by [ExpressionType](expressiontype-swift.enum.md).

## Return Value

An initialized `NSExpression` object of the type `type`.

## Discussion

This method is the designated initializer for `NSExpression`.

## See Also

### Related Documentation

- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)

### Creating an Expression

- [+ expressionWithFormat:argumentArray:](<init(format_argumentarray_).md>) — Creates the expression with the specified expression format and array of arguments.
- [+ expressionWithFormat:arguments:](<init(format_arguments_).md>) — Creates the expression with the specified expression format and arguments list.
- [init(format:_:)](<init(format___).md>) — Creates the expression with the expression format and arguments list you specify.
- [- initWithCoder:](<init(coder_).md>) — Creates an expression by decoding from the coder you specify.
