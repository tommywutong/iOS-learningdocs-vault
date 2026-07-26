---
title: NSTextSelectionNavigation.Destination.line
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/destination/line
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destination/line'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/destination/line.json'
content_hash: 'sha256:8fbe7736e305ec48'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextSelectionNavigation](../../nstextselectionnavigation.md) · [Destination](../destination.md)

# NSTextSelectionNavigation.Destination.line

<sub>Case</sub>

The selection moves to the next line boundary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case line
```

## Discussion

The boundary of a line can be logical, based on the line separator characters, as well as visual using soft line wrapping.

## See Also

### Selection destinations

- [NSTextSelectionNavigationDestinationCharacter](character.md) — The selection moves to the next extended grapheme cluster boundary.
- [NSTextSelectionNavigationDestinationWord](word.md) — The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigationDestinationSentence](sentence.md) — The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigationDestinationParagraph](paragraph.md) — The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.
- [NSTextSelectionNavigationDestinationContainer](container.md) — The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.
- [NSTextSelectionNavigationDestinationDocument](document.md) — The selection moves to the document boundary.
