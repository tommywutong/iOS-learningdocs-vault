---
title: signalCompensationDelay
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/signalcompensationdelay
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/signalcompensationdelay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/signalcompensationdelay.json'
content_hash: 'sha256:18488b1ff3bf1ab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDevice](../avexternalsyncdevice.md)

# signalCompensationDelay

<sub>Instance Property</sub>

Delay to wait before starting the frame capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var signalCompensationDelay: CMTime { get set }
```

## Discussion

An external sync is generally used to configure multiple devices in the real world. A display and a camera may receive a signal at the same time, but that does not mean the refresh of the display and camera are aligned in a way that does not cause tearing in the recording. The signal compensation delay can be used to offset the readout of a camera on an intra-frame scale.

Setting this property throws an NSInvalidArgumentException if called when [signalCompensationDelaySupported](issignalcompensationdelaysupported.md) returns NO.

> [!important] Important
> You should always set this property to a value less than the frame duration at which the camera is operating.

## See Also

### Inspecting a device

- [clock](clock.md) — A clock representing the source of time from the external sync device.
- [productID](productid.md) — The USB product identifier associated with the external sync device.
- [status](status.md) — The status of the externally connected device.
- [uuid](uuid.md) — A unique identifier for an external sync device.
- [vendorID](vendorid.md) — The USB vendor identifier associated with the external sync device.
