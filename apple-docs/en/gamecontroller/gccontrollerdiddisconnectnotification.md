---
title: GCControllerDidDisconnectNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gccontrollerdiddisconnectnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gccontrollerdiddisconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gccontrollerdiddisconnectnotification.json'
content_hash: 'sha256:50bda34eba4ccd63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCControllerDidDisconnectNotification

<sub>Global Variable</sub>

A notification that posts after a controller disconnects from the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCControllerDidDisconnectNotification;
```

## Discussion

The notification object is the [GCController](gccontroller.md) object that disconnects from the device.

The system posts this notification on the main thread.

## See Also

### Discovering controllers

- [+ controllers](<gccontroller/controllers().md>) — Returns the connected controllers for the device.
- [+ startWirelessControllerDiscoveryWithCompletionHandler:](<gccontroller/startwirelesscontrollerdiscovery(completionhandler_).md>) — Starts searching for nearby wireless controllers.
- [+ stopWirelessControllerDiscovery](<gccontroller/stopwirelesscontrollerdiscovery().md>) — Stops searching for nearby wireless controllers.
- [GCControllerDidConnectNotification](gccontrollerdidconnectnotification.md) — A notification that posts after a controller connects to the device.
