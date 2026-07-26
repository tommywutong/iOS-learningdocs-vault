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
doc_path: /documentation/uikit/uiview/focusgrouppriority
source_url: 'https://developer.apple.com/documentation/uikit/uiview/focusgrouppriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/focusgrouppriority.json'
content_hash: 'sha256:7ee815c5b87d512f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# focusGroupPriority

<sub>Instance Property</sub>

The importance of the item within a focus group, used by the focus system to determine the group’s primary item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var focusGroupPriority: UIFocusGroupPriority { get set }
```

## Discussion

The system automatically assigns each focusable item in a focus group one of the predefined system priorities. The visible item with the highest priority is the group’s primary item.

You can override the default priority of an item to customize the primary item of a group. When setting a custom priority, you can only increase the item’s priority above its system-provided value, not decrease it. The system-provided priority is always the minimum priority applied for the item. The system ignores any priority lower than `0`.

## See Also

### Working with focus

- [canBecomeFocused](canbecomefocused.md) — A Boolean value that indicates whether the view is currently capable of being focused.
- [inheritedAnimationDuration](inheritedanimationduration.md) — Returns the inherited duration of the current animation.
- [focused](isfocused.md) — A Boolean value that indicates whether the item is currently focused.
- [focusGroupIdentifier](focusgroupidentifier.md) — The identifier of the focus group that this view belongs to.
- [focusEffect](focuseffect.md) — The visual effect to apply when the view becomes focused.
