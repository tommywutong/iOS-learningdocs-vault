---
title: UIObjectRestoration
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiobjectrestoration
source_url: 'https://developer.apple.com/documentation/uikit/uiobjectrestoration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiobjectrestoration.json'
content_hash: 'sha256:d9dc9b7e148ffd69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIObjectRestoration

<sub>Protocol</sub>

The interface that restoration classes use to restore preserved objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIObjectRestoration
```

## Overview

A restorable object must set its [objectRestorationClass](uistaterestoring/objectrestorationclass.md) property to the class that adopts this protocol. The method in this protocol should be used to return the object if it already exists or create it if needed.

## Topics

### Creating the restorable object

- [+ objectWithRestorationIdentifierPath:coder:](<uiobjectrestoration/object(withrestorationidentifierpath_coder_).md>) — Requests the object that corresponds to the specified identifier information.

## See Also

### Interface restoration

- [Restoring your app’s state](restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [Restoring your app’s state with SwiftUI](../swiftui/restoring-your-app-s-state-with-swiftui.md) — Provide app continuity for users by preserving their current activities.
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md) — Return your app to its previous state after the system terminates it.
- [UIViewControllerRestoration](uiviewcontrollerrestoration.md) — The methods that objects adopt so that they can act as a restoration class for view controllers during state restoration.
- [UIStateRestoring](uistaterestoring.md) — Methods for adding objects to your state restoration archives.
