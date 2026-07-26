---
title: 'largeContentViewerInteraction(_:didEndOn:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:didendon:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(_:didendon:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteractiondelegate/largecontentviewerinteraction%28_%3Adidendon%3Aat%3A%29.json'
content_hash: 'sha256:356678233da1a98b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerInteractionDelegate](../uilargecontentviewerinteractiondelegate.md)

# largeContentViewerInteraction(_:didEndOn:at:)

<sub>Instance Method</sub>

Performs an action when the large content viewer gesture ends at the location of the specified item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func largeContentViewerInteraction(_ interaction: UILargeContentViewerInteraction, didEndOn item: (any UILargeContentViewerItem)?, at point: CGPoint)
```

## Parameters

- `interaction` — The large content viewer interaction associated with the view that the user interacted with.

- `item` — The item that the user interacted with in the large content viewer.

- `point` — The point where the user’s interaction ended, in the coordinate space of the item’s view.

## Discussion

If you don’t implement this method and are using standard UIKit controls, the system performs a default action, such as sending a [UIControlEventTouchUpInside](../uicontrol/event/touchupinside.md) event to the control. If you’re using a custom view with its own tap gesture recognizer, implement this method to handle the interaction. For example, to perform the action that would have occurred if the user tapped on that item.

UIKit only calls this method if the gesture ends successfully, not if it fails or gets canceled.

## See Also

### Customizing large content viewer interactions

- [- largeContentViewerInteraction:itemAtPoint:](<largecontentviewerinteraction(__itemat_).md>) — Identifies the large content viewer item for the specified interaction and location.
- [- viewControllerForLargeContentViewerInteraction:](<viewcontroller(for_).md>) — Specifies which view controller should display the large content viewer.
