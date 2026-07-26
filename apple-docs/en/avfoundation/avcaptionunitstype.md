---
title: AVCaptionUnitsType
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionunitstype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionunitstype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionunitstype.json'
content_hash: 'sha256:cb4a14dbaadd7087'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptionUnitsType

<sub>Enumeration</sub>

A structure that defines a units for caption formats.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum AVCaptionUnitsType
```

## Overview

Some geometry values may use sizing and positioning with different units. In some cases, an object might allow multiple kinds of dimensions varying by units.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Unit types

- [AVCaptionUnitsTypeCells](avcaptionunitstype/cells.md) — A cell-based unit type.
- [AVCaptionUnitsTypePercent](avcaptionunitstype/percent.md) — A percentage-based unit type.
- [AVCaptionUnitsTypeUnspecified](avcaptionunitstype/unspecified.md) — An unspecified unit type.

### Initializers

- [init(rawValue:)](<avcaptionunitstype/init(rawvalue_).md>)

## See Also

### Inspecting the dimensions

- [value](avcaptiondimension/value.md) — The value of the coordinate or length.
- [units](avcaptiondimension/units.md) — The units of the coordinate, such as cells or points.
