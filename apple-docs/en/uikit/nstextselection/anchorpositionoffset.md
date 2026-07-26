---
title: anchorPositionOffset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselection/anchorpositionoffset
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/anchorpositionoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/anchorpositionoffset.json'
content_hash: 'sha256:5fed267d4c1bd9ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# anchorPositionOffset

<sub>Instance Property</sub>

Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var anchorPositionOffset: CGFloat { get set }
```

## Discussion

That starts from the left for a horizontal line fragment, and from the top for a vertical. Navigating between lines uses this point when the current line fragment associated with the selection is shorter than the next line visited. Defaults to `0.0`.

## See Also

### Characteristics of a selection

- [affinity](affinity-swift.property.md) — Returns the selection affinity of the text selection.
- [Affinity](affinity-swift.enum.md) — Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [granularity](granularity-swift.property.md) — The granularity of the selection.
- [Granularity](granularity-swift.enum.md) — Values that describe the different granularities available to make a selection.
- [logical](islogical.md) — A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [transient](istransient.md) — A Boolean value that indicates transient text selection during drag handling.
- [secondarySelectionLocation](secondaryselectionlocation.md) — Specifies the secondary character location when user taps or clicks at a directional boundary.
- [NSTextLocation](../nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
- [textRanges](textranges.md) — Represents an array of noncontiguous logical ranges in the selection.
- [typingAttributes](typingattributes.md) — The template attributes the framework uses for characters that replace the contents of this selection.
