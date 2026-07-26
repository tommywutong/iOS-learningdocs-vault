---
title: 'init(width:height:bezierPoints:colors:background:smoothsColors:colorSpace:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/meshgradient/init(width:height:bezierpoints:colors:background:smoothscolors:colorspace:)'
source_url: 'https://developer.apple.com/documentation/swiftui/meshgradient/init(width:height:bezierpoints:colors:background:smoothscolors:colorspace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/meshgradient/init%28width%3Aheight%3Abezierpoints%3Acolors%3Abackground%3Asmoothscolors%3Acolorspace%3A%29.json'
content_hash: 'sha256:8329938b3f48c2c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MeshGradient](../meshgradient.md)

# init(width:height:bezierPoints:colors:background:smoothsColors:colorSpace:)

<sub>Initializer</sub>

Creates a new gradient mesh specified as a 2D grid of colored points, specifying the Bezier control points explicitly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(width: Int, height: Int, bezierPoints: [MeshGradient.BezierPoint], colors: [Color], background: Color = .clear, smoothsColors: Bool = true, colorSpace: Gradient.ColorSpace = .device)
```

## Parameters

- `width` — The width of the mesh, i.e. the number of vertices per row.

- `height` — The height of the mesh, i.e. the number of vertices per column.

- `bezierPoints` — The array of points and control points, containing `width x height` elements.

- `colors` — The array of colors, containing `width x height` elements.

- `background` — The background color, this fills any points outside the defined vertex mesh.

- `smoothsColors` — Whether cubic (smooth) interpolation should be used for the colors in the mesh (rather than only for the shape of the mesh).

- `colorSpace` — The color space in which to interpolate vertex colors.
