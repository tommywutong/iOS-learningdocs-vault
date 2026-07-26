---
title: WKHostingController
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkhostingcontroller
source_url: 'https://developer.apple.com/documentation/swiftui/wkhostingcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkhostingcontroller.json'
content_hash: 'sha256:b4ae982377c1a4c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WKHostingController

<sub>Class</sub>

A WatchKit interface controller that hosts a SwiftUI view hierarchy.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency class WKHostingController<Body> where Body : View
```

## Overview

A [WKHostingController](wkhostingcontroller.md) presents and manages your app’s main interface using SwiftUI views. You must subclass [WKHostingController](wkhostingcontroller.md) and override the [body](wkhostingcontroller/body.md) property to provide the set of SwiftUI views you want to display. Display the content of your hosting controller as you would any other [WKInterfaceController](../watchkit/wkinterfacecontroller.md) object. For example, you can include it as one of your app’s root interface controllers, or present it modally.

## Relationships

- **Inherits From**: [WKInterfaceController](../watchkit/wkinterfacecontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a hosting controller object

- [init()](<wkhostingcontroller/init().md>) — Creates a hosting controller object that you can use to implement your app’s main interface using SwiftUI views

### Getting the root view

- [body](wkhostingcontroller/body.md) — The root view of the view hierarchy to display for your interface controller.

### Updating the root view

- [updateBodyIfNeeded()](<wkhostingcontroller/updatebodyifneeded().md>) — Updates the interface controller’s set of views immediately, if updates are pending.
- [setNeedsBodyUpdate()](<wkhostingcontroller/setneedsbodyupdate().md>) — Invalidates the current SwiftUI views and triggers an update during the next cycle.

## See Also

### Displaying SwiftUI views in WatchKit

- [WKUserNotificationHostingController](wkusernotificationhostingcontroller.md) — A WatchKit user notification interface controller that hosts a SwiftUI view hierarchy.
