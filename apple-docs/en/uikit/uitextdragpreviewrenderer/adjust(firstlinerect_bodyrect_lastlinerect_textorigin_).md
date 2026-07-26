---
title: 'adjust(firstLineRect:bodyRect:lastLineRect:textOrigin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragpreviewrenderer/adjust(firstlinerect:bodyrect:lastlinerect:textorigin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/adjust(firstlinerect:bodyrect:lastlinerect:textorigin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragpreviewrenderer/adjust%28firstlinerect%3Abodyrect%3Alastlinerect%3Atextorigin%3A%29.json'
content_hash: 'sha256:b3be4f58cf955322'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragPreviewRenderer](../uitextdragpreviewrenderer.md)

# adjust(firstLineRect:bodyRect:lastLineRect:textOrigin:)

<sub>Instance Method</sub>

Adjusts the size and origin of the bounding rectangles during a text drag operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func adjust(firstLineRect: UnsafeMutablePointer<CGRect>, bodyRect: UnsafeMutablePointer<CGRect>, lastLineRect: UnsafeMutablePointer<CGRect>, textOrigin origin: CGPoint)
```

## Parameters

- `firstLineRect` — The bounding rectangle for the first line of text in the drag preview.

- `bodyRect` — The bounding rectangle for the text in the middle of the drag preview that doesn’t include the first and last line.

- `lastLineRect` — The bounding rectangle for the last line of text in the drag preview.

- `origin` — The origin of the text preview.

## Discussion

This method does nothing by default. Subclasses may override this method to change the rectangle calculations; for example, in order to enlarge the rectangles by a few points. If you adjust the rectangles, the drag preview changes accordingly.

## See Also

### Getting and setting bounding rectangles

- [bodyRect](bodyrect.md) — The bounding rectangle of the text in the middle of the drag preview.
- [firstLineRect](firstlinerect.md) — The bounding rectangle of the first line of text in the drag preview.
- [lastLineRect](lastlinerect.md) — The bounding rectangle of the last line of text in the drag preview.
