---
title: 'contrast(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/contrast(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/contrast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/contrast%28_%3A%29.json'
content_hash: 'sha256:9d8c6e6db929324f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# contrast(_:)

<sub>Instance Method</sub>

Sets the contrast and separation between similar colors in the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contrast(_ amount: Double) -> some VisualEffect

```

## Parameters

- `amount` — The intensity of color contrast to apply. negative values invert colors in addition to applying contrast.

## Return Value

An effect that applies color contrast to the view.

## Discussion

Apply contrast to a view to increase or decrease the separation between similar colors in the view.

## See Also

### Adjusting Color

- [brightness(_:)](<brightness(__).md>) — Brightens the view by the specified amount.
- [colorEffect(_:isEnabled:)](<coloreffect(__isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [grayscale(_:)](<grayscale(__).md>) — Adds a grayscale effect to the view.
- [hueRotation(_:)](<huerotation(__).md>) — Applies a hue rotation effect to the view.
- [saturation(_:)](<saturation(__).md>) — Adjusts the color saturation of the view.
- [opacity(_:)](<opacity(__).md>) — Sets the transparency of the view.
