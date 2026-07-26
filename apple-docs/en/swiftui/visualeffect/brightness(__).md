---
title: 'brightness(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/brightness(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/brightness(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/brightness%28_%3A%29.json'
content_hash: 'sha256:a7f1f7b0a28cddab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# brightness(_:)

<sub>Instance Method</sub>

Brightens the view by the specified amount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func brightness(_ amount: Double) -> some VisualEffect

```

## Parameters

- `amount` — A value between 0 (no effect) and 1 (full white brightening) that represents the intensity of the brightness effect.

## Return Value

An effect that brightens the view by the specified amount.

## See Also

### Adjusting Color

- [colorEffect(_:isEnabled:)](<coloreffect(__isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [contrast(_:)](<contrast(__).md>) — Sets the contrast and separation between similar colors in the view.
- [grayscale(_:)](<grayscale(__).md>) — Adds a grayscale effect to the view.
- [hueRotation(_:)](<huerotation(__).md>) — Applies a hue rotation effect to the view.
- [saturation(_:)](<saturation(__).md>) — Adjusts the color saturation of the view.
- [opacity(_:)](<opacity(__).md>) — Sets the transparency of the view.
