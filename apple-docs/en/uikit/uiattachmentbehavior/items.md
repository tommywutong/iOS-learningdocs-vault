---
title: items
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiattachmentbehavior/items
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/items.json'
content_hash: 'sha256:f9a2662513df6456'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# items

<sub>Instance Property</sub>

The dynamic items connected by the attachment behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var items: [any UIDynamicItem] { get }
```

## Discussion

Contains two elements when used for an attachment behavior of type [UIAttachmentBehaviorTypeItems](attachmenttype/items.md); contains one element when used for an attachment behavior of type [UIAttachmentBehaviorTypeAnchor](attachmenttype/anchor.md).
