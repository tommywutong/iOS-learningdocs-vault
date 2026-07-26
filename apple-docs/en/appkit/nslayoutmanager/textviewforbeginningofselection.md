---
title: textViewForBeginningOfSelection
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutmanager/textviewforbeginningofselection
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/textviewforbeginningofselection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/textviewforbeginningofselection.json'
content_hash: 'sha256:3392c62307cfb618'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# textViewForBeginningOfSelection

<sub>Instance Property</sub>

The text view that contains the first glyph in the selection.

<sub>macOS</sub>

```swift
unowned(unsafe) var textViewForBeginningOfSelection: NSTextView? { get }
```

## Discussion

This property does not cause layout if the beginning of the selected range is not yet laid out.

## See Also

### Managing the responder chain

- [- layoutManagerOwnsFirstResponderInWindow:](<layoutmanagerownsfirstresponder(in_).md>) — Indicates whether the first responder in the specified window is a text view for the layout manager.
- [firstTextView](firsttextview.md) — The first text view in the layout manager’s series of text views.
