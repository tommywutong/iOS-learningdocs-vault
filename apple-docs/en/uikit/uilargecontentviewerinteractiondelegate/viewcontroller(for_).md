---
title: 'viewController(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilargecontentviewerinteractiondelegate/viewcontroller(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate/viewcontroller(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteractiondelegate/viewcontroller%28for%3A%29.json'
content_hash: 'sha256:3b696deb605616ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerInteractionDelegate](../uilargecontentviewerinteractiondelegate.md)

# viewController(for:)

<sub>Instance Method</sub>

Specifies which view controller should display the large content viewer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func viewController(for interaction: UILargeContentViewerInteraction) -> UIViewController
```

## Parameters

- `interaction` — The large content viewer that the system is displaying.

## Return Value

A view controller that the system uses to present the large content viewer in.

## Discussion

By default, UIKit uses a view controller that contains the view you added the interaction to. If this default choice doesn’t work for your app, implement this method to specify a different view controller.

## See Also

### Customizing large content viewer interactions

- [- largeContentViewerInteraction:didEndOnItem:atPoint:](<largecontentviewerinteraction(__didendon_at_).md>) — Performs an action when the large content viewer gesture ends at the location of the specified item.
- [- largeContentViewerInteraction:itemAtPoint:](<largecontentviewerinteraction(__itemat_).md>) — Identifies the large content viewer item for the specified interaction and location.
