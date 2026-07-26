---
title: AVExternalSyncDeviceStatus.activeSync
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevicestatus/activesync
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevicestatus/activesync'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevicestatus/activesync.json'
content_hash: 'sha256:5a72647b2131f8f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDeviceStatus](../avexternalsyncdevicestatus.md)

# AVExternalSyncDeviceStatus.activeSync

<sub>Case</sub>

Indicates that the [AVExternalSyncDevice](../avexternalsyncdevice.md) object is running and that the clock property on [AVExternalSyncDevice](../avexternalsyncdevice.md) is calibrated to the external sync signal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case activeSync
```

## See Also

### Status values

- [AVExternalSyncDeviceStatusCalibrating](calibrating.md) — Indicates that the external sync signal is connected and that the AVExternalSyncDevice object is calibrating to follow.
- [AVExternalSyncDeviceStatusFreeRunSync](freerunsync.md) — Indicates that the AVExternalSyncDevice was calibrated to follow the external sync, but the sync signal has been lost. The camera will continue to match the last signal it received, but sync is not guaranteed.
- [AVExternalSyncDeviceStatusReady](ready.md) — Indicates that a device supporting external sync is connected, but calibration has not started.
- [AVExternalSyncDeviceStatusUnavailable](unavailable.md) — Indicates that external sync signal is not connected, or has transitioned to a state that is not recoverable.
