---
title: UISearchControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate.json'
content_hash: 'sha256:d11d887a760d90d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchControllerDelegate

<sub>Protocol</sub>

A set of delegate methods for search controller objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UISearchControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Presenting and dismissing the search controller

- [- didDismissSearchController:](<uisearchcontrollerdelegate/diddismisssearchcontroller(__).md>) — Notifies the delegate when the system completes automatic dismissal of the search controller.
- [- didPresentSearchController:](<uisearchcontrollerdelegate/didpresentsearchcontroller(__).md>) — Notifies the delegate when the system completes automatic presentation of the search controller.
- [- presentSearchController:](<uisearchcontrollerdelegate/presentsearchcontroller(__).md>) — Presents the designated search controller.
- [- willDismissSearchController:](<uisearchcontrollerdelegate/willdismisssearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically dismiss the search controller.
- [- willPresentSearchController:](<uisearchcontrollerdelegate/willpresentsearchcontroller(__).md>) — Notifies the delegate that the system is about to automatically display the search controller.

### Responding to search bar placement updates

- [- searchController:didChangeFromSearchBarPlacement:](<uisearchcontrollerdelegate/searchcontroller(__didchangefrom_).md>) — Notifies the delegate after the search bar placement changes.
- [- searchController:willChangeToSearchBarPlacement:](<uisearchcontrollerdelegate/searchcontroller(__willchangeto_).md>) — Notifies the delegate before the search bar placement changes.

## See Also

### Responding to presentation and dismissal

- [delegate](uisearchcontroller/delegate.md) — The search controller’s delegate.
