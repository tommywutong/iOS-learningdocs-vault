---
title: NSTextSelection.Granularity
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselection/granularity-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection/granularity-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection/granularity-swift.enum.json'
content_hash: 'sha256:434595474c0ce24c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelection](../nstextselection.md)

# NSTextSelection.Granularity

<sub>Enumeration</sub>

Values that describe the different granularities available to make a selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Granularity
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Degrees of granularity

- [NSTextSelectionGranularityCharacter](granularity-swift.enum/character.md) — A value that represents selection by character.
- [NSTextSelectionGranularityWord](granularity-swift.enum/word.md) — A value that represents selection by word.
- [NSTextSelectionGranularityParagraph](granularity-swift.enum/paragraph.md) — A value that represents selection by paragraph.
- [NSTextSelectionGranularityLine](granularity-swift.enum/line.md) — A value that represents selection by line.
- [NSTextSelectionGranularitySentence](granularity-swift.enum/sentence.md) — A value that represents selection by sentence.

### Initializers

- [init(rawValue:)](<granularity-swift.enum/init(rawvalue_).md>)

## See Also

### Characteristics of a selection

- [affinity](affinity-swift.property.md) — Returns the selection affinity of the text selection.
- [Affinity](affinity-swift.enum.md) — Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [anchorPositionOffset](anchorpositionoffset.md) — Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [granularity](granularity-swift.property.md) — The granularity of the selection.
- [logical](islogical.md) — A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [transient](istransient.md) — A Boolean value that indicates transient text selection during drag handling.
- [secondarySelectionLocation](secondaryselectionlocation.md) — Specifies the secondary character location when user taps or clicks at a directional boundary.
- [NSTextLocation](../nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
- [textRanges](textranges.md) — Represents an array of noncontiguous logical ranges in the selection.
- [typingAttributes](typingattributes.md) — The template attributes the framework uses for characters that replace the contents of this selection.
