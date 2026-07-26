---
title: textView
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextcontainer/textview
source_url: 'https://developer.apple.com/documentation/appkit/nstextcontainer/textview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextcontainer/textview.json'
content_hash: 'sha256:02b1c8b072bf82af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextContainer](../nstextcontainer.md)

# textView

<sub>Instance Property</sub>

The text container’s text view.

<sub>macOS</sub>

```swift
weak var textView: NSTextView? { get set }
```

## Discussion

A text container doesn’t need a text view to calculate line fragment rectangles, but must have one to display text.

You can use this property to disconnect a text view from a group of text system objects by sending this message to its text container and passing `nil` as `aTextView`.

## See Also

### Managing text components

- [layoutManager](layoutmanager.md) — The text container’s layout manager.
- [textLayoutManager](textlayoutmanager.md)
- [- replaceLayoutManager:](<replacelayoutmanager(__).md>) — Replaces the layout manager for the group of text system objects that contains the text container.
