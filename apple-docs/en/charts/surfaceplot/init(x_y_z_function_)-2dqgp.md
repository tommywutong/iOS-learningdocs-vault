---
title: 'init(x:y:z:function:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/surfaceplot/init(x:y:z:function:)-2dqgp'
source_url: 'https://developer.apple.com/documentation/charts/surfaceplot/init(x:y:z:function:)-2dqgp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/surfaceplot/init%28x%3Ay%3Az%3Afunction%3A%29-2dqgp.json'
content_hash: 'sha256:8fc64f710c1383cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [SurfacePlot](../surfaceplot.md)

# init(x:y:z:function:)

<sub>Initializer</sub>

Creates a SurfacePlot that represents a function y = f(x, z).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(x: Text, y: Text, z: Text, function: @escaping @Sendable (Double, Double) -> Double)
```

## Parameters

- `x` — The x label.

- `y` — The y label.

- `z` — The z label.

- `function` — The function to graph.

## Discussion

> [!note] Note
> For x and z value pairs where the function is undefined or is infinity, the function is expected to return `Double.nan`
