---
title: GCKeyboardDidDisconnectNotification
framework: Game Controller
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/gamecontroller/gckeyboarddiddisconnectnotification
source_url: 'https://developer.apple.com/documentation/gamecontroller/gckeyboarddiddisconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamecontroller/gckeyboarddiddisconnectnotification.json'
content_hash: 'sha256:4b9f8eb05c50c242'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Game Controller](../gamecontroller.md)

# GCKeyboardDidDisconnectNotification

<sub>Global Variable</sub>

A notification that posts after a single keyboard, or the last of multiple keyboards, disconnects from the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const GCKeyboardDidDisconnectNotification;
```

## Discussion

The notification object is a [GCKeyboard](gckeyboard.md) object that represents one or more keyboards. If the user connects multiple keyboards, the framework posts this notification only after the last keyboard disconnects from the device.

The system posts this notification on the main thread.

## See Also

### Discovering keyboards

- [coalescedKeyboard](gckeyboard/coalesced.md) — The keyboard currently connected to the device.
- [GCKeyboardDidConnectNotification](gckeyboarddidconnectnotification.md) — A notification that posts after a keyboard connects to the device.
