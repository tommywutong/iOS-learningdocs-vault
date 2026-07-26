---
title: NSTextSelectionNavigation.Destination
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/destination
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destination'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/destination.json'
content_hash: 'sha256:62560b68180f9a30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionNavigation](../nstextselectionnavigation.md)

# NSTextSelectionNavigation.Destination

<sub>Enumeration</sub>

Values that affect how the framework handles navigation across different textual boundaries during a selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Destination
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Selection destinations

- [NSTextSelectionNavigationDestinationCharacter](destination/character.md) — The selection moves to the next extended grapheme cluster boundary.
- [NSTextSelectionNavigationDestinationWord](destination/word.md) — The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigationDestinationLine](destination/line.md) — The selection moves to the next line boundary.
- [NSTextSelectionNavigationDestinationSentence](destination/sentence.md) — The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigationDestinationParagraph](destination/paragraph.md) — The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.
- [NSTextSelectionNavigationDestinationContainer](destination/container.md) — The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.
- [NSTextSelectionNavigationDestinationDocument](destination/document.md) — The selection moves to the document boundary.

### Initializers

- [init(rawValue:)](<destination/init(rawvalue_).md>)

## See Also

### Selection characteristics

- [allowsNonContiguousRanges](allowsnoncontiguousranges.md) — Determines if the instance could produce selections with multiple noncontiguous selections.
- [rotatesCoordinateSystemForLayoutOrientation](rotatescoordinatesystemforlayoutorientation.md) — Determines if the framework rotates the coordinate system to match the layout orientation.
- [Modifier](modifier.md) — Values that describe how the framework handles different kinds of selection modifiers.
- [Direction](direction.md) — Values that describe the direction of a selection.
- [- textSelectionForSelectionGranularity:enclosingPoint:inContainerAtLocation:](<textselection(for_enclosing_incontainerat_).md>) — Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.
