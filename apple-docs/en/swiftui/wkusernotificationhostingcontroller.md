---
title: WKUserNotificationHostingController
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkusernotificationhostingcontroller
source_url: 'https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkusernotificationhostingcontroller.json'
content_hash: 'sha256:fa97c70245ee4f11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WKUserNotificationHostingController

<sub>Class</sub>

A WatchKit user notification interface controller that hosts a SwiftUI view hierarchy.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency class WKUserNotificationHostingController<Body> where Body : View
```

## Overview

A [WKUserNotificationHostingController](wkusernotificationhostingcontroller.md) presents and manages your app’s notification interface using SwiftUI views. You must subclass [WKUserNotificationHostingController](wkusernotificationhostingcontroller.md) and override the [body](wkusernotificationhostingcontroller/body.md) property to provide the set of SwiftUI views you want to display. In the storyboard of your watch app, specify the name of your custom class for your dynamic interactive interface.

## Relationships

- **Inherits From**: [WKUserNotificationInterfaceController](../watchkit/wkusernotificationinterfacecontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a hosting controller object

- [init()](<wkusernotificationhostingcontroller/init().md>) — Creates a notification hosting controller object that you can use to implement your notification interfaces using SwiftUI views.

### Getting the root view

- [body](wkusernotificationhostingcontroller/body.md) — The root view of the view hierarchy to display for your notification interface.

### Configuring the notification

- [coalescedDescriptionFormat](wkusernotificationhostingcontroller/coalesceddescriptionformat.md) — The format string to display when multiple notifications of the same type arrive simultaneously. If you specify a custom string, you can use the %d variable to reflect the number of notifications. If `nil` format will be the system default.
- [isInteractive](wkusernotificationhostingcontroller/isinteractive.md) — If the notification should accept user input.
- [sashColor](wkusernotificationhostingcontroller/sashcolor.md) — Color to use within the sash of the long look interface. If `nil` the sash will be the default system color.
- [subtitleColor](wkusernotificationhostingcontroller/subtitlecolor.md) — The color to apply to the subtitle text displayed in the short look interface. If `nil` the text will be the default system color.
- [titleColor](wkusernotificationhostingcontroller/titlecolor.md) — The color to apply to the text displayed in the sash. If `nil` the text will be the default system color.
- [wantsSashBlur](wkusernotificationhostingcontroller/wantssashblur.md) — If the sash should include a blur over the background.

## See Also

### Displaying SwiftUI views in WatchKit

- [WKHostingController](wkhostingcontroller.md) — A WatchKit interface controller that hosts a SwiftUI view hierarchy.
