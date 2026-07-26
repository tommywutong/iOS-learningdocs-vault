---
title: lastLineRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragpreviewrenderer/lastlinerect
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/lastlinerect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragpreviewrenderer/lastlinerect.json'
content_hash: 'sha256:d1a6e3126b849ace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragPreviewRenderer](../uitextdragpreviewrenderer.md)

# lastLineRect

<sub>Instance Property</sub>

The bounding rectangle of the last line of text in the drag preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var lastLineRect: CGRect { get }
```

## Discussion

The last line rectangle contains the last line of text in the drag preview that may be a partial line. This property can be a zero rectangle. The initial value is also not calculated until the first time it’s used.

## See Also

### Getting and setting bounding rectangles

- [bodyRect](bodyrect.md) — The bounding rectangle of the text in the middle of the drag preview.
- [firstLineRect](firstlinerect.md) — The bounding rectangle of the first line of text in the drag preview.
- [- adjustFirstLineRect:bodyRect:lastLineRect:textOrigin:](<adjust(firstlinerect_bodyrect_lastlinerect_textorigin_).md>) — Adjusts the size and origin of the bounding rectangles during a text drag operation.
