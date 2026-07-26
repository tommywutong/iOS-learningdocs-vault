---
title: inheritedAnimationDuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/inheritedanimationduration
source_url: 'https://developer.apple.com/documentation/uikit/uiview/inheritedanimationduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/inheritedanimationduration.json'
content_hash: 'sha256:974a01c11d3c1595'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# inheritedAnimationDuration

<sub>Type Property</sub>

Returns the inherited duration of the current animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var inheritedAnimationDuration: TimeInterval { get }
```

## Return Value

The duration of the current animation.

## Discussion

This method only returns a non-zero value if called within a [UIView](../uiview.md) animation block.

## See Also

### Working with focus

- [canBecomeFocused](canbecomefocused.md) — A Boolean value that indicates whether the view is currently capable of being focused.
- [focused](isfocused.md) — A Boolean value that indicates whether the item is currently focused.
- [focusGroupIdentifier](focusgroupidentifier.md) — The identifier of the focus group that this view belongs to.
- [focusEffect](focuseffect.md) — The visual effect to apply when the view becomes focused.
- [focusGroupPriority](focusgrouppriority.md) — The importance of the item within a focus group, used by the focus system to determine the group’s primary item.
