---
title: affinity
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselection/affinity-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/affinity-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/affinity-swift.property.json'
content_hash: 'sha256:02448588ebcfeda0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# affinity

<sub>Instance Property</sub>

Returns the selection affinity of the text selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var affinity: NSTextSelection.Affinity { get }
```

## Discussion

The affinity is [NSTextSelectionAffinityDownstream](affinity-swift.enum/downstream.md) by default. For a zero-length selection, it describes the visual location of the text cursor between the head of line containing the selection location (downstream) or tail of the previous line (upstream). For a selection with contents, it describes the logical direction of non-anchored edge of the selection.

## See Also

### Characteristics of a selection

- [Affinity](affinity-swift.enum.md) — Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [anchorPositionOffset](anchorpositionoffset.md) — Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [granularity](granularity-swift.property.md) — The granularity of the selection.
- [Granularity](granularity-swift.enum.md) — Values that describe the different granularities available to make a selection.
- [logical](islogical.md) — A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [transient](istransient.md) — A Boolean value that indicates transient text selection during drag handling.
- [secondarySelectionLocation](secondaryselectionlocation.md) — Specifies the secondary character location when user taps or clicks at a directional boundary.
- [NSTextLocation](../nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
- [textRanges](textranges.md) — Represents an array of noncontiguous logical ranges in the selection.
- [typingAttributes](typingattributes.md) — The template attributes the framework uses for characters that replace the contents of this selection.
