---
title: UIViewControllerRestoration
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollerrestoration
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerrestoration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerrestoration.json'
content_hash: 'sha256:5363dccaaee6518b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIViewControllerRestoration

<sub>Protocol</sub>

The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIViewControllerRestoration
```

## Overview

To use a class that adopts this protocol, you must assign that class to the [restorationClass](uiviewcontroller/restorationclass.md) property of one of your app’s view controllers. The method in this protocol should be used to create the view controller, if it doesn’t yet exist, or return an existing view controller object, if one does exist.

## Topics

### Creating the view controller

- [+ viewControllerWithRestorationIdentifierPath:coder:](<uiviewcontrollerrestoration/viewcontroller(withrestorationidentifierpath_coder_).md>) — Requests the view controller that corresponds to the specified identifier information.

## See Also

### Interface restoration

- [Restoring your app’s state](restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [Restoring your app’s state with SwiftUI](../swiftui/restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md) — Return your app to its previous state after the system terminates it.
- [UIObjectRestoration](uiobjectrestoration.md) — The interface that restoration classes use to restore preserved objects.
- [UIStateRestoring](uistaterestoring.md) — Methods for adding objects to your state restoration archives.
