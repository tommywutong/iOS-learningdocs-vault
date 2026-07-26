---
title: 'foregroundStyle(_:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axismark/foregroundstyle(_:)'
source_url: 'https://developer.apple.com/documentation/charts/axismark/foregroundstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismark/foregroundstyle%28_%3A%29.json'
content_hash: 'sha256:1548abf37bc63742'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisMark](../axismark.md)

# foregroundStyle(_:)

<sub>Instance Method</sub>

Sets the axis content’s foreground elements to use a given style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func foregroundStyle<S>(_ style: S) -> some AxisMark where S : ShapeStyle

```

## Parameters

- `style` — The color or pattern to use when filling in the foreground elements.

## Return Value

An axis content that uses the given foreground style.
