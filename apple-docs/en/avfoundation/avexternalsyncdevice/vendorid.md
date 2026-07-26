---
title: vendorID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/vendorid
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/vendorid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/vendorid.json'
content_hash: 'sha256:9f1dbc855df2220c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDevice](../avexternalsyncdevice.md)

# vendorID

<sub>Instance Property</sub>

The USB vendor identifier associated with the external sync device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var vendorID: UInt32 { get }
```

## Discussion

This `UInt32` value is provided by the hardware vendor, and returns 0 if not available.

## See Also

### Inspecting a device

- [clock](clock.md) — A clock representing the source of time from the external sync device.
- [productID](productid.md) — The USB product identifier associated with the external sync device.
- [signalCompensationDelay](signalcompensationdelay.md) — Delay to wait before starting the frame capture.
- [status](status.md) — The status of the externally connected device.
- [uuid](uuid.md) — A unique identifier for an external sync device.
