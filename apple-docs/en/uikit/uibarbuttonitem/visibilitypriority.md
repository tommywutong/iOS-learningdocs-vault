---
title: visibilityPriority
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/visibilitypriority
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/visibilitypriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/visibilitypriority.json'
content_hash: 'sha256:b864084e88a65a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# visibilityPriority

<sub>Instance Property</sub>

Visibility priority for this item when placed in a button bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var visibilityPriority: UIBarButtonItemVisibilityPriority { get set }
```

## Discussion

Items with higher priority values are preserved longer when space is constrained. When an item is placed in an implicit group, the group inherits this priority.

The default value is `UIBarButtonItemVisibilityPriorityStandard`.
