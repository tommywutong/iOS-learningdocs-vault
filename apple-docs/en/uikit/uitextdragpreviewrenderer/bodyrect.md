---
title: bodyRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragpreviewrenderer/bodyrect
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/bodyrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragpreviewrenderer/bodyrect.json'
content_hash: 'sha256:5696765e4066bdd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragPreviewRenderer](../uitextdragpreviewrenderer.md)

# bodyRect

<sub>Instance Property</sub>

The bounding rectangle of the text in the middle of the drag preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var bodyRect: CGRect { get }
```

## Discussion

The body rectangle contains the full lines of text in the middle of the drag preview that doesn’t include the first line and last line. This property can be a zero rectangle. The initial value is also not calculated until the first time it’s used.

## See Also

### Getting and setting bounding rectangles

- [firstLineRect](firstlinerect.md) — The bounding rectangle of the first line of text in the drag preview.
- [lastLineRect](lastlinerect.md) — The bounding rectangle of the last line of text in the drag preview.
- [- adjustFirstLineRect:bodyRect:lastLineRect:textOrigin:](<adjust(firstlinerect_bodyrect_lastlinerect_textorigin_).md>) — Adjusts the size and origin of the bounding rectangles during a text drag operation.
