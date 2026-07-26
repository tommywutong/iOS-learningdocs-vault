---
title: 'willPresentSearchController(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontrollerdelegate/willpresentsearchcontroller(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/willpresentsearchcontroller(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate/willpresentsearchcontroller%28_%3A%29.json'
content_hash: 'sha256:a81bae87ba5734f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchControllerDelegate](../uisearchcontrollerdelegate.md)

# willPresentSearchController(_:)

<sub>Instance Method</sub>

Notifies the delegate that the system is about to automatically display the search controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func willPresentSearchController(_ searchController: UISearchController)
```

## Parameters

- `searchController` — The [UISearchController](../uisearchcontroller.md) object to present.

## Discussion

The system only calls this method when it’s about to automatically present the search controller. The system doesn’t call this method when you explicitly present the search controller.

## See Also

### Presenting and dismissing the search controller

- [- didDismissSearchController:](<diddismisssearchcontroller(__).md>) — Notifies the delegate when the system completes automatic dismissal of the search controller.
- [- didPresentSearchController:](<didpresentsearchcontroller(__).md>) — Notifies the delegate when the system completes automatic presentation of the search controller.
- [- presentSearchController:](<presentsearchcontroller(__).md>) — Presents the designated search controller.
- [- willDismissSearchController:](<willdismisssearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically dismiss the search controller.
