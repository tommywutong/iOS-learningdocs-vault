---
title: 'scrollRangeToVisible(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextview/scrollrangetovisible(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/scrollrangetovisible(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/scrollrangetovisible%28_%3A%29.json'
content_hash: 'sha256:b568fa1a038ba48e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# scrollRangeToVisible(_:)

<sub>Instance Method</sub>

Scrolls the text view until the text in the specified range is visible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func scrollRangeToVisible(_ range: NSRange)
```

## Parameters

- `range` — The range of text to scroll into view.

## See Also

### Working with the selection

- [selectedRange](selectedrange.md) — The current selection range of the text view. _(deprecated)_
- [clearsOnInsertion](clearsoninsertion.md) — A Boolean value that indicates whether inserting text replaces the previous contents.
- [selectable](isselectable.md) — A Boolean value that indicates whether the text view is selectable.
