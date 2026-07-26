---
title: 'textLayoutManager(_:retrieveCachedTextAttachmentViewProviderFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:retrievecachedtextattachmentviewproviderfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager%28_%3Aretrievecachedtextattachmentviewproviderfor%3A%29.json'
content_hash: 'sha256:2c693f498ece00fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManagerDelegate](../nstextlayoutmanagerdelegate.md)

# textLayoutManager(_:retrieveCachedTextAttachmentViewProviderFor:)

<sub>Instance Method</sub>

Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, retrieveCachedTextAttachmentViewProviderFor attachment: NSTextAttachment) -> NSTextAttachmentViewProvider?
```

## Parameters

- `textLayoutManager` — The text layout manager sending the message.

- `attachment` — The attachment to retrieve a cached view provider for.

## Return Value

A previously cached view provider, or `nil`.

## See Also

### Reusing text attachment view providers

- [- textLayoutManager:cacheTextAttachmentViewProvider:forTextAttachment:](<textlayoutmanager(__cachetextattachmentviewprovider_for_).md>) — Notifies the delegate that a view provider associated with a text attachment is about to be invalidated. _(beta)_
