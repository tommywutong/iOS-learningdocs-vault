---
title: Audio Input Entitlement
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.device.audio-input
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.device.audio-input'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.device.audio-input.json'
content_hash: 'sha256:f46e97522eb78a63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# Audio Input Entitlement

<sub>Property List Key</sub>

A Boolean value that indicates whether the app may record audio using the built-in microphone and access audio input using Core Audio.

## Discussion

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Resource Access, select Audio Input.

## See Also

### Device access

- [Camera entitlement](com.apple.security.device.camera.md) — A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.
- [com.apple.security.device.microphone](com.apple.security.device.microphone.md) — A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](com.apple.security.device.usb.md) — A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](com.apple.security.print.md) — A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](com.apple.security.device.bluetooth.md) — A Boolean value indicating whether your app may interact with Bluetooth devices.
- [com.apple.security.smartcard](com.apple.security.smartcard.md) — A Boolean that indicates whether your app has access to smart card slots and smart cards.
