---
title: userInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensionitem/userinfo
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionitem/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionitem/userinfo.json'
content_hash: 'sha256:e3a3239ae2e87117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionItem](../nsextensionitem.md)

# userInfo

<sub>Instance Property</sub>

An optional dictionary of keys and values corresponding to the extension item’s properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

## Discussion

If applicable to a particular extension type, additional information may be available in the `userInfo` dictionary. For example, in the context of an Action extension, the `userInfo` dictionary may contain values for the keys [NSExtensionItemAttachmentsKey](../nsextensionitemattachmentskey.md), [NSExtensionItemAttributedContentTextKey](../nsextensionitemattributedcontenttextkey.md), and [NSExtensionItemAttributedTitleKey](../nsextensionitemattributedtitlekey.md).

> [!important] Important
> Setting the [userInfo](userinfo.md) dictionary after setting [attachments](attachments.md), [attributedContentText](attributedcontenttext.md), or [attributedTitle](attributedtitle.md) overrides those properties.

## See Also

### Identifying the Item

- [attributedTitle](attributedtitle.md) — An optional title for the item.
