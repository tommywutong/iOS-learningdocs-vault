---
title: 'brightness(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/brightness(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/brightness(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/brightness%28_%3A%29.json'
content_hash: 'sha256:2e99e60c99a7638e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# brightness(_:)

<sub>Type Method</sub>

Returns a filter that applies a brightness adjustment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func brightness(_ amount: Double) -> GraphicsContext.Filter
```

## Parameters

- `amount` — An amount to add to the pixel’s color components.

## Return Value

A filter that applies a brightness adjustment.

## Discussion

This filter is different than `brightness` filter primitive defined by the Scalable Vector Graphics (SVG) specification. You can obtain an effect like that filter using a [grayscale(_:)](<grayscale(__).md>) color multiply. However, this filter does match the [CIColorControls](../../../coreimage/cicolorcontrols.md) filter’s brightness adjustment.

## See Also

### Changing brightness and contrast

- [contrast(_:)](<contrast(__).md>) — Returns a filter that applies a contrast adjustment.
