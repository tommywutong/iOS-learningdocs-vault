---
title: allowsNonContiguousRanges
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/allowsnoncontiguousranges
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/allowsnoncontiguousranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/allowsnoncontiguousranges.json'
content_hash: 'sha256:d2951733ab232ea7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# allowsNonContiguousRanges

<sub>Instance Property</sub>

Determines if the instance could produce selections with multiple noncontiguous selections.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsNonContiguousRanges: Bool { get set }
```

## See Also

### Selection characteristics

- [rotatesCoordinateSystemForLayoutOrientation](rotatescoordinatesystemforlayoutorientation.md) — Determines if the framework rotates the coordinate system to match the layout orientation.
- [Modifier](modifier.md) — Values that describe how the framework handles different kinds of selection modifiers.
- [Destination](destination.md) — Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [Direction](direction.md) — Values that describe the direction of a selection.
- [- textSelectionForSelectionGranularity:enclosingPoint:inContainerAtLocation:](<textselection(for_enclosing_incontainerat_).md>) — Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.
