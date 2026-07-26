---
title: 'didPresentSearchController(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontrollerdelegate/didpresentsearchcontroller(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/didpresentsearchcontroller(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate/didpresentsearchcontroller%28_%3A%29.json'
content_hash: 'sha256:c8f38e3931cd2de2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchControllerDelegate](../uisearchcontrollerdelegate.md)

# didPresentSearchController(_:)

<sub>Instance Method</sub>

Notifies the delegate when the system completes automatic presentation of the search controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func didPresentSearchController(_ searchController: UISearchController)
```

## Parameters

- `searchController` — The [UISearchController](../uisearchcontroller.md) object to present.

## Discussion

The system only calls this method when it automatically presents the search controller. The system doesn’t call this method if you explicitly present the search controller.

## See Also

### Presenting and dismissing the search controller

- [- didDismissSearchController:](<diddismisssearchcontroller(__).md>) — Notifies the delegate when the system completes automatic dismissal of the search controller.
- [- presentSearchController:](<presentsearchcontroller(__).md>) — Presents the designated search controller.
- [- willDismissSearchController:](<willdismisssearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically dismiss the search controller.
- [- willPresentSearchController:](<willpresentsearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically display the search controller.
