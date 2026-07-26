---
title: canBecomeFocused
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/canbecomefocused
source_url: 'https://developer.apple.com/documentation/uikit/uiview/canbecomefocused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/canbecomefocused.json'
content_hash: 'sha256:d219bf535f0cc457'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# canBecomeFocused

<sub>Instance Property</sub>

A Boolean value that indicates whether the view is currently capable of being focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canBecomeFocused: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if the view can become focused; [false](../../swift/false.md) otherwise.

By default, the value of this property is [false](../../swift/false.md). This property informs the focus engine if a view is capable of being focused. Sometimes even if a view returns [true](../../swift/true.md), a view may not be focusable for the following reasons:

- The view is hidden.
- The view has alpha set to 0.
- The view has `userInteractionEnabled` set to [false](../../swift/false.md).
- The view is not currently in the view hierarchy.

## See Also

### Working with focus

- [inheritedAnimationDuration](inheritedanimationduration.md) — Returns the inherited duration of the current animation.
- [focused](isfocused.md) — A Boolean value that indicates whether the item is currently focused.
- [focusGroupIdentifier](focusgroupidentifier.md) — The identifier of the focus group that this view belongs to.
- [focusEffect](focuseffect.md) — The visual effect to apply when the view becomes focused.
- [focusGroupPriority](focusgrouppriority.md) — The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
