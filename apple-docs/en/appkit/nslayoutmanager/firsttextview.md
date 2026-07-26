---
title: firstTextView
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutmanager/firsttextview
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/firsttextview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/firsttextview.json'
content_hash: 'sha256:85a6e4a1eb4f431a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# firstTextView

<sub>Instance Property</sub>

The first text view in the layout manager’s series of text views.

<sub>macOS</sub>

```swift
unowned(unsafe) var firstTextView: NSTextView? { get }
```

## Discussion

This `NSTextView` object is the recipient of various `NSText` and `NSTextView` notifications.

## See Also

### Managing the responder chain

- [- layoutManagerOwnsFirstResponderInWindow:](<layoutmanagerownsfirstresponder(in_).md>) — Indicates whether the first responder in the specified window is a text view for the layout manager.
- [textViewForBeginningOfSelection](textviewforbeginningofselection.md) — The text view that contains the first glyph in the selection.
