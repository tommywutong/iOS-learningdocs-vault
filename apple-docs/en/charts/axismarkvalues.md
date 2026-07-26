---
title: AxisMarkValues
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/axismarkvalues
source_url: 'https://developer.apple.com/documentation/charts/axismarkvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/axismarkvalues.json'
content_hash: 'sha256:ac7563000971e472'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AxisMarkValues

<sub>Structure</sub>

Describes the values the axis markers will present (one for each value).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AxisMarkValues
```

## Relationships

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md)

## Topics

### Type Properties

- [automatic](axismarkvalues/automatic.md) — Automatically determines the values for the markers of the axis.

### Type Methods

- [automatic(desiredCount:roundLowerBound:roundUpperBound:)](<axismarkvalues/automatic(desiredcount_roundlowerbound_roundupperbound_).md>) — Automatically determines the values for the markers, approximating the target number of values.
- [automatic(minimumStride:desiredCount:roundLowerBound:roundUpperBound:)](<axismarkvalues/automatic(minimumstride_desiredcount_roundlowerbound_roundupperbound_).md>)
- [stride(by:count:roundLowerBound:roundUpperBound:calendar:)](<axismarkvalues/stride(by_count_roundlowerbound_roundupperbound_calendar_).md>) — Creates values with the given calendar unit.
- [stride(by:roundLowerBound:roundUpperBound:)](<axismarkvalues/stride(by_roundlowerbound_roundupperbound_).md>) — Creates values with the given number step.

## See Also

### Supporting types

- [AxisMarkPreset](axismarkpreset.md) — Describes preset styles for axis markers.
- [AxisMarkPosition](axismarkposition.md) — Describes the position of axis markers.
