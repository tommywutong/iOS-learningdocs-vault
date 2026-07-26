---
title: 'init(items:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicitemgroup/init(items:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitemgroup/init(items:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitemgroup/init%28items%3A%29.json'
content_hash: 'sha256:288488ad0b06be98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemGroup](../uidynamicitemgroup.md)

# init(items:)

<sub>Initializer</sub>

Initializes and returns a group containing the specified items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(items: [any UIDynamicItem])
```

## Parameters

- `items` — The dynamic items to include in the group. You cannot change the items in a group after initialization.

## Return Value

A new group object containing the items.
