---
title: 'textLayoutManager(_:cacheTextAttachmentViewProvider:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:cachetextattachmentviewprovider:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:cachetextattachmentviewprovider:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager%28_%3Acachetextattachmentviewprovider%3Afor%3A%29.json'
content_hash: 'sha256:5fa18d7a63e9ce92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManagerDelegate](../nstextlayoutmanagerdelegate.md)

# textLayoutManager(_:cacheTextAttachmentViewProvider:for:)

<sub>Instance Method</sub>

Notifies the delegate that a view provider associated with a text attachment is about to be invalidated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, cacheTextAttachmentViewProvider viewProvider: NSTextAttachmentViewProvider, for textAttachment: NSTextAttachment)
```

## Parameters

- `textLayoutManager` — The text layout manager sending the message.

- `viewProvider` — The view provider being invalidated.

- `textAttachment` — The attachment associated with the view provider.

## Discussion

The delegate can use this to cache the view provider.

## See Also

### Reusing text attachment view providers

- [- textLayoutManager:retrieveCachedTextAttachmentViewProviderForTextAttachment:](<textlayoutmanager(__retrievecachedtextattachmentviewproviderfor_).md>) — Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment. _(beta)_
