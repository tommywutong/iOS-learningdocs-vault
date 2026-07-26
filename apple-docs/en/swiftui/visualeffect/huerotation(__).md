---
title: 'hueRotation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/huerotation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/huerotation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/huerotation%28_%3A%29.json'
content_hash: 'sha256:a11acb54bae13f24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# hueRotation(_:)

<sub>Instance Method</sub>

Applies a hue rotation effect to the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hueRotation(_ angle: Angle) -> some VisualEffect

```

## Parameters

- `angle` — The hue rotation angle to apply to the colors in the view.

## Return Value

An effect that shifts all of the colors in the view.

## Discussion

Use hue rotation effect to shift all of the colors in a view according to the angle you specify.

## See Also

### Adjusting Color

- [brightness(_:)](<brightness(__).md>) — Brightens the view by the specified amount.
- [colorEffect(_:isEnabled:)](<coloreffect(__isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter effect on the color of each pixel.
- [contrast(_:)](<contrast(__).md>) — Sets the contrast and separation between similar colors in the view.
- [grayscale(_:)](<grayscale(__).md>) — Adds a grayscale effect to the view.
- [saturation(_:)](<saturation(__).md>) — Adjusts the color saturation of the view.
- [opacity(_:)](<opacity(__).md>) — Sets the transparency of the view.
