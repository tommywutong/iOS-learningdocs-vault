---
title: capturedDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/captureddidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/captureddidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/captureddidchangenotification.json'
content_hash: 'sha256:cb5a4e75a9b0298f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# capturedDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the capture status of a screen changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated class let capturedDidChangeNotification: NSNotification.Name
```

## Discussion

The contents of a screen can be recorded, mirrored, sent over AirPlay, or otherwise cloned to another destination. UIKit sends this notification when the capture status of the screen changes.

The object of the notification is the [UIScreen](../uiscreen.md) object whose [captured](iscaptured.md) property changed. There is no `userInfo` dictionary.

The system posts this notification on the main actor.

## See Also

### Notifications

- [UIScreenBrightnessDidChangeNotification](brightnessdidchangenotification.md) — A notification that posts when a screen’s brightness changes.
- [UIScreenModeDidChangeNotification](modedidchangenotification.md) — A notification that posts when a screen’s mode changes.
- [UIScreenReferenceDisplayModeStatusDidChangeNotification](referencedisplaymodestatusdidchangenotification.md) — A notification that posts when there’s a change to a screen’s reference display mode status.
