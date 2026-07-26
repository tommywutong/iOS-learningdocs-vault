---
title: attributedContentText
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensionitem/attributedcontenttext
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionitem/attributedcontenttext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionitem/attributedcontenttext.json'
content_hash: 'sha256:8be5bf5a405edfb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionItem](../nsextensionitem.md)

# attributedContentText

<sub>Instance Property</sub>

An optional string describing the extension item content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var attributedContentText: NSAttributedString? { get set }
```

## Discussion

> [!important] Important
> Alternatively, you can set attributed content in the [userInfo](userinfo.md) dictionary using the [NSExtensionItemAttributedContentTextKey](../nsextensionitemattributedcontenttextkey.md) key. However, setting the [userInfo](userinfo.md) dictionary after setting [attributedContentText](attributedcontenttext.md) overrides this property.

## See Also

### Item Contents

- [attachments](attachments.md) — An optional array of media data associated with the extension item.
