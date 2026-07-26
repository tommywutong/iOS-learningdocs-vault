---
title: defaultAttachmentScaling
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutmanager/defaultattachmentscaling
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/defaultattachmentscaling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/defaultattachmentscaling.json'
content_hash: 'sha256:a4c558aaa7ec1655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# defaultAttachmentScaling

<sub>Instance Property</sub>

The default amount of scaling to apply when an attachment image is too large to fit in a text container.

<sub>macOS</sub>

```swift
var defaultAttachmentScaling: NSImageScaling { get set }
```

## Discussion

Attachment cells control their own size and drawing, so this setting is only advisory to them, but Application Kit–supplied attachment cells respect it.

## See Also

### Managing attachments

- [- showAttachmentCell:inRect:characterIndex:](<showattachmentcell(__in_characterindex_).md>) — Draws an attachment cell.
