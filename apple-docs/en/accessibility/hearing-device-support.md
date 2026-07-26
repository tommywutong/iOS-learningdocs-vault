---
title: Hearing device support
framework: Accessibility
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/accessibility/hearing-device-support
source_url: 'https://developer.apple.com/documentation/accessibility/hearing-device-support'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/accessibility/hearing-device-support.json'
content_hash: 'sha256:085823a7f14d19b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Accessibility](../accessibility.md) · [Accessibility API](accessibility-api.md)

# Hearing device support

<sub>API Collection</sub>

Access information about paired hearing aid devices and streaming status.

## Overview

Companion apps for hearing device manufacturers might offer certain features, like remote fitting and hearing device health checks, that rely on streaming audio to the hearing devices. If a user disables audio streaming on their Apple device, these features might become unavailable.

This API gives your app the ability to check the state of the streaming preferences, so you can ask users to temporarily enable streaming to use your app’s features. You can also query other information about streaming capabilities and paired hearing devices.

Use this API to check:

- The state of the streaming preferences for the hearing device in each ear
- Whether the iOS device supports bidirectional streaming
- The Bluetooth UUIDs of the paired hearing devices that match your app’s `hearing.aid.app` entitlement

## Topics

### Hearing devices

- [AXMFiHearingDevice](axmfihearingdevice.md) — A namespace for hearing device accessibility symbols in Swift.

### Streaming status

- [Ear](axmfihearingdevice/ear.md) — Constants that represent a hearing device ear.
- [AXMFiHearingDeviceStreamingEar](<axmfihearingdevice/streamingear().md>) — Returns which ears enable streaming.
- [AXMFiHearingDeviceStreamingEarDidChangeNotification](axmfihearingdevice/streamingeardidchangenotification.md) — A notification that the system posts when there’s a change to which ears enable streaming.

### Streaming type

- [AXSupportsBidirectionalAXMFiHearingDeviceStreaming](<axmfihearingdevice/supportsbidirectionalstreaming().md>) — Returns a Boolean value that indicates whether the iOS device supports bidirectional streaming.

### Paired hearing devices

- [AXMFiHearingDevicePairedUUIDs](<axmfihearingdevice/paireddeviceidentifiers().md>) — Returns the UUIDs of the hearing device peripherals.
- [AXMFiHearingDevicePairedUUIDsDidChangeNotification](axmfihearingdevice/paireduuidsdidchangenotification.md) — A notification that the system posts when there’s a change to the UUIDs of the hearing device peripherals.

## See Also

### Features

- [Customized accessibility content](customized-accessibility-content.md) — Customize your apps to deliver accessibility information to your users in measured portions as they need it.
- [Audio graphs](audio-graphs.md) — Define an accessible representation of your chart for VoiceOver to generate an audio graph.
- [AXNameFromColor](<axnamefromcolor(__).md>) — Returns a localized description of the color to use in accessibility attributes.
