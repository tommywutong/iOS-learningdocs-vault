---
title: UIPageViewControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdelegate.json'
content_hash: 'sha256:998001ea69d806df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPageViewControllerDelegate

<sub>Protocol</sub>

The delegate of a page view controller must adopt the [UIPageViewControllerDelegate](uipageviewcontrollerdelegate.md) protocol. These methods allow the delegate to receive a notification when the device orientation changes and when the user navigates to a new page. For page-curl style transitions, the delegate can provide a different spine location in response to a change in the interface orientation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIPageViewControllerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to Page View Controller Events

- [- pageViewController:willTransitionToViewControllers:](<uipageviewcontrollerdelegate/pageviewcontroller(__willtransitionto_).md>) — Called before a gesture-driven transition begins.
- [- pageViewController:didFinishAnimating:previousViewControllers:transitionCompleted:](<uipageviewcontrollerdelegate/pageviewcontroller(__didfinishanimating_previousviewcontrollers_transitioncompleted_).md>) — Called after a gesture-driven transition completes.
- [- pageViewController:spineLocationForInterfaceOrientation:](<uipageviewcontrollerdelegate/pageviewcontroller(__spinelocationfor_).md>) — Returns the spine location for the given orientation.

### Overriding View Rotation Settings

- [- pageViewControllerSupportedInterfaceOrientations:](<uipageviewcontrollerdelegate/pageviewcontrollersupportedinterfaceorientations(__).md>) — Returns the complete set of supported interface orientations for the page view controller, as determined by the delegate.
- [- pageViewControllerPreferredInterfaceOrientationForPresentation:](<uipageviewcontrollerdelegate/pageviewcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Returns the preferred orientation for presentation of the page view controller, as determined by the delegate.

## See Also

### Customizing the Page View Behavior

- [delegate](uipageviewcontroller/delegate.md) — The delegate object.
