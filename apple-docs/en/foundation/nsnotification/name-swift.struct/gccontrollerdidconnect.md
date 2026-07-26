---
title: GCControllerDidConnect
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/gccontrollerdidconnect
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gccontrollerdidconnect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/gccontrollerdidconnect.json'
content_hash: 'sha256:f9266b9c0ad35314'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# GCControllerDidConnect

<sub>Type Property</sub>

A notification that posts after a controller connects to the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let GCControllerDidConnect: NSNotification.Name
```

## Discussion

The notification object is the [GCController](../../../gamecontroller/gccontroller.md) object that connects to the device.

The system posts this notification on the main actor.

## See Also

### Game Controller

- [GCControllerDidDisconnect](gccontrollerdiddisconnect.md) — A notification that posts after a controller disconnects from the device.
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
