---
title: 'alphaThreshold(min:max:color:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/graphicscontext/filter/alphathreshold(min:max:color:)'
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/filter/alphathreshold(min:max:color:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/filter/alphathreshold%28min%3Amax%3Acolor%3A%29.json'
content_hash: 'sha256:15cb15ad6f6b5881'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [GraphicsContext](../../graphicscontext.md) · [Filter](../filter.md)

# alphaThreshold(min:max:color:)

<sub>Type Method</sub>

Returns a filter that replaces each pixel with alpha components within a range by a constant color, or transparency otherwise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func alphaThreshold(min: Double, max: Double = 1, color: Color = Color.black) -> GraphicsContext.Filter
```

## Parameters

- `min` — The minimum alpha threshold. Pixels whose alpha component is less than this value will render as transparent. Results are undefined unless `min < max`.

- `max` — The maximum alpha threshold. Pixels whose alpha component is greater than this value will render as transparent. Results are undefined unless `min < max`.

- `color` — The color that is output for pixels with an alpha component between the two threshold values.

## Return Value

A filter that applies a threshold to alpha values.

## See Also

### Adjusting opacity

- [luminanceToAlpha](luminancetoalpha.md) — Returns a filter that sets the opacity of each pixel based on its luminance.
