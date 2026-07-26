---
title: textLayoutManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachmentviewprovider/textlayoutmanager
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/textlayoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentviewprovider/textlayoutmanager.json'
content_hash: 'sha256:4c4a088629607d55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentViewProvider](../nstextattachmentviewprovider.md)

# textLayoutManager

<sub>Instance Property</sub>

The text layout manager for this view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var textLayoutManager: NSTextLayoutManager? { get }
```

## Discussion

Specify the value of this property at initialization time using the [- initWithTextAttachment:parentView:textLayoutManager:location:](<init(textattachment_parentview_textlayoutmanager_location_).md>) initializer.

## See Also

### Defining the contents

- [location](location.md) — The location that indicates the start of the text attachment.
- [textAttachment](textattachment.md) — The text attachment for this view.
- [tracksTextAttachmentViewBounds](trackstextattachmentviewbounds.md) — A Boolean value that determines the text attachment’s bounds policy.
- [view](view.md) — The text attachment’s view.
