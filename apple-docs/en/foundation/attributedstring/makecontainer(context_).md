---
title: 'makeContainer(context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/foundation/attributedstring/makecontainer(context:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/makecontainer(context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/makecontainer%28context%3A%29.json'
content_hash: 'sha256:02ef05d3784276cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# makeContainer(context:)

<sub>Instance Method</sub>

Creates a container that represents the attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeContainer(context: IntentValueContainer.ConversionContext) -> IntentValueContainer
```

## Parameters

- `context` — The context to use for the conversion.

## Return Value

An intent value container representing this attributed string.

## Discussion

This method converts the `AttributedString` to an `NSAttributedString` and wraps it in an intent value container.
