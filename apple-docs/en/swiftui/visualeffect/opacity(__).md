---
title: 'opacity(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/opacity(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/opacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/opacity%28_%3A%29.json'
content_hash: 'sha256:60489cdf5120bc52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# opacity(_:)

<sub>Instance Method</sub>

Sets the transparency of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func opacity(_ opacity: Double) -> some VisualEffect

```

## Parameters

- `opacity` — A value between 0 (fully transparent) and 1 (fully opaque).

## Return Value

An effect that sets the transparency of the view.

## Discussion

When applying the `opacity(_:)` effect to a view that has already had its opacity transformed, the effect of the underlying opacity transformation is multiplied.

## See Also

### Adjusting Color

- [brightness(_:)](<brightness(__).md>) — Brightens the view by the specified amount.
- [colorEffect(_:isEnabled:)](<coloreffect(__isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [contrast(_:)](<contrast(__).md>) — Sets the contrast and separation between similar colors in the view.
- [grayscale(_:)](<grayscale(__).md>) — Adds a grayscale effect to the view.
- [hueRotation(_:)](<huerotation(__).md>) — Applies a hue rotation effect to the view.
- [saturation(_:)](<saturation(__).md>) — Adjusts the color saturation of the view.
