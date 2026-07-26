---
title: bounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachment/bounds
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/bounds.json'
content_hash: 'sha256:cac2b9247d03befc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# bounds

<sub>Instance Property</sub>

The layout bounds of the text attachment’s graphical representation in the text coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var bounds: CGRect { get set }
```

## Discussion

The bounds rectangle origin is at the current glyph location on the text baseline. The default value is [CGRectZero](../../coregraphics/cgrectzero.md).

## See Also

### Defining the attachment’s contents

- [contents](contents.md) — The contents for the text attachment.
- [fileType](filetype.md) — The file type of the contents for the text attachment.
- [image](image.md) — An instance of the relevant image class that represents the contents of the text attachment object.
- [fileWrapper](filewrapper.md) — The text attachment’s file wrapper.
- [allowsTextAttachmentView](allowstextattachmentview.md) — A Boolean value that determines whether the text attachment uses text attachment views.
- [usesTextAttachmentView](usestextattachmentview.md) — A Boolean value that indicates whether the text attachment uses text attachment views.
- [lineLayoutPadding](linelayoutpadding.md) — The layout padding before and after the text attachment bounds.
