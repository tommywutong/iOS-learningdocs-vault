---
title: makeExpression()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swift/array/makeexpression()
source_url: 'https://developer.apple.com/documentation/swift/array/makeexpression()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/makeexpression%28%29.json'
content_hash: 'sha256:c294c3505960cf2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# makeExpression()

<sub>Instance Method</sub>

Creates a pending expression of an array of intent values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeExpression() -> IntentValueExpression
```

## Return Value

An intent value expression representing this array.

## Discussion

The system evaluates the expression when needed, allowing for lazy conversion of the array’s elements.
