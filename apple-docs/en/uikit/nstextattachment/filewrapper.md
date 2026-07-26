---
title: fileWrapper
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachment/filewrapper
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment/filewrapper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment/filewrapper.json'
content_hash: 'sha256:5e8b850d4978a115'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachment](../nstextattachment.md)

# fileWrapper

<sub>Instance Property</sub>

The text attachment’s file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var fileWrapper: FileWrapper? { get set }
```

## Discussion

The file wrapper holds the contents of the attached file. In iOS, modifying this property has a side effect of invalidating the [image](image.md), [contents](contents.md), and [fileType](filetype.md) properties.

## See Also

### Defining the attachment’s contents

- [bounds](bounds.md) — The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [contents](contents.md) — The contents for the text attachment.
- [fileType](filetype.md) — The file type of the contents for the text attachment.
- [image](image.md) — An instance of the relevant image class that represents the contents of the text attachment object.
- [allowsTextAttachmentView](allowstextattachmentview.md) — A Boolean value that determines whether the text attachment uses text attachment views.
- [usesTextAttachmentView](usestextattachmentview.md) — A Boolean value that indicates whether the text attachment uses text attachment views.
- [lineLayoutPadding](linelayoutpadding.md) — The layout padding before and after the text attachment bounds.
