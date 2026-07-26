---
title: UINavigationControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontrollerdelegate.json'
content_hash: 'sha256:464c2a9dfb2c9038'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINavigationControllerDelegate

<sub>Protocol</sub>

The interface for an object that serves as a navigation controller’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UINavigationControllerDelegate : NSObjectProtocol
```

## Overview

Use a navigation controller delegate (a custom object that implements this protocol) to modify behavior when a view controller is pushed or popped from the navigation stack of a [UINavigationController](uinavigationcontroller.md) object.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to a view controller being shown

- [- navigationController:willShowViewController:animated:](<uinavigationcontrollerdelegate/navigationcontroller(__willshow_animated_).md>) — Notifies the delegate before the navigation controller displays a view controller’s view and navigation item properties.
- [- navigationController:didShowViewController:animated:](<uinavigationcontrollerdelegate/navigationcontroller(__didshow_animated_).md>) — Notifies the delegate after the navigation controller displays a view controller’s view and navigation item properties.

### Supporting custom transition animations

- [- navigationController:animationControllerForOperation:fromViewController:toViewController:](<uinavigationcontrollerdelegate/navigationcontroller(__animationcontrollerfor_from_to_).md>) — Allows the delegate to return a noninteractive animator object for use during view controller transitions.
- [- navigationController:interactionControllerForAnimationController:](<uinavigationcontrollerdelegate/navigationcontroller(__interactioncontrollerfor_).md>) — Allows the delegate to return an interactive animator object for use during view controller transitions.
- [- navigationControllerPreferredInterfaceOrientationForPresentation:](<uinavigationcontrollerdelegate/navigationcontrollerpreferredinterfaceorientationforpresentation(__).md>) — Returns the preferred orientation for presentation of the navigation controller, as determined by the delegate.
- [- navigationControllerSupportedInterfaceOrientations:](<uinavigationcontrollerdelegate/navigationcontrollersupportedinterfaceorientations(__).md>) — Returns the complete set of supported interface orientations for the navigation controller, as determined by the delegate.

### Constants

- [Operation](uinavigationcontroller/operation.md) — Constants that define the type of navigation controller transitions that can occur.

## See Also

### Customizing the navigation interface behavior

- [delegate](uinavigationcontroller/delegate.md) — The delegate of the navigation controller object.
