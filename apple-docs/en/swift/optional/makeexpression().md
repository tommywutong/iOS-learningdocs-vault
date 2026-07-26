---
title: makeExpression()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/optional/makeexpression()
source_url: 'https://developer.apple.com/documentation/swift/optional/makeexpression()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/makeexpression%28%29.json'
content_hash: 'sha256:b6dd9eddd66a73be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# makeExpression()

<sub>Instance Method</sub>

Creates an expression that represents this optional intent value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeExpression() -> IntentValueExpression
```

## Return Value

An intent value expression representing this optional value.

## Discussion

This method handles both the `.some` and `.none` cases:

- For `.none`, it creates a pending expression that will resolve to a null value
- For `.some`, it delegates to the wrapped value’s expression creation
