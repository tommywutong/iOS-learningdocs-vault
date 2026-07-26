---
title: 'grayscale(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/grayscale(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/grayscale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/grayscale%28_%3A%29.json'
content_hash: 'sha256:f4c4298bbc8c868d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# grayscale(_:)

<sub>Instance Method</sub>

Adds a grayscale effect to the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func grayscale(_ amount: Double) -> some VisualEffect

```

## Parameters

- `amount` — The intensity of grayscale to apply from 0.0 to less than 1.0. Values closer to 0.0 are more colorful, and values closer to 1.0 are less colorful.

## Return Value

An effect that reduces the intensity of colors in the view.

## Discussion

A grayscale effect reduces the intensity of colors in the view.

## See Also

### Adjusting Color

- [brightness(_:)](<brightness(__).md>) — Brightens the view by the specified amount.
- [colorEffect(_:isEnabled:)](<coloreffect(__isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [contrast(_:)](<contrast(__).md>) — Sets the contrast and separation between similar colors in the view.
- [hueRotation(_:)](<huerotation(__).md>) — Applies a hue rotation effect to the view.
- [saturation(_:)](<saturation(__).md>) — Adjusts the color saturation of the view.
- [opacity(_:)](<opacity(__).md>) — Sets the transparency of the view.
