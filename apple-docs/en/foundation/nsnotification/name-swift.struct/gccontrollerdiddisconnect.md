---
title: GCControllerDidDisconnect
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/gccontrollerdiddisconnect
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gccontrollerdiddisconnect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/gccontrollerdiddisconnect.json'
content_hash: 'sha256:628850a6ce5deb93'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# GCControllerDidDisconnect

<sub>Type Property</sub>

A notification that posts after a controller disconnects from the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let GCControllerDidDisconnect: NSNotification.Name
```

## Discussion

The notification object is the [GCController](../../../gamecontroller/gccontroller.md) object that disconnects from the device.

The system posts this notification on the main actor.

## See Also

### Game Controller

- [GCControllerDidConnect](gccontrollerdidconnect.md) — A notification that posts after a controller connects to the device.
- [GCControllerDidBecomeCurrent](gccontrollerdidbecomecurrent.md) — A notification that posts when a controller becomes the current controller.
- [GCControllerDidStopBeingCurrent](gccontrollerdidstopbeingcurrent.md) — A notification that posts when a controller stops being the current controller.
- [GCControllerUserCustomizationsDidChange](gccontrollerusercustomizationsdidchange.md) — A notification that posts when the user customizes the button mappings or other settings of a controller.
- [GCKeyboardDidConnect](gckeyboarddidconnect.md) — A notification that posts after a keyboard connects to the device.
- [GCKeyboardDidDisconnect](gckeyboarddiddisconnect.md) — A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
- [GCMouseDidBecomeCurrent](gcmousedidbecomecurrent.md) — A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [GCMouseDidConnect](gcmousedidconnect.md) — A notification that posts after a mouse connects to the device.
- [GCMouseDidDisconnect](gcmousediddisconnect.md) — A notification that posts after a mouse disconnects from the device.
- [GCMouseDidStopBeingCurrent](gcmousedidstopbeingcurrent.md) — A notification that posts when a mouse stops being the most recent mouse that the user connects.
- [GCRacingWheelDidConnect](gcracingwheeldidconnect.md) — A notification that posts after a racing wheel controller connects to the device.
- [GCRacingWheelDidDisconnect](gcracingwheeldiddisconnect.md) — A notification that posts after a racing wheel controller disconnects from the device.
