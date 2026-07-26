---
title: 'blur(radius:options:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/blur(radius:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/blur(radius:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/blur%28radius%3Aoptions%3A%29.json'
content_hash: 'sha256:986b0606d1d1c371'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# blur(radius:options:)

<sub>Type Method</sub>

Returns a filter that applies a Gaussian blur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func blur(radius: CGFloat, options: GraphicsContext.BlurOptions = BlurOptions()) -> GraphicsContext.Filter
```

## Parameters

- `radius` — The standard deviation of the Gaussian blur.

- `options` — A set of options controlling the application of the effect.

## Return Value

A filter that applies Gaussian blur.
