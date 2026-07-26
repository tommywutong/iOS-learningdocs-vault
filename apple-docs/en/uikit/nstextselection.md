---
title: NSTextSelection
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselection
source_url: 'https://developer.apple.com/documentation/uikit/nstextselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselection.json'
content_hash: 'sha256:c9097d7cadb8bc15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextSelection

<sub>Class</sub>

A class that represents a single logical selection context that corresponds to an insertion point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextSelection
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a text selection

- [- initWithLocation:affinity:](<nstextselection/init(__affinity_).md>) — Creates a new text selection with the location and selection affinity you provide.
- [- initWithRange:affinity:granularity:](<nstextselection/init(range_affinity_granularity_).md>) — Creates a new text selection with the range, selection affinity, and granularity you provide.
- [- initWithRanges:affinity:granularity:](<nstextselection/init(__affinity_granularity_).md>) — Creates a new text selection with the ranges, selection affinity, and granularity you provide.
- [- initWithCoder:](<nstextselection/init(coder_).md>) — Creates a test selection from data in an unarchiver.

### Characteristics of a selection

- [affinity](nstextselection/affinity-swift.property.md) — Returns the selection affinity of the text selection.
- [Affinity](nstextselection/affinity-swift.enum.md) — Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [anchorPositionOffset](nstextselection/anchorpositionoffset.md) — Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [granularity](nstextselection/granularity-swift.property.md) — The granularity of the selection.
- [Granularity](nstextselection/granularity-swift.enum.md) — Values that describe the different granularities available to make a selection.
- [logical](nstextselection/islogical.md) — A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [transient](nstextselection/istransient.md) — A Boolean value that indicates transient text selection during drag handling.
- [secondarySelectionLocation](nstextselection/secondaryselectionlocation.md) — Specifies the secondary character location when user taps or clicks at a directional boundary.
- [NSTextLocation](nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
- [textRanges](nstextselection/textranges.md) — Represents an array of noncontiguous logical ranges in the selection.
- [typingAttributes](nstextselection/typingattributes.md) — The template attributes the framework uses for characters that replace the contents of this selection.

### Creating subselections

- [- textSelectionWithTextRanges:](<nstextselection/textselection(__).md>) — Creates a subselection of the current text selection with the ranges you specify.

### Initializers

- [init(location:affinity:)](<nstextselection/init(location_affinity_).md>)
- [init(ranges:affinity:granularity:)](<nstextselection/init(ranges_affinity_granularity_).md>)

## See Also

### Location and selection

- [NSTextRange](nstextrange.md) — A class that represents a contiguous range between two locations inside document contents.
- [NSTextSelectionNavigation](nstextselectionnavigation.md) — An interface you use to expose methods for obtaining results from actions performed on text selections.
- [NSTextLocation](nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
