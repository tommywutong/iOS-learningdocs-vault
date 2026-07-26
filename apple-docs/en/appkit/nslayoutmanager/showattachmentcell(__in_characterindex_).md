---
title: 'showAttachmentCell(_:in:characterIndex:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/showattachmentcell(_:in:characterindex:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/showattachmentcell(_:in:characterindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/showattachmentcell%28_%3Ain%3Acharacterindex%3A%29.json'
content_hash: 'sha256:9c2a35a8e55a4348'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# showAttachmentCell(_:in:characterIndex:)

<sub>Instance Method</sub>

Draws an attachment cell.

<sub>macOS</sub>

```swift
func showAttachmentCell(_ cell: NSCell, in rect: NSRect, characterIndex attachmentIndex: Int)
```

## Parameters

- `cell` — The attachment cell to draw.

- `rect` — The rectangle within which to draw `cell`.

- `attachmentIndex` — The location of the attachment cell.

## Discussion

The `attachmentIndex` parameter is provided for cells that alter their appearance based on their location.

## See Also

### Managing attachments

- [defaultAttachmentScaling](defaultattachmentscaling.md) — The default amount of scaling to apply when an attachment image is too large to fit in a text container.
