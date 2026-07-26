---
title: attachments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensionitem/attachments
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionitem/attachments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionitem/attachments.json'
content_hash: 'sha256:1a568bc69fa7216b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionItem](../nsextensionitem.md)

# attachments

<sub>Instance Property</sub>

An optional array of media data associated with the extension item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attachments: [NSItemProvider]? { get set }
```

## Discussion

Populate this array with images, videos, URLs, and so on. It’s not meant to be an array of alternative data formats or types, but is instead a collection to include in a social media post, for example. These items are always typed [NSItemProvider](../nsitemprovider.md).

> [!important] Important
> Alternatively, you can set attachments in the [userInfo](userinfo.md) dictionary using the [NSExtensionItemAttachmentsKey](../nsextensionitemattachmentskey.md) key. However, setting the [userInfo](userinfo.md) dictionary after setting [attachments](attachments.md) will override this property.

## See Also

### Item Contents

- [attributedContentText](attributedcontenttext.md) — An optional string describing the extension item content.
