---
title: referenceDisplayModeStatusDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/referencedisplaymodestatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/referencedisplaymodestatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/referencedisplaymodestatusdidchangenotification.json'
content_hash: 'sha256:68561bb369695280'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# referenceDisplayModeStatusDidChangeNotification

<sub>Type Property</sub>

A notification that posts when there’s a change to a screen’s reference display mode status.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated class let referenceDisplayModeStatusDidChangeNotification: NSNotification.Name
```

## Discussion

The notification’s [object](../../foundation/notification/object.md) is the changed screen. Use that object’s [referenceDisplayModeStatus](referencedisplaymodestatus-swift.property.md) property to retrieve the new status.

The system posts this notification on the main actor.

## See Also

### Notifications

- [UIScreenBrightnessDidChangeNotification](brightnessdidchangenotification.md) — A notification that posts when a screen’s brightness changes.
- [UIScreenModeDidChangeNotification](modedidchangenotification.md) — A notification that posts when a screen’s mode changes.
- [UIScreenCapturedDidChangeNotification](captureddidchangenotification.md) — A notification that posts when the capture status of a screen changes.
