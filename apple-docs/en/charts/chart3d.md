---
title: Chart3D
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chart3d
source_url: 'https://developer.apple.com/documentation/charts/chart3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart3d.json'
content_hash: 'sha256:9357e985ce5c0c99'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# Chart3D

<sub>Structure</sub>

A SwiftUI view that displays interactive 3D charts and visualizations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct Chart3D<Content> where Content : Chart3DContent
```

## Overview

Use `Chart3D` to create three-dimensional data visualizations with compatible mark types. To add content to your chart, use the 3D-only [SurfacePlot](surfaceplot.md) or the 3D initializers of [PointMark](pointmark.md), [RuleMark](rulemark.md), and [RectangleMark](rectanglemark.md).

For example, you can use a [SurfacePlot](surfaceplot.md) to visualize a 3D surface for the function `y = cos(2 * x) * sin(2 * x)`:

```swift
Chart3D {
    SurfacePlot(x: "x", y: "y", z: "z") { x, z in
        sin(2 * x) * cos(2 * z)
    }
}
```

You can also use the 3D initializers for `PointMark` [init(x:y:z:)](<pointmark/init(x_y_z_).md>), `RuleMark` [init(x:y:z:)](<rulemark/init(x_y_z_).md>), `RectangleMark` [init(x:y:z:)](<rectanglemark/init(x_y_z_).md>) to plot 3D visualizations of your data.

For example, suppose you have an array of `Penguin` structures that define datapoints composed of `beakLength`, `weight` `flipperLength`:

```swift
struct Penguin: Identifiable {
    let id: Int
    let flipperLength: Double
    let weight: Double
    let beakLength: Double
}

let penguins: [Penguin] = [
    Penguin(id: 0, flipperLength: 197, weight: 4.2, beakLength: 59),
    Penguin(id: 1, flipperLength: 220, weight: 4.7, beakLength: 48),
    Penguin(id: 2, flipperLength: 235, weight: 5.8, beakLength: 42),
    ...
]
```

You can also use the 3D initializer of`PointMark` [init(x:y:z:)](<pointmark/init(x_y_z_).md>) to represent the `flipperLength` property as the x value, the `weight` property as the y value, and the `beakLength` property as the z value:

```swift
Chart3D(penguins) {
    PointMark(
        x: .value("Flipper Length (mm)", $0.flipperLength),
        y: .value("Weight (kg)", $0.weight),
        z: .value("Beak Length (mm)", $0.beakLength)
    )
}
```

### Customizing interactivity

To make your 3D Chart interactive, declare a `@State` property of type  [Chart3DPose](chart3dpose.md) and pass it as a binding to the `chart3DPose(_:)-(Binding<Chart3DPose>)` view modifier:

```swift
@State private var pose: Chart3DPose = .default
var body: some View {
    Chart3D(penguins) {
        PointMark(
            x: .value("Flipper Length (mm)", $0.flipperLength),
            y: .value("Weight (kg)", $0.weight),
            z: .value("Beak Length (mm)", $0.beakLength)
        )
    }
    .chart3DPose($pose)
}
```

On available platforms, you can use the `chart3DCameraProjection(_:)` modifier to switch from orthographic to perspective projection.

```swift
Chart3D(penguins) {
    ...
}
.chart3DCameraProjection(.perspective)
```

A SwiftUI view that displays a three-dimensional chart.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating 3D charts

- [init(_:content:)](<chart3d/init(__content_).md>) — Creates a 3D chart composed of a series of identifiable marks.
- [init(_:id:content:)](<chart3d/init(__id_content_).md>) — Creates a 3D chart composed of a series of marks.
- [init(content:)](<chart3d/init(content_).md>)

### Configuring chart shapes

- [Chart3DSymbolShape](chart3dsymbolshape.md) — A type that can act as a shape for the marks that you add to a chart.
- [BasicChart3DSymbolShape](basicchart3dsymbolshape.md) — A basic chart symbol shape.

### Configuring surfaces

- [Chart3DSurfaceStyle](chart3dsurfacestyle.md)
- [BasicChart3DSurfaceStyle](basicchart3dsurfacestyle.md)

### Customizing chart presentation

- [Chart3DCameraProjection](chart3dcameraprojection.md)
- [Chart3DPose](chart3dpose.md)

## See Also

### 3D charts

- [Chart3DContent](chart3dcontent.md) — A type that represents the three-dimensional content that you draw on a chart.
- [Chart3DContentBuilder](chart3dcontentbuilder.md) — A result builder that you use to compose the three-dimensional contents of a chart.
- [SurfacePlot](surfaceplot.md) — Chart content that represents a mathematical function of two variables using a 3D surface.
