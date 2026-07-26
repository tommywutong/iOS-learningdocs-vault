---
title: focusGroupPriority
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitem/focusgrouppriority
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem/focusgrouppriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem/focusgrouppriority.json'
content_hash: 'sha256:f2017d87dbff335b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItem](../uifocusitem.md)

# focusGroupPriority

<sub>Instance Property</sub>

The importance of the item within a focus group, used by the focus system to determine the group’s primary item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional var focusGroupPriority: UIFocusGroupPriority { get }
```

## Discussion

The system automatically assigns each focusable item in a focus group one of the predefined system priorities. The system assigns the [UIFocusGroupPriorityCurrentlyFocused](../uifocusgrouppriority/currentlyfocused.md) priority to the focused item, [UIFocusGroupPriorityPreviouslyFocused](../uifocusgrouppriority/previouslyfocused.md) to the group’s previous focused item, and [UIFocusGroupPriorityIgnored](../uifocusgrouppriority/ignored.md) for all other items. The visible item with the highest priority is the group’s primary item.

You can override the default priority of an item to customize the primary item of a group. When setting a custom priority, you can only increase the item’s priority above its system-provided value, not decrease it. The system-provided priority is always the minimum priority applied for the item. The system ignores any priority lower than `0`.

## See Also

### Determining the focus priority

- [UIFocusGroupPriority](../uifocusgrouppriority.md) — The importance of an item within a focus group, used by the focus system to determine the group’s primary item.
