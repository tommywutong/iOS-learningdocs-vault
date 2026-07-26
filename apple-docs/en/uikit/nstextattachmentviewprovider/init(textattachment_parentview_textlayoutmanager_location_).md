---
title: 'init(textAttachment:parentView:textLayoutManager:location:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextattachmentviewprovider/init(textattachment:parentview:textlayoutmanager:location:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachmentviewprovider/init(textattachment:parentview:textlayoutmanager:location:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachmentviewprovider/init%28textattachment%3Aparentview%3Atextlayoutmanager%3Alocation%3A%29.json'
content_hash: 'sha256:a1e07ed0619e3167'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextAttachmentViewProvider](../nstextattachmentviewprovider.md)

# init(textAttachment:parentView:textLayoutManager:location:)

<sub>Initializer</sub>

Creates a new text attachment view whose content starts at the location you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(textAttachment: NSTextAttachment, parentView: UIView?, textLayoutManager: NSTextLayoutManager?, location: any NSTextLocation)
```

## Parameters

- `textAttachment` — The [NSTextAttachment](../nstextattachment.md) for this view.

- `parentView` — The parent view of this attachment.

- `textLayoutManager` — The [NSTextLayoutManager](../nstextlayoutmanager.md) for this view.

- `location` — The [NSTextLocation](../nstextlocation.md) that identifies the start of the text.
