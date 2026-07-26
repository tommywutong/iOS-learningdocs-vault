---
title: NSTextSelectionNavigation.Destination.character
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/destination/character
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destination/character'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/destination/character.json'
content_hash: 'sha256:59d6897e21bc92e2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextSelectionNavigation](../../nstextselectionnavigation.md) · [Destination](../destination.md)

# NSTextSelectionNavigation.Destination.character

<sub>Case</sub>

The selection moves to the next extended grapheme cluster boundary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case character
```

## Discussion

When the movement direction isn’t along the line (for example up and down for a horizontal line), it moves to the adjacent line using the anchor point instead of resolving to the logical direction. This could result in a location inside a cluster depending on the specific characteristics of a given script.  For example, certain Indic scripts combine characters in specific ways depending on usage and position to form composite characters. The framework returns a location consistent with the rules of the script and the direction of movement.

## See Also

### Selection destinations

- [NSTextSelectionNavigationDestinationWord](word.md) — The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigationDestinationLine](line.md) — The selection moves to the next line boundary.
- [NSTextSelectionNavigationDestinationSentence](sentence.md) — The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigationDestinationParagraph](paragraph.md) — The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.
- [NSTextSelectionNavigationDestinationContainer](container.md) — The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.
- [NSTextSelectionNavigationDestinationDocument](document.md) — The selection moves to the document boundary.
