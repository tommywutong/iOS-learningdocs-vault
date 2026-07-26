---
title: isMonitoring
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesmartframingmonitor/ismonitoring
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/ismonitoring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesmartframingmonitor/ismonitoring.json'
content_hash: 'sha256:e370c94bee4adf23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSmartFramingMonitor](../avcapturesmartframingmonitor.md)

# isMonitoring

<sub>Instance Property</sub>

Yes when the receiver is actively monitoring.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isMonitoring: Bool { get }
```

## Discussion

See [- startMonitoringWithError:](<startmonitoring().md>) and [- stopMonitoring](<stopmonitoring().md>).

## See Also

### Managing the life cycle

- [- startMonitoringWithError:](<startmonitoring().md>) — Begins monitoring the device’s active scene and making framing recommendations.
- [- stopMonitoring](<stopmonitoring().md>) — Stops monitoring the device’s active scene and making framing recommendations.
