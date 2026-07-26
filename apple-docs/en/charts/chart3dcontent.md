---
title: Chart3DContent
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chart3dcontent
source_url: 'https://developer.apple.com/documentation/charts/chart3dcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart3dcontent.json'
content_hash: 'sha256:c3829b1fe27457e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# Chart3DContent

<sub>Protocol</sub>

A type that represents the three-dimensional content that you draw on a chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol Chart3DContent
```

## Relationships

- **Conforming Types**: [BuilderConditional](builderconditional.md), [PointMark](pointmark.md), [RectangleMark](rectanglemark.md), [RuleMark](rulemark.md), [SurfacePlot](surfaceplot.md)

## Topics

### Associated Types

- [Body](chart3dcontent/body-swift.associatedtype.md)

### Instance Properties

- [body](chart3dcontent/body-swift.property.md)

### Instance Methods

- [foregroundStyle(_:)](<chart3dcontent/foregroundstyle(__)-1pjaq.md>)
- [foregroundStyle(_:)](<chart3dcontent/foregroundstyle(__)-7skde.md>)
- [foregroundStyle(by:)](<chart3dcontent/foregroundstyle(by_).md>)
- [metalness(_:)](<chart3dcontent/metalness(__).md>) — A value that controls whether the surface has a metallic look.
- [roughness(_:)](<chart3dcontent/roughness(__).md>) — A value that controls the degree of surface roughness.
- [symbol(_:)](<chart3dcontent/symbol(__).md>)
- [symbolRotation(_:)](<chart3dcontent/symbolrotation(__).md>) — Set the rotation of a 3D symbol.
- [symbolSize(_:)](<chart3dcontent/symbolsize(__).md>)

## See Also

### 3D charts

- [Chart3D](chart3d.md) — A SwiftUI view that displays interactive 3D charts and visualizations.
- [Chart3DContentBuilder](chart3dcontentbuilder.md) — A result builder that you use to compose the three-dimensional contents of a chart.
- [SurfacePlot](surfaceplot.md) — Chart content that represents a mathematical function of two variables using a 3D surface.
