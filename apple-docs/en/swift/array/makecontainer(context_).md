---
title: 'makeContainer(context:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/array/makecontainer(context:)'
source_url: 'https://developer.apple.com/documentation/swift/array/makecontainer(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/makecontainer%28context%3A%29.json'
content_hash: 'sha256:9509725674c6201f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# makeContainer(context:)

<sub>Instance Method</sub>

Creates a container that represents this array of intent values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeContainer(context: IntentValueContainer.ConversionContext) -> IntentValueContainer
```

## Parameters

- `context` — The context to use for the conversion.

## Return Value

An intent value container representing this array.

## Discussion

This method converts each element in the array to its container representation and wraps them in an `ArrayContainerElement`.
