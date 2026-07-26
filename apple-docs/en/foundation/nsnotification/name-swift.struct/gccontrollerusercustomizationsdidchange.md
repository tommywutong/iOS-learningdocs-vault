---
title: GCControllerUserCustomizationsDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/gccontrollerusercustomizationsdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gccontrollerusercustomizationsdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/gccontrollerusercustomizationsdidchange.json'
content_hash: 'sha256:b016e54bf4f883db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# GCControllerUserCustomizationsDidChange

<sub>Type Property</sub>

A notification that posts when the user customizes the button mappings or other settings of a controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let GCControllerUserCustomizationsDidChange: NSNotification.Name
```

## Discussion

Use this notification to update your interface when the mappings change. The notification object is the [GCController](../../../gamecontroller/gccontroller.md) object that the user customizes.

The system posts this notification on the main actor.

## See Also

### Game Controller

- [GCControllerDidConnect](gccontrollerdidconnect.md) — A notification that posts after a controller connects to the device.
- [GCControllerDidDisconnect](gccontrollerdiddisconnect.md) — A notification that posts after a controller disconnects from the device.
- [GCControllerDidBecomeCurrent](gccontrollerdidbecomecurrent.md) — A notification that posts when a controller becomes the current controller.
- [GCControllerDidStopBeingCurrent](gccontrollerdidstopbeingcurrent.md) — A notification that posts when a controller stops being the current controller.
- [GCKeyboardDidConnect](gckeyboarddidconnect.md) — A notification that posts after a keyboard connects to the device.
- [GCKeyboardDidDisconnect](gckeyboarddiddisconnect.md) — A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.
- [GCMouseDidBecomeCurrent](gcmousedidbecomecurrent.md) — A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [GCMouseDidConnect](gcmousedidconnect.md) — A notification that posts after a mouse connects to the device.
- [GCMouseDidDisconnect](gcmousediddisconnect.md) — A notification that posts after a mouse disconnects from the device.
- [GCMouseDidStopBeingCurrent](gcmousedidstopbeingcurrent.md) — A notification that posts when a mouse stops being the most recent mouse that the user connects.
- [GCRacingWheelDidConnect](gcracingwheeldidconnect.md) — A notification that posts after a racing wheel controller connects to the device.
- [GCRacingWheelDidDisconnect](gcracingwheeldiddisconnect.md) — A notification that posts after a racing wheel controller disconnects from the device.
