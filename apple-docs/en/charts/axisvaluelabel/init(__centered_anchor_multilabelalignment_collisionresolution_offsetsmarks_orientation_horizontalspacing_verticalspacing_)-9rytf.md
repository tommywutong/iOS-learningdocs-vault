---
title: 'init(_:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/axisvaluelabel/init(_:centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:)-9rytf'
source_url: 'https://developer.apple.com/documentation/charts/axisvaluelabel/init(_:centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:)-9rytf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axisvaluelabel/init%28_%3Acentered%3Aanchor%3Amultilabelalignment%3Acollisionresolution%3Aoffsetsmarks%3Aorientation%3Ahorizontalspacing%3Averticalspacing%3A%29-9rytf.json'
content_hash: 'sha256:8545ff7d13f0a2de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AxisValueLabel](../axisvaluelabel.md)

# init(_:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)

<sub>Initializer</sub>

Constructs an axis value label with the given properties to display the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<S>(_ title: S, centered: Bool? = nil, anchor: UnitPoint? = nil, multiLabelAlignment: Alignment? = nil, collisionResolution: AxisValueLabelCollisionResolution = .automatic, offsetsMarks: Bool? = nil, orientation: AxisValueLabelOrientation = .automatic, horizontalSpacing: CGFloat? = nil, verticalSpacing: CGFloat? = nil) where Content == Text, S : StringProtocol
```

## Parameters

- `title` — A title generated from a string.

- `centered` — Whether to center the label between two axis values. If `nil`, default to true for discrete data, false to continuous data.

- `anchor` — The anchor point on the bounding box of the text element that attaches to the `position`.

- `multiLabelAlignment` — How labels along the axis are aligned with each other.

- `collisionResolution` — How labels that collide with others are resolved.

- `offsetsMarks` — Whether to offset marks to accomodate for the space used by the label.

- `orientation` — The orientation of the label.

- `horizontalSpacing` — The horizontal spacing of the label. If `nil`, a default spacing will be used.

- `verticalSpacing` — The vertical spacing of the label.
