---
title: allowsTextAttachmentView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachment/allowstextattachmentview
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/allowstextattachmentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/allowstextattachmentview.json'
content_hash: 'sha256:a234a95f267ef7d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# allowsTextAttachmentView

<sub>Instance Property</sub>

A Boolean value that determines whether the text attachment uses text attachment views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsTextAttachmentView: Bool { get set }
```

## Discussion

When `true`, the text attachment tries to use a text attachment view returned by [- viewProviderForParentView:location:textContainer:](<../nstextattachmentlayout/viewprovider(for_location_textcontainer_).md>). Default is `true`.

## See Also

### Defining the attachment’s contents

- [bounds](bounds.md) — The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [contents](contents.md) — The contents for the text attachment.
- [fileType](filetype.md) — The file type of the contents for the text attachment.
- [image](image.md) — An instance of the relevant image class that represents the contents of the text attachment object.
- [fileWrapper](filewrapper.md) — The text attachment’s file wrapper.
- [usesTextAttachmentView](usestextattachmentview.md) — A Boolean value that indicates whether the text attachment uses text attachment views.
- [lineLayoutPadding](linelayoutpadding.md) — The layout padding before and after the text attachment bounds.
