---
title: AxisValueLabelCollisionResolution
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axisvaluelabelcollisionresolution
source_url: 'https://developer.apple.com/documentation/charts/axisvaluelabelcollisionresolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axisvaluelabelcollisionresolution.json'
content_hash: 'sha256:7d8641c3f9fa2a06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisValueLabelCollisionResolution

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AxisValueLabelCollisionResolution
```

## Relationships

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md)

## Topics

### Type Properties

- [automatic](axisvaluelabelcollisionresolution/automatic.md) — Automatically determine the prevention method based on axis type and data.
- [disabled](axisvaluelabelcollisionresolution/disabled.md) — Do not apply collision resolution to this label. The label will always be displayed.
- [greedy](axisvaluelabelcollisionresolution/greedy.md) — Use a greedy algorithm. Display a label if it’s not overlapping with other labels.
- [truncate](axisvaluelabelcollisionresolution/truncate.md) — Truncate a label to the space available to it.

### Type Methods

- [greedy(priority:minimumSpacing:)](<axisvaluelabelcollisionresolution/greedy(priority_minimumspacing_).md>) — Use a greedy algorithm. Display a label if it’s not overlapping with other labels.

## See Also

### Supporting types

- [AxisValueLabelOrientation](axisvaluelabelorientation.md) — Describes the orientation of a label.
