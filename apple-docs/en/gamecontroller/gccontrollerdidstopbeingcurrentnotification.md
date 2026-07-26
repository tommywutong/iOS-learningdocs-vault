---
title: GCControllerDidStopBeingCurrentNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gccontrollerdidstopbeingcurrentnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gccontrollerdidstopbeingcurrentnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gccontrollerdidstopbeingcurrentnotification.json'
content_hash: 'sha256:05f236ae6ea03ddb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCControllerDidStopBeingCurrentNotification

<sub>Global Variable</sub>

A notification that posts when a controller stops being the current controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCControllerDidStopBeingCurrentNotification;
```

## Discussion

The notification object is the [GCController](gccontroller.md) object that’s no longer current.

The system posts this notification on the main thread.

## See Also

### Handling multiple controllers

- [current](gccontroller/current.md) — The most recently used game controller.
- [GCControllerDidBecomeCurrentNotification](gccontrollerdidbecomecurrentnotification.md) — A notification that posts when a controller becomes the current controller.
