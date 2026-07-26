---
title: focusGroupIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/focusgroupidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiview/focusgroupidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/focusgroupidentifier.json'
content_hash: 'sha256:512db675fd41f662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# focusGroupIdentifier

<sub>Instance Property</sub>

The identifier of the focus group that this view belongs to.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var focusGroupIdentifier: String? { get set }
```

## Discussion

If this property is `nil`, subviews inherit their superview’s focus group.

## See Also

### Working with focus

- [canBecomeFocused](canbecomefocused.md) — A Boolean value that indicates whether the view is currently capable of being focused.
- [inheritedAnimationDuration](inheritedanimationduration.md) — Returns the inherited duration of the current animation.
- [focused](isfocused.md) — A Boolean value that indicates whether the item is currently focused.
- [focusEffect](focuseffect.md) — The visual effect to apply when the view becomes focused.
- [focusGroupPriority](focusgrouppriority.md) — The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
