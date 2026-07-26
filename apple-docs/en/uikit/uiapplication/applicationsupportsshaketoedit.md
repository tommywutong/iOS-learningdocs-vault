---
title: applicationSupportsShakeToEdit
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/applicationsupportsshaketoedit
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/applicationsupportsshaketoedit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/applicationsupportsshaketoedit.json'
content_hash: 'sha256:ad229874244573c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# applicationSupportsShakeToEdit

<sub>Instance Property</sub>

A Boolean value that determines whether shaking the device displays the undo-redo user interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var applicationSupportsShakeToEdit: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). Set the property to [false](../../swift/false.md) if you don’t want your app to display the Undo and Redo buttons when users shake the device.

## See Also

### Controlling and handling events

- [- sendEvent:](<sendevent(__).md>) — Dispatches an event to the appropriate responder objects in the app.
- [- sendAction:to:from:forEvent:](<sendaction(__to_from_for_).md>) — Sends an action message identified by the selector to a specified target.
