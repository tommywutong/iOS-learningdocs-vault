---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/delegate.json'
content_hash: 'sha256:8390aceeb2f8fc2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# delegate

<sub>Instance Property</sub>

The search controller’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UISearchControllerDelegate)? { get set }
```

## Discussion

Use the delegate object to receive notifications when the search results controller is presented and dismissed. You might use these notifications to customize the search interface or perform related actions.

## See Also

### Responding to presentation and dismissal

- [UISearchControllerDelegate](../uisearchcontrollerdelegate.md) — A set of delegate methods for search controller objects.
