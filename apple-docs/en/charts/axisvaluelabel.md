---
title: AxisValueLabel
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axisvaluelabel
source_url: 'https://developer.apple.com/documentation/charts/axisvaluelabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axisvaluelabel.json'
content_hash: 'sha256:0b85487ef8c793ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisValueLabel

<sub>Structure</sub>

A label that describes the value for an axis mark.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AxisValueLabel<Content> where Content : View
```

## Relationships

- **Conforms To**: [AxisMark](axismark.md)

## Topics

### Supporting types

- [AxisValueLabelOrientation](axisvaluelabelorientation.md) — Describes the orientation of a label.
- [AxisValueLabelCollisionResolution](axisvaluelabelcollisionresolution.md)

### Initializers

- [init(_:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)](<axisvaluelabel/init(__centered_anchor_multilabelalignment_collisionresolution_offsetsmarks_orientation_horizontalspacing_verticalspacing_)-4xde3.md>) — Constructs an axis value label with the given properties to display the given string.
- [init(_:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)](<axisvaluelabel/init(__centered_anchor_multilabelalignment_collisionresolution_offsetsmarks_orientation_horizontalspacing_verticalspacing_)-9202h.md>) — Constructs an axis value label with the given properties to display the given string.
- [init(_:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)](<axisvaluelabel/init(__centered_anchor_multilabelalignment_collisionresolution_offsetsmarks_orientation_horizontalspacing_verticalspacing_)-9rytf.md>) — Constructs an axis value label with the given properties to display the given string.
- [init(centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)](<axisvaluelabel/init(centered_anchor_multilabelalignment_collisionresolution_offsetsmarks_orientation_horizontalspacing_verticalspacing_).md>) — Constructs axis value labels with the given properties and default text.
- [init(centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:content:)](<axisvaluelabel/init(centered_anchor_multilabelalignment_collisionresolution_offsetsmarks_orientation_horizontalspacing_verticalspacing_content_).md>) — Constructs an axis value label with the given properties to display the given content.
- [init(format:centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)](<axisvaluelabel/init(format_centered_anchor_multilabelalignment_collisionresolution_offsetsmarks_orientation_horizontalspacing_verticalspacing_).md>) — Constructs an axis value label with the given properties to display the given content.

## See Also

### Axis marks

- [AxisMark](axismark.md) — A type that serves as the basic building block for the elements of an axis.
- [AxisTick](axistick.md) — A mark that a chart draws on an axis to indicate a reference point along that axis.
- [AxisGridLine](axisgridline.md) — A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [AxisValue](axisvalue.md) — A value for an axis mark.
- [AnyAxisMark](anyaxismark.md) — A type-erased axis mark.
- [AxisMarkBuilder](axismarkbuilder.md) — A result builder that constructs axis marks and overrides default marks.
