---
title: brightnessDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/brightnessdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/brightnessdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/brightnessdidchangenotification.json'
content_hash: 'sha256:ea93e3a873aa6586'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# brightnessDidChangeNotification

<sub>Type Property</sub>

A notification that posts when a screen’s brightness changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated class let brightnessDidChangeNotification: NSNotification.Name
```

## Discussion

The object of the notification is the [UIScreen](../uiscreen.md) object whose [brightness](brightness.md) property changed. There is no `userInfo` dictionary.

## See Also

### Notifications

- [UIScreenModeDidChangeNotification](modedidchangenotification.md) — A notification that posts when a screen’s mode changes.
- [UIScreenCapturedDidChangeNotification](captureddidchangenotification.md) — A notification that posts when the capture status of a screen changes.
- [UIScreenReferenceDisplayModeStatusDidChangeNotification](referencedisplaymodestatusdidchangenotification.md) — A notification that posts when there’s a change to a screen’s reference display mode status.
