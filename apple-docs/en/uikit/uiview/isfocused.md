---
title: isFocused
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/isfocused
source_url: 'https://developer.apple.com/documentation/uikit/uiview/isfocused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/isfocused.json'
content_hash: 'sha256:cf8f9c9c8a0c57cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# isFocused

<sub>Instance Property</sub>

A Boolean value that indicates whether the item is currently focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isFocused: Bool { get }
```

## Discussion

This is a convenience property that checks whether the item is equal to the value in the [UIScreen](../uiscreen.md) class’s [focusedView](../uiscreen/focusedview.md) property.

## See Also

### Working with focus

- [canBecomeFocused](canbecomefocused.md) — A Boolean value that indicates whether the view is currently capable of being focused.
- [inheritedAnimationDuration](inheritedanimationduration.md) — Returns the inherited duration of the current animation.
- [focusGroupIdentifier](focusgroupidentifier.md) — The identifier of the focus group that this view belongs to.
- [focusEffect](focuseffect.md) — The visual effect to apply when the view becomes focused.
- [focusGroupPriority](focusgrouppriority.md) — The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
