---
title: 'saturation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/saturation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/saturation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/saturation%28_%3A%29.json'
content_hash: 'sha256:5ab6b611f39fdd14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# saturation(_:)

<sub>Instance Method</sub>

Adjusts the color saturation of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func saturation(_ amount: Double) -> some VisualEffect

```

## Parameters

- `amount` — The amount of saturation to apply to the view.

## Return Value

An effect that adjusts the saturation of the view.

## Discussion

Use color saturation to increase or decrease the intensity of colors in a view.

> [!info] See Also
> `contrast(_:)`

## See Also

### Adjusting Color

- [brightness(_:)](<brightness(__).md>) — Brightens the view by the specified amount.
- [colorEffect(_:isEnabled:)](<coloreffect(__isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [contrast(_:)](<contrast(__).md>) — Sets the contrast and separation between similar colors in the view.
- [grayscale(_:)](<grayscale(__).md>) — Adds a grayscale effect to the view.
- [hueRotation(_:)](<huerotation(__).md>) — Applies a hue rotation effect to the view.
- [opacity(_:)](<opacity(__).md>) — Sets the transparency of the view.
