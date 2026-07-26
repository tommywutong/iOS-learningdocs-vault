---
title: NSTextSelectionNavigation.Destination.container
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/destination/container
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/destination/container'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/destination/container.json'
content_hash: 'sha256:dc6f4d494309708f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextSelectionNavigation](../../nstextselectionnavigation.md) · [Destination](../destination.md)

# NSTextSelectionNavigation.Destination.container

<sub>Case</sub>

The selection moves to the next container or page boundary after boundary of the current container, ignoring the end of line elastic characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case container
```

## See Also

### Selection destinations

- [NSTextSelectionNavigationDestinationCharacter](character.md) — The selection moves to the next extended grapheme cluster boundary.
- [NSTextSelectionNavigationDestinationWord](word.md) — The selection moves to the next word boundary ignoring punctuation, whitespace, and format characters preceding the next word.
- [NSTextSelectionNavigationDestinationLine](line.md) — The selection moves to the next line boundary.
- [NSTextSelectionNavigationDestinationSentence](sentence.md) — The selection moves to the next sentence boundary, ignoring punctuation, whitespace, and format characters preceding the next sentence.
- [NSTextSelectionNavigationDestinationParagraph](paragraph.md) — The selection moves to the next paragraph boundary, ignoring the end of line elastic characters and paragraph separators.
- [NSTextSelectionNavigationDestinationDocument](document.md) — The selection moves to the document boundary.
