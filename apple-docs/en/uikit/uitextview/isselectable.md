---
title: isSelectable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/isselectable
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/isselectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/isselectable.json'
content_hash: 'sha256:769625bb8e4dae34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# isSelectable

<sub>Instance Property</sub>

A Boolean value that indicates whether the text view is selectable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isSelectable: Bool { get set }
```

## Discussion

This property controls the ability of the user to select content and interact with URLs and text attachments. The default value is [true](../../swift/true.md).

## See Also

### Working with the selection

- [selectedRange](selectedrange.md) — The current selection range of the text view. _(deprecated)_
- [- scrollRangeToVisible:](<scrollrangetovisible(__).md>) — Scrolls the text view until the text in the specified range is visible.
- [clearsOnInsertion](clearsoninsertion.md) — A Boolean value that indicates whether inserting text replaces the previous contents.
