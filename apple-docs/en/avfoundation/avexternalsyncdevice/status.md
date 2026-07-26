---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/status
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/status'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/status.json'
content_hash: 'sha256:6c7e98d4a8954a8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDevice](../avexternalsyncdevice.md)

# status

<sub>Instance Property</sub>

The status of the externally connected device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var status: AVExternalSyncDeviceStatus { get }
```

## Discussion

Use this property to query the current connection status of the external sync device. This property is key-value observable.

## See Also

### Inspecting a device

- [clock](clock.md) — A clock representing the source of time from the external sync device.
- [productID](productid.md) — The USB product identifier associated with the external sync device.
- [signalCompensationDelay](signalcompensationdelay.md) — Delay to wait before starting the frame capture.
- [uuid](uuid.md) — A unique identifier for an external sync device.
- [vendorID](vendorid.md) — The USB vendor identifier associated with the external sync device.
