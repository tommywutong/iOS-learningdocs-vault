---
title: attributedTitle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensionitem/attributedtitle
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionitem/attributedtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionitem/attributedtitle.json'
content_hash: 'sha256:47245cbfa257e59a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionItem](../nsextensionitem.md)

# attributedTitle

<sub>Instance Property</sub>

An optional title for the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var attributedTitle: NSAttributedString? { get set }
```

## Discussion

> [!important] Important
> Alternatively, you can set attributed content in the [userInfo](userinfo.md) dictionary using the [NSExtensionItemAttributedTitleKey](../nsextensionitemattributedtitlekey.md) key. However, setting the [userInfo](userinfo.md) dictionary after setting [attributedTitle](attributedtitle.md) overrides this property.

## See Also

### Related Documentation

- [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)

### Identifying the Item

- [userInfo](userinfo.md) — An optional dictionary of keys and values corresponding to the extension item’s properties.
