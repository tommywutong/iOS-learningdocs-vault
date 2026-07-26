---
title: clock
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/clock
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/clock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/clock.json'
content_hash: 'sha256:8e3f3c02d0ae4506'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDevice](../avexternalsyncdevice.md)

# clock

<sub>Instance Property</sub>

A clock representing the source of time from the external sync device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var clock: CMClock? { get }
```

## Discussion

This property returns `NULL` until the [status](status.md) reaches `AVExternalSyncDeviceStatusActiveSync`.

## See Also

### Inspecting a device

- [productID](productid.md) — The USB product identifier associated with the external sync device.
- [signalCompensationDelay](signalcompensationdelay.md) — Delay to wait before starting the frame capture.
- [status](status.md) — The status of the externally connected device.
- [uuid](uuid.md) — A unique identifier for an external sync device.
- [vendorID](vendorid.md) — The USB vendor identifier associated with the external sync device.
