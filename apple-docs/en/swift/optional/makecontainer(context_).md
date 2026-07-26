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
doc_path: '/documentation/swift/optional/makecontainer(context:)'
source_url: 'https://developer.apple.com/documentation/swift/optional/makecontainer(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/optional/makecontainer%28context%3A%29.json'
content_hash: 'sha256:9cd9c6081ff7e172'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Optional](../optional.md)

# makeContainer(context:)

<sub>Instance Method</sub>

Creates a container that represents this optional intent value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeContainer(context: IntentValueContainer.ConversionContext) -> IntentValueContainer
```

## Parameters

- `context` — The context to use for the conversion.

## Return Value

An intent value container representing this optional value.

## Discussion

If the optional is `nil`, it creates a container that resolves to a null vlaue. If the optional isn’t `nil`, it delegates the conversation to the wrapped value’s container creation.
