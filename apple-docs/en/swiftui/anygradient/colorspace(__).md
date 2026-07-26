---
title: 'colorSpace(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anygradient/colorspace(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anygradient/colorspace(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anygradient/colorspace%28_%3A%29.json'
content_hash: 'sha256:b7ff33c0be61289d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyGradient](../anygradient.md)

# colorSpace(_:)

<sub>Instance Method</sub>

Returns a version of the gradient that will use a specified color space for interpolating between its colors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func colorSpace(_ space: Gradient.ColorSpace) -> AnyGradient
```

## Parameters

- `space` — The color space the new gradient will use to interpolate its constituent colors.

## Return Value

A new gradient that interpolates its colors in the specified color space.

## Discussion

```swift
Rectangle().fill(.linearGradient(
    colors: [.white, .blue]).colorSpace(.perceptual))
```
