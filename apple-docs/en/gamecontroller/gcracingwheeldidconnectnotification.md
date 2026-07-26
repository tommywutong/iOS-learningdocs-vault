---
title: GCRacingWheelDidConnectNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 16.0+, macOS 13.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gcracingwheeldidconnectnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gcracingwheeldidconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gcracingwheeldidconnectnotification.json'
content_hash: 'sha256:316a75dccfe1179d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCRacingWheelDidConnectNotification

<sub>Global Variable</sub>

A notification that posts after a racing wheel controller connects to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCRacingWheelDidConnectNotification;
```

## Discussion

The notification object is the [GCRacingWheel](gcracingwheel.md) object that connects to the device.

The system posts this notification on the main thread.

## See Also

### Discovering racing wheels

- [connectedRacingWheels](gcracingwheel/connectedracingwheels.md) — The racing wheels connected to the device.
- [GCRacingWheelDidDisconnectNotification](gcracingwheeldiddisconnectnotification.md) — A notification that posts after a racing wheel controller disconnects from the device.
