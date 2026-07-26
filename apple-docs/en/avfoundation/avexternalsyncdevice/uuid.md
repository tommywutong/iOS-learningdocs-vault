---
title: uuid
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/uuid
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/uuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/uuid.json'
content_hash: 'sha256:257ff7fc0b1d4c29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDevice](../avexternalsyncdevice.md)

# uuid

<sub>Instance Property</sub>

A unique identifier for an external sync device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var uuid: UUID { get }
```

## Discussion

Use this property to select a specific external sync device.

## See Also

### Inspecting a device

- [clock](clock.md) — A clock representing the source of time from the external sync device.
- [productID](productid.md) — The USB product identifier associated with the external sync device.
- [signalCompensationDelay](signalcompensationdelay.md) — Delay to wait before starting the frame capture.
- [status](status.md) — The status of the externally connected device.
- [vendorID](vendorid.md) — The USB vendor identifier associated with the external sync device.
