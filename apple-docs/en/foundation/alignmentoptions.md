---
title: AlignmentOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/alignmentoptions
source_url: 'https://developer.apple.com/documentation/foundation/alignmentoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/alignmentoptions.json'
content_hash: 'sha256:16a3cb358f6012ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AlignmentOptions

<sub>Structure</sub>

Values representing alignment operations.

<sub>Mac Catalyst, macOS</sub>

```swift
struct AlignmentOptions
```

## Overview

These constants are used by the [NSIntegralRectWithOptions](<nsintegralrectwithoptions(____).md>) function and other related methods, such as [backingAlignedRect(_:options:)](<../appkit/nsview/backingalignedrect(__options_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [NSAlignMinXInward](alignmentoptions/alignminxinward.md) — Specifies that alignment of the minimum X coordinate should be to the nearest inward integral value.
- [NSAlignMinYInward](alignmentoptions/alignminyinward.md) — Specifies that alignment of the minimum Y coordinate should be to the nearest inward integral value.
- [NSAlignMaxXInward](alignmentoptions/alignmaxxinward.md) — Specifies that alignment of the maximum X coordinate should be to the nearest inward integral value.
- [NSAlignMaxYInward](alignmentoptions/alignmaxyinward.md) — Specifies that alignment of the maximum X coordinate should be to the nearest inward integral value.
- [NSAlignWidthInward](alignmentoptions/alignwidthinward.md) — Specifies that alignment of the width should be to the nearest inward integral value.
- [NSAlignHeightInward](alignmentoptions/alignheightinward.md) — Specifies that alignment of the height should be to the nearest inward integral value.
- [NSAlignMinXOutward](alignmentoptions/alignminxoutward.md) — Specifies that alignment of the minimum X coordinate should be to the nearest outward integral value.
- [NSAlignMinYOutward](alignmentoptions/alignminyoutward.md) — Specifies that alignment of the minimum Y coordinate should be to the nearest outward integral value.
- [NSAlignMaxXOutward](alignmentoptions/alignmaxxoutward.md) — Specifies that alignment of the maximum X coordinate should be to the nearest outward integral value.
- [NSAlignMaxYOutward](alignmentoptions/alignmaxyoutward.md) — Specifies that alignment of the maximum Y coordinate should be to the nearest outward integral value.
- [NSAlignWidthOutward](alignmentoptions/alignwidthoutward.md) — Specifies that alignment of the width should be to the nearest outward integral value.
- [NSAlignHeightOutward](alignmentoptions/alignheightoutward.md) — Specifies that alignment of the height should be to the nearest outward integral value.
- [NSAlignMinXNearest](alignmentoptions/alignminxnearest.md) — Specifies that alignment of the minimum X coordinate should be to the nearest integral value.
- [NSAlignMinYNearest](alignmentoptions/alignminynearest.md) — Specifies that alignment of the minimum Y coordinate should be to the nearest integral value.
- [NSAlignMaxXNearest](alignmentoptions/alignmaxxnearest.md) — Specifies that alignment of the maximum X coordinate should be to the nearest integral value.
- [NSAlignMaxYNearest](alignmentoptions/alignmaxynearest.md) — Specifies that alignment of the maximum Y coordinate should be to the nearest integral value.
- [NSAlignWidthNearest](alignmentoptions/alignwidthnearest.md) — Specifies that alignment of the width should be to the nearest integral value.
- [NSAlignHeightNearest](alignmentoptions/alignheightnearest.md) — Specifies that alignment of the height should be to the nearest integral value.
- [NSAlignRectFlipped](alignmentoptions/alignrectflipped.md) — This option should be included  if the rectangle is in a flipped coordinate system. This allows 0.5 to be treated in a visually consistent way.
- [NSAlignAllEdgesInward](alignmentoptions/alignalledgesinward.md) — Aligns all edges inward. This is the same as `NSAlignMinXInward|NSAlignMaxXInward|NSAlignMinYInward|NSAlignMaxYInward`.
- [NSAlignAllEdgesOutward](alignmentoptions/alignalledgesoutward.md) — Aligns all edges outwards. This is the same as `NSAlignMinXOutward|NSAlignMaxXOutward|NSAlignMinYOutward|NSAlignMaxYOutward`.
- [NSAlignAllEdgesNearest](alignmentoptions/alignalledgesnearest.md) — Aligns all edges to the nearest value. This is the same as `NSAlignMinXNearest|NSAlignMaxXNearest|NSAlignMinYNearest|NSAlignMaxYNearest`.

### Initializers

- [init(rawValue:)](<alignmentoptions/init(rawvalue_).md>)

## See Also

### Related Types

- [NSRectEdge](nsrectedge.md)
- [NSRectArray](nsrectarray.md) — Type indicating a parameter is array of `NSRect` structures.
- [NSRectPointer](nsrectpointer.md) — Type indicating a parameter is a pointer to an `NSRect` structure.
