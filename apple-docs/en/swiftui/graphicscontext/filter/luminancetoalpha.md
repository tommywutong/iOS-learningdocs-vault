---
title: luminanceToAlpha
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/filter/luminancetoalpha
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/luminancetoalpha'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/luminancetoalpha.json'
content_hash: 'sha256:6a9da26a4d999d74'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# luminanceToAlpha

<sub>Type Property</sub>

Returns a filter that sets the opacity of each pixel based on its luminance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var luminanceToAlpha: GraphicsContext.Filter { get }
```

## Return Value

A filter that applies a luminance to alpha transformation.

## Discussion

The filter computes the luminance of each pixel and uses it to define the opacity of the result, combined with black (zero) color components.

## See Also

### Adjusting opacity

- [alphaThreshold(min:max:color:)](<alphathreshold(min_max_color_).md>) — Returns a filter that replaces each pixel with alpha components within a range by a constant color, or transparency otherwise.
