---
title: 'makeContainer(context:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/set/makecontainer(context:)'
source_url: 'https://developer.apple.com/documentation/swift/set/makecontainer(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/makecontainer%28context%3A%29.json'
content_hash: 'sha256:12874094b7710f12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# makeContainer(context:)

<sub>Instance Method</sub>

Creates a container that represents this set of intent values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeContainer(context: IntentValueContainer.ConversionContext) -> IntentValueContainer
```

## Parameters

- `context` — The context to use for the conversion.

## Return Value

An intent value container representing this set.

## Discussion

This method converts each element in the set to its container representation and wraps them in an `ArrayContainerElement`.
