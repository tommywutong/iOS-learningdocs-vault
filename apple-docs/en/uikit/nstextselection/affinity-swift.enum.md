---
title: NSTextSelection.Affinity
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselection/affinity-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/affinity-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/affinity-swift.enum.json'
content_hash: 'sha256:ab39dd3a7a7a2eab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# NSTextSelection.Affinity

<sub>Enumeration</sub>

Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Affinity
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Affinities

- [NSTextSelectionAffinityDownstream](affinity-swift.enum/downstream.md) — The value that defines the visual location of the text cursor between the head of line that contains the selection location.
- [NSTextSelectionAffinityUpstream](affinity-swift.enum/upstream.md) — The value that defines the visual location of the text cursor to the tail of the previous line.

### Initializers

- [init(rawValue:)](<affinity-swift.enum/init(rawvalue_).md>)

## See Also

### Characteristics of a selection

- [affinity](affinity-swift.property.md) — Returns the selection affinity of the text selection.
- [anchorPositionOffset](anchorpositionoffset.md) — Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [granularity](granularity-swift.property.md) — The granularity of the selection.
- [Granularity](granularity-swift.enum.md) — Values that describe the different granularities available to make a selection.
- [logical](islogical.md) — A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [transient](istransient.md) — A Boolean value that indicates transient text selection during drag handling.
- [secondarySelectionLocation](secondaryselectionlocation.md) — Specifies the secondary character location when user taps or clicks at a directional boundary.
- [NSTextLocation](../nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
- [textRanges](textranges.md) — Represents an array of noncontiguous logical ranges in the selection.
- [typingAttributes](typingattributes.md) — The template attributes the framework uses for characters that replace the contents of this selection.
