---
title: 'willDismissSearchController(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontrollerdelegate/willdismisssearchcontroller(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/willdismisssearchcontroller(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate/willdismisssearchcontroller%28_%3A%29.json'
content_hash: 'sha256:ab9a3211b9076766'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchControllerDelegate](../uisearchcontrollerdelegate.md)

# willDismissSearchController(_:)

<sub>Instance Method</sub>

Notifies the delegate that the system is about to automatically dismiss the search controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func willDismissSearchController(_ searchController: UISearchController)
```

## Parameters

- `searchController` — The [UISearchController](../uisearchcontroller.md) object to dismiss.

## Discussion

The system only calls this method when it’s about to automatically dismiss the search controller. The system doesn’t call this method if you explicitly dismiss the search controller.

## See Also

### Presenting and dismissing the search controller

- [- didDismissSearchController:](<diddismisssearchcontroller(__).md>) — Notifies the delegate when the system completes automatic dismissal of the search controller.
- [- didPresentSearchController:](<didpresentsearchcontroller(__).md>) — Notifies the delegate when the system completes automatic presentation of the search controller.
- [- presentSearchController:](<presentsearchcontroller(__).md>) — Presents the designated search controller.
- [- willPresentSearchController:](<willpresentsearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically display the search controller.
