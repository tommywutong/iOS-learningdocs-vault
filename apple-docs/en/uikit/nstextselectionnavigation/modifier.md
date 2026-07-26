---
title: NSTextSelectionNavigation.Modifier
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/modifier
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/modifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/modifier.json'
content_hash: 'sha256:d9ade71974ccf42a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# NSTextSelectionNavigation.Modifier

<sub>Structure</sub>

Values that describe how the framework handles different kinds of selection modifiers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Modifier
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a navigation modifier

- [init(rawValue:)](<modifier/init(rawvalue_).md>) — Creates a new navigation modifier using a raw value.

### Navigation modifier characteristics

- [NSTextSelectionNavigationModifierExtend](modifier/extend.md) — The value that indicates the framework extends the selection by not moving the initial location while in a drag selection.
- [NSTextSelectionNavigationModifierMultiple](modifier/multiple.md) — The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and dragged positions.
- [NSTextSelectionNavigationModifierVisual](modifier/visual.md) — The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and drag positions.

## See Also

### Selection characteristics

- [allowsNonContiguousRanges](allowsnoncontiguousranges.md) — Determines if the instance could produce selections with multiple noncontiguous selections.
- [rotatesCoordinateSystemForLayoutOrientation](rotatescoordinatesystemforlayoutorientation.md) — Determines if the framework rotates the coordinate system to match the layout orientation.
- [Destination](destination.md) — Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [Direction](direction.md) — Values that describe the direction of a selection.
- [- textSelectionForSelectionGranularity:enclosingPoint:inContainerAtLocation:](<textselection(for_enclosing_incontainerat_).md>) — Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.
