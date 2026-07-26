---
title: modeDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/modedidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/modedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/modedidchangenotification.json'
content_hash: 'sha256:4f0f72da41f66340'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# modeDidChangeNotification

<sub>Type Property</sub>

A notification that posts when a screen’s mode changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated class let modeDidChangeNotification: NSNotification.Name
```

## Discussion

Clients can use this notification to detect changes in the screen resolution.

The object of the notification is the [UIScreen](../uiscreen.md) object whose [currentMode](currentmode.md) property changed. There is no `userInfo` dictionary.

The system posts this notification on the main actor.

## See Also

### Notifications

- [UIScreenBrightnessDidChangeNotification](brightnessdidchangenotification.md) — A notification that posts when a screen’s brightness changes.
- [UIScreenCapturedDidChangeNotification](captureddidchangenotification.md) — A notification that posts when the capture status of a screen changes.
- [UIScreenReferenceDisplayModeStatusDidChangeNotification](referencedisplaymodestatusdidchangenotification.md) — A notification that posts when there’s a change to a screen’s reference display mode status.
