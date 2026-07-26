---
title: 'strokeBorder(lineWidth:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/basicchartsymbolshape/strokeborder(linewidth:)'
source_url: 'https://developer.apple.com/documentation/charts/basicchartsymbolshape/strokeborder(linewidth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/basicchartsymbolshape/strokeborder%28linewidth%3A%29.json'
content_hash: 'sha256:754e8ed6eedd8bc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [BasicChartSymbolShape](../basicchartsymbolshape.md)

# strokeBorder(lineWidth:)

<sub>Instance Method</sub>

Creates a stroked symbol shape by inner-stroking the basic symbol shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func strokeBorder(lineWidth: CGFloat = 1) -> some ChartSymbolShape

```

## Parameters

- `lineWidth` — The stroke line width.

## Return Value

A symbol shape that strokes the shape of `self`.
