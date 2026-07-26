---
title: tracksTextAttachmentViewBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachmentviewprovider/trackstextattachmentviewbounds
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/trackstextattachmentviewbounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentviewprovider/trackstextattachmentviewbounds.json'
content_hash: 'sha256:6cf34cc5f96837af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentViewProvider](../nstextattachmentviewprovider.md)

# tracksTextAttachmentViewBounds

<sub>Instance Property</sub>

A Boolean value that determines the text attachment’s bounds policy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tracksTextAttachmentViewBounds: Bool { get set }
```

## Discussion

If `true`, the framework calls the `textAttachment` property’s [- attachmentBoundsForAttributes:location:textContainer:proposedLineFragment:position:](<attachmentbounds(for_location_textcontainer_proposedlinefragment_position_).md>) method and examines the text attachment view provider to determine the bounds instead of using the `bounds` property of this instance. Defaults to `false`.

## See Also

### Defining the contents

- [location](location.md) — The location that indicates the start of the text attachment.
- [textAttachment](textattachment.md) — The text attachment for this view.
- [textLayoutManager](textlayoutmanager.md) — The text layout manager for this view.
- [view](view.md) — The text attachment’s view.
