---
title: 'badgeWithCount:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitembadge/badgewithcount:'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitembadge/badgewithcount:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitembadge/badgewithcount%3A.json'
content_hash: 'sha256:63a6f2cf0a2bf51b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItemBadge](../uibarbuttonitembadge.md)

# badgeWithCount:

<sub>Type Method</sub>

Creates a badge with the specified `count`.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) badgeWithCount:(NSUInteger) count;
```

## Discussion

The count is localized when shown, and will update when the app’s locale changes.
