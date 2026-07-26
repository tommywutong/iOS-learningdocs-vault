---
title: selectedRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitextview/selectedrange
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/selectedrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/selectedrange.json'
content_hash: 'sha256:fa1a056dee3cd50d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# selectedRange

<sub>Instance Property</sub>

The current selection range of the text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedRange: NSRange { get set }
```

## Discussion

In iOS 2.2 and earlier, the length of the selection range is always 0, indicating that the selection is actually an insertion point. In iOS 3.0 and later, the length of the selection range may be non-zero.

## See Also

### Working with the selection

- [- scrollRangeToVisible:](<scrollrangetovisible(__).md>) — Scrolls the text view until the text in the specified range is visible.
- [clearsOnInsertion](clearsoninsertion.md) — A Boolean value that indicates whether inserting text replaces the previous contents.
- [selectable](isselectable.md) — A Boolean value that indicates whether the text view is selectable.
