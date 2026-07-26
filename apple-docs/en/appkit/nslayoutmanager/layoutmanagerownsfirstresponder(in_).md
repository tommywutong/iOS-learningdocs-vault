---
title: 'layoutManagerOwnsFirstResponder(in:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/layoutmanagerownsfirstresponder(in:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/layoutmanagerownsfirstresponder(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/layoutmanagerownsfirstresponder%28in%3A%29.json'
content_hash: 'sha256:d8795590ebfcb9bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# layoutManagerOwnsFirstResponder(in:)

<sub>Instance Method</sub>

Indicates whether the first responder in the specified window is a text view for the layout manager.

<sub>macOS</sub>

```swift
func layoutManagerOwnsFirstResponder(in window: NSWindow) -> Bool
```

## Parameters

- `window` — The window whose first responder is tested.

## Return Value

[true](../../swift/true.md) if the first responder in `window` is a text view associated with the receiver; otherwise, [false](../../swift/false.md).

## See Also

### Managing the responder chain

- [firstTextView](firsttextview.md) — The first text view in the layout manager’s series of text views.
- [textViewForBeginningOfSelection](textviewforbeginningofselection.md) — The text view that contains the first glyph in the selection.
