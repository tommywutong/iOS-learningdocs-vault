---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/delegate.json'
content_hash: 'sha256:6bdd976e1d4d5d21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UIPageViewControllerDelegate)? { get set }
```

## Discussion

Methods of the delegate are called in response to gesture-based navigation and orientation changes.

## See Also

### Customizing the Page View Behavior

- [UIPageViewControllerDelegate](../uipageviewcontrollerdelegate.md) — The delegate of a page view controller must adopt the [UIPageViewControllerDelegate](../uipageviewcontrollerdelegate.md) protocol. These methods allow the delegate to receive a notification when the device orientation changes and when the user navigates to a new page. For page-curl style transitions, the delegate can provide a different spine location in response to a change in the interface orientation.
