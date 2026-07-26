---
title: lineLayoutPadding
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachment/linelayoutpadding
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/linelayoutpadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/linelayoutpadding.json'
content_hash: 'sha256:f63b30e74fef7ec3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# lineLayoutPadding

<sub>Instance Property</sub>

The layout padding before and after the text attachment bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var lineLayoutPadding: CGFloat { get set }
```

## Discussion

The layout and rendering bounds X origin is inset by the padding value. This affects the relationship between the text attachment bounds and `NSLayoutManager` glyph metrics methods [- locationForGlyphAtIndex:](<../nslayoutmanager/location(forglyphat_).md>) and [- attachmentSizeForGlyphAtIndex:](<../nslayoutmanager/attachmentsize(forglyphat_).md>). The default value is `0.0`.

## See Also

### Defining the attachment’s contents

- [bounds](bounds.md) — The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [contents](contents.md) — The contents for the text attachment.
- [fileType](filetype.md) — The file type of the contents for the text attachment.
- [image](image.md) — An instance of the relevant image class that represents the contents of the text attachment object.
- [fileWrapper](filewrapper.md) — The text attachment’s file wrapper.
- [allowsTextAttachmentView](allowstextattachmentview.md) — A Boolean value that determines whether the text attachment uses text attachment views.
- [usesTextAttachmentView](usestextattachmentview.md) — A Boolean value that indicates whether the text attachment uses text attachment views.
