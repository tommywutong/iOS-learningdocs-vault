---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/delegate.json'
content_hash: 'sha256:b60bf23e20d8477f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate of the navigation controller object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UINavigationControllerDelegate)? { get set }
```

## Discussion

You can use the navigation delegate to perform additional actions in response to changes in the navigation interface. For more information about implementing the delegate, see [UINavigationControllerDelegate](../uinavigationcontrollerdelegate.md).

## See Also

### Customizing the navigation interface behavior

- [UINavigationControllerDelegate](../uinavigationcontrollerdelegate.md) — The interface for an object that serves as a navigation controller’s delegate.
