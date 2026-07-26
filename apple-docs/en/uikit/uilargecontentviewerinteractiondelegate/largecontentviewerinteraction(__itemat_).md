---
title: 'largeContentViewerInteraction(_:itemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:itemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:itemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction%28_%3Aitemat%3A%29.json'
content_hash: 'sha256:0805649ead36dba1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerInteractionDelegate](../uilargecontentviewerinteractiondelegate.md)

# largeContentViewerInteraction(_:itemAt:)

<sub>Instance Method</sub>

Identifies the large content viewer item for the specified interaction and location.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func largeContentViewerInteraction(_ interaction: UILargeContentViewerInteraction, itemAt point: CGPoint) -> (any UILargeContentViewerItem)?
```

## Parameters

- `interaction` — The large content viewer interaction that needs an item.

- `point` — The point where the user’s interaction is taking place, in the coordinate space of the view that contains the interaction.

## Discussion

By default, UIKit finds the item for the interaction by calling [- pointInside:withEvent:](<../uiview/point(inside_with_).md>) recursively on your view hierarchy. If you’re not using views, implement this method to identify the item for an interaction at a given point.

## See Also

### Customizing large content viewer interactions

- [- largeContentViewerInteraction:didEndOnItem:atPoint:](<largecontentviewerinteraction(__didendon_at_).md>) — Performs an action when the large content viewer gesture ends at the location of the specified item.
- [- viewControllerForLargeContentViewerInteraction:](<viewcontroller(for_).md>) — Specifies which view controller should display the large content viewer.
