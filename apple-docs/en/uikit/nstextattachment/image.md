---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachment/image
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/image.json'
content_hash: 'sha256:de51bd293de3000f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# image

<sub>Instance Property</sub>

An instance of the relevant image class that represents the contents of the text attachment object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var image: UIImage? { get set }
```

## Discussion

For details about using the [UIImage](../uiimage.md) class to create text attachments that automatically adjust to surrounding font and color attributes, see the [+ textAttachmentWithImage:](<init(image_).md>) initializer.

## See Also

### Defining the attachment’s contents

- [bounds](bounds.md) — The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [contents](contents.md) — The contents for the text attachment.
- [fileType](filetype.md) — The file type of the contents for the text attachment.
- [fileWrapper](filewrapper.md) — The text attachment’s file wrapper.
- [allowsTextAttachmentView](allowstextattachmentview.md) — A Boolean value that determines whether the text attachment uses text attachment views.
- [usesTextAttachmentView](usestextattachmentview.md) — A Boolean value that indicates whether the text attachment uses text attachment views.
- [lineLayoutPadding](linelayoutpadding.md) — The layout padding before and after the text attachment bounds.
