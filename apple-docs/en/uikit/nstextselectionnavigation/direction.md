---
title: NSTextSelectionNavigation.Direction
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/direction
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/direction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/direction.json'
content_hash: 'sha256:5a8edf4212b0f9b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# NSTextSelectionNavigation.Direction

<sub>Enumeration</sub>

Values that describe the direction of a selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Direction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Navigation directions

- [NSTextSelectionNavigationDirectionForward](direction/forward.md) — The value that represents a logical forward selection based on the flow of text stored in the document.
- [NSTextSelectionNavigationDirectionBackward](direction/backward.md) — The value that represents a backward selection based on the flow of text stored in the document.
- [NSTextSelectionNavigationDirectionLeft](direction/left.md) — The value that represents a selection in the left direction along the current line.
- [NSTextSelectionNavigationDirectionRight](direction/right.md) — The value that represents a selection in the right direction along the current line.
- [NSTextSelectionNavigationDirectionUp](direction/up.md) — The value that represents a selection in the up direction, above the current line.
- [NSTextSelectionNavigationDirectionDown](direction/down.md) — The value that represents a selection in the down direction, below the current line.

### Initializers

- [init(rawValue:)](<direction/init(rawvalue_).md>)

## See Also

### Selection characteristics

- [allowsNonContiguousRanges](allowsnoncontiguousranges.md) — Determines if the instance could produce selections with multiple noncontiguous selections.
- [rotatesCoordinateSystemForLayoutOrientation](rotatescoordinatesystemforlayoutorientation.md) — Determines if the framework rotates the coordinate system to match the layout orientation.
- [Modifier](modifier.md) — Values that describe how the framework handles different kinds of selection modifiers.
- [Destination](destination.md) — Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [- textSelectionForSelectionGranularity:enclosingPoint:inContainerAtLocation:](<textselection(for_enclosing_incontainerat_).md>) — Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.
