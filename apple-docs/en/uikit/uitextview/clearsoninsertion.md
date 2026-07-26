---
title: clearsOnInsertion
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/clearsoninsertion
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/clearsoninsertion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/clearsoninsertion.json'
content_hash: 'sha256:e5aa2e2baa5d9890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# clearsOnInsertion

<sub>Instance Property</sub>

A Boolean value that indicates whether inserting text replaces the previous contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clearsOnInsertion: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). When the value of this property is [true](../../swift/true.md) and the text view is in editing mode, the selection UI is hidden and inserting new text clears the contents of the text view and sets the value of this property back to [false](../../swift/false.md).

## See Also

### Working with the selection

- [selectedRange](selectedrange.md) — The current selection range of the text view. _(deprecated)_
- [- scrollRangeToVisible:](<scrollrangetovisible(__).md>) — Scrolls the text view until the text in the specified range is visible.
- [selectable](isselectable.md) — A Boolean value that indicates whether the text view is selectable.
