---
title: GCMouseDidConnectNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gcmousedidconnectnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gcmousedidconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gcmousedidconnectnotification.json'
content_hash: 'sha256:39913a11ee776df1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCMouseDidConnectNotification

<sub>Global Variable</sub>

A notification that posts after a mouse connects to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCMouseDidConnectNotification;
```

## Discussion

The notification object is a [GCMouse](gcmouse.md) object that represents the mouse.

The system posts this notification on the main thread.

## See Also

### Discovering mouse devices

- [+ mice](<gcmouse/mice().md>) — Returns any mice that the user connects to the device.
- [GCMouseDidDisconnectNotification](gcmousediddisconnectnotification.md) — A notification that posts after a mouse disconnects from the device.
