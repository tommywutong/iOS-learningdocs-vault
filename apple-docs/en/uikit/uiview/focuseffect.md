---
title: focusEffect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/focuseffect
source_url: 'https://developer.apple.com/documentation/uikit/uiview/focuseffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/focuseffect.json'
content_hash: 'sha256:44ddb559976655ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# focusEffect

<sub>Instance Property</sub>

The visual effect to apply when the view becomes focused.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying var focusEffect: UIFocusEffect? { get set }
```

## Discussion

If this property is `nil`, the system doesn’t apply an effect when the view becomes focused.

## See Also

### Working with focus

- [canBecomeFocused](canbecomefocused.md) — A Boolean value that indicates whether the view is currently capable of being focused.
- [inheritedAnimationDuration](inheritedanimationduration.md) — Returns the inherited duration of the current animation.
- [focused](isfocused.md) — A Boolean value that indicates whether the item is currently focused.
- [focusGroupIdentifier](focusgroupidentifier.md) — The identifier of the focus group that this view belongs to.
- [focusGroupPriority](focusgrouppriority.md) — The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
