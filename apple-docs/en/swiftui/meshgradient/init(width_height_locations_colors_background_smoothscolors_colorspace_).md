---
title: 'init(width:height:locations:colors:background:smoothsColors:colorSpace:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/meshgradient/init(width:height:locations:colors:background:smoothscolors:colorspace:)'
source_url: 'https://developer.apple.com/documentation/swiftui/meshgradient/init(width:height:locations:colors:background:smoothscolors:colorspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/meshgradient/init%28width%3Aheight%3Alocations%3Acolors%3Abackground%3Asmoothscolors%3Acolorspace%3A%29.json'
content_hash: 'sha256:2bfdfba49621c8d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MeshGradient](../meshgradient.md)

# init(width:height:locations:colors:background:smoothsColors:colorSpace:)

<sub>Initializer</sub>

Creates a new gradient mesh specified as a 2D grid of colored vertices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(width: Int, height: Int, locations: MeshGradient.Locations, colors: MeshGradient.Colors, background: Color = .clear, smoothsColors: Bool = true, colorSpace: Gradient.ColorSpace = .device)
```

## Parameters

- `width` — The width of the mesh, i.e. the number of vertices per row.

- `height` — The height of the mesh, i.e. the number of vertices per column.

- `locations` — The array of locations, containing `width x height` elements.

- `colors` — The array of colors, containing `width x height` elements.

- `background` — The background color, this fills any points outside the defined vertex mesh.

- `smoothsColors` — Whether cubic (smooth) interpolation should be used for the colors in the mesh (rather than only for the shape of the mesh).

- `colorSpace` — The color space in which to interpolate vertex colors.
