---
title: GCControllerDidConnectNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gccontrollerdidconnectnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gccontrollerdidconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gccontrollerdidconnectnotification.json'
content_hash: 'sha256:65b5eec270054520'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCControllerDidConnectNotification

<sub>Global Variable</sub>

A notification that posts after a controller connects to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCControllerDidConnectNotification;
```

## Discussion

The notification object is the [GCController](gccontroller.md) object that connects to the device.

The system posts this notification on the main thread.

## See Also

### Discovering controllers

- [+ controllers](<gccontroller/controllers().md>) — Returns the connected controllers for the device.
- [+ startWirelessControllerDiscoveryWithCompletionHandler:](<gccontroller/startwirelesscontrollerdiscovery(completionhandler_).md>) — Starts searching for nearby wireless controllers.
- [+ stopWirelessControllerDiscovery](<gccontroller/stopwirelesscontrollerdiscovery().md>) — Stops searching for nearby wireless controllers.
- [GCControllerDidDisconnectNotification](gccontrollerdiddisconnectnotification.md) — A notification that posts after a controller disconnects from the device.
