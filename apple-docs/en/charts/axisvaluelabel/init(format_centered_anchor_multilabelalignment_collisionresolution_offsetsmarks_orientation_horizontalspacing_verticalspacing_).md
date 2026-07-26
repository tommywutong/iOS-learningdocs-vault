---
title: 'init(format:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axisvaluelabel/init(format:centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:)'
source_url: 'https://developer.apple.com/documentation/charts/axisvaluelabel/init(format:centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axisvaluelabel/init%28format%3Acentered%3Aanchor%3Amultilabelalignment%3Acollisionresolution%3Aoffsetsmarks%3Aorientation%3Ahorizontalspacing%3Averticalspacing%3A%29.json'
content_hash: 'sha256:7630fae49b181da3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisValueLabel](../axisvaluelabel.md)

# init(format:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)

<sub>Initializer</sub>

Constructs an axis value label with the given properties to display the given content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Format>(format: Format, centered: Bool? = nil, anchor: UnitPoint? = nil, multiLabelAlignment: Alignment? = nil, collisionResolution: AxisValueLabelCollisionResolution = .automatic, offsetsMarks: Bool? = nil, orientation: AxisValueLabelOrientation = .automatic, horizontalSpacing: CGFloat? = nil, verticalSpacing: CGFloat? = nil) where Content == Never, Format : FormatStyle, Format.FormatInput : Plottable, Format.FormatOutput == String
```

## Parameters

- `format` — The format for the text.

- `centered` — Whether to center the label between two axis values. If `nil`, default to true for discrete data, false to continuous data.

- `anchor` — The anchor point on the bounding box of the text element that attaches to the `position`.

- `multiLabelAlignment` — How labels along the axis are aligned with each other.

- `collisionResolution` — How labels that collide with others are resolved.

- `offsetsMarks` — Whether to offset marks to accomodate for the space used by the label.

- `orientation` — The orientation of the label.

- `horizontalSpacing` — The horizontal spacing of the label. If `nil`, a default spacing will be used.

- `verticalSpacing` — The vertical spacing of the label.
