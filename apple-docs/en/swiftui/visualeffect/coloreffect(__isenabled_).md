---
title: 'colorEffect(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/coloreffect(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/coloreffect(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/coloreffect%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:9180cf88f325cf16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# colorEffect(_:isEnabled:)

<sub>Instance Method</sub>

Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func colorEffect(_ shader: Shader, isEnabled: Bool = true) -> some VisualEffect

```

## Parameters

- `shader` — The shader to apply to `self` as a color filter.

- `isEnabled` — Whether the effect is enabled or not.

## Return Value

A new view that renders `self` with the shader applied as a color filter.

## Discussion

For a shader function to act as a color filter it must have a function signature matching:

```swift
[[ stitchable ]] half4 name(float2 position, half4 color, args...)
```

where `position` is the user-space coordinates of the pixel applied to the shader and `color` its source color, as a pre-multiplied color in the destination color space. `args...` should be compatible with the uniform arguments bound to `shader`. The function should return the modified color value.

> [!important] Important
> Views backed by AppKit or UIKit views may not render into the filtered layer. Instead, they log a warning and display a placeholder image to highlight the error.

## See Also

### Adjusting Color

- [brightness(_:)](<brightness(__).md>) — Brightens the view by the specified amount.
- [contrast(_:)](<contrast(__).md>) — Sets the contrast and separation between similar colors in the view.
- [grayscale(_:)](<grayscale(__).md>) — Adds a grayscale effect to the view.
- [hueRotation(_:)](<huerotation(__).md>) — Applies a hue rotation effect to the view.
- [saturation(_:)](<saturation(__).md>) — Adjusts the color saturation of the view.
- [opacity(_:)](<opacity(__).md>) — Sets the transparency of the view.
