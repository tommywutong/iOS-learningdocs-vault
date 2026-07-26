---
title: GCMouseDidBecomeCurrentNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gcmousedidbecomecurrentnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gcmousedidbecomecurrentnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gcmousedidbecomecurrentnotification.json'
content_hash: 'sha256:c22c9884e5c2f77a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCMouseDidBecomeCurrentNotification

<sub>Global Variable</sub>

A notification that posts when a mouse becomes the most recent mouse that the user connects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCMouseDidBecomeCurrentNotification;
```

## Discussion

The notification object is a [GCMouse](gcmouse.md) object that represents the current mouse. For example, set the mouse input change handlers when you receive this notification.

The system posts this notification on the main thread.

## See Also

### Handling multiple mouse devices

- [current](gcmouse/current.md) — The most recent mouse that the user connects.
- [GCMouseDidStopBeingCurrentNotification](gcmousedidstopbeingcurrentnotification.md) — A notification that posts when a mouse stops being the most recent mouse that the user connects.
