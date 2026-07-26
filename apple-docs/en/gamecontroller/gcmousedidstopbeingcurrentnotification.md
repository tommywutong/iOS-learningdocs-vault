---
title: GCMouseDidStopBeingCurrentNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gcmousedidstopbeingcurrentnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gcmousedidstopbeingcurrentnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gcmousedidstopbeingcurrentnotification.json'
content_hash: 'sha256:e095942b1dbfcc30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCMouseDidStopBeingCurrentNotification

<sub>Global Variable</sub>

A notification that posts when a mouse stops being the most recent mouse that the user connects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCMouseDidStopBeingCurrentNotification;
```

## Discussion

The notification object is a [GCMouse](gcmouse.md) object that represents the previous current mouse. For example, if you set any of the mouse input change handlers, unset them when you receive this notification.

The system posts this notification on the main thread.

## See Also

### Handling multiple mouse devices

- [current](gcmouse/current.md) — The most recent mouse that the user connects.
- [GCMouseDidBecomeCurrentNotification](gcmousedidbecomecurrentnotification.md) — A notification that posts when a mouse becomes the most recent mouse that the user connects.
