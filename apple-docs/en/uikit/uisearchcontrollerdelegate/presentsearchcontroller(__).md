---
title: 'presentSearchController(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontrollerdelegate/presentsearchcontroller(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/presentsearchcontroller(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate/presentsearchcontroller%28_%3A%29.json'
content_hash: 'sha256:714fc912a1ab84d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchControllerDelegate](../uisearchcontrollerdelegate.md)

# presentSearchController(_:)

<sub>Instance Method</sub>

Presents the designated search controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentSearchController(_ searchController: UISearchController)
```

## Parameters

- `searchController` — The [UISearchController](../uisearchcontroller.md) object to present.

## Discussion

The system calls this method when the user begins editing in the search controller, or you set the [active](../uisearchcontroller/isactive.md) property to [true](../../swift/true.md). The system performs a default presentation if you don’t implement this method or you present the controller yourself.

## See Also

### Presenting and dismissing the search controller

- [- didDismissSearchController:](<diddismisssearchcontroller(__).md>) — Notifies the delegate when the system completes automatic dismissal of the search controller.
- [- didPresentSearchController:](<didpresentsearchcontroller(__).md>) — Notifies the delegate when the system completes automatic presentation of the search controller.
- [- willDismissSearchController:](<willdismisssearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically dismiss the search controller.
- [- willPresentSearchController:](<willpresentsearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically display the search controller.
