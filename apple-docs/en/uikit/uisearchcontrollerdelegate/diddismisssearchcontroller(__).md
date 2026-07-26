---
title: 'didDismissSearchController(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontrollerdelegate/diddismisssearchcontroller(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/diddismisssearchcontroller(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate/diddismisssearchcontroller%28_%3A%29.json'
content_hash: 'sha256:d683eee4bb3952f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchControllerDelegate](../uisearchcontrollerdelegate.md)

# didDismissSearchController(_:)

<sub>Instance Method</sub>

Notifies the delegate when the system completes automatic dismissal of the search controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func didDismissSearchController(_ searchController: UISearchController)
```

## Parameters

- `searchController` — The [UISearchController](../uisearchcontroller.md) object to dismiss.

## Discussion

The system only calls this method when it automatically dismisses the search controller. The system doesn’t call this method if you explicitly dismiss the search controller.

## See Also

### Presenting and dismissing the search controller

- [- didPresentSearchController:](<didpresentsearchcontroller(__).md>) — Notifies the delegate when the system completes automatic presentation of the search controller.
- [- presentSearchController:](<presentsearchcontroller(__).md>) — Presents the designated search controller.
- [- willDismissSearchController:](<willdismisssearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically dismiss the search controller.
- [- willPresentSearchController:](<willpresentsearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically display the search controller.
