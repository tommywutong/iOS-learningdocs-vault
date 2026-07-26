---
title: stopMonitoring()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesmartframingmonitor/stopmonitoring()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/stopmonitoring()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesmartframingmonitor/stopmonitoring%28%29.json'
content_hash: 'sha256:a62a6ea72565cbac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSmartFramingMonitor](../avcapturesmartframingmonitor.md)

# stopMonitoring()

<sub>Instance Method</sub>

Stops monitoring the device’s active scene and making framing recommendations.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func stopMonitoring()
```

## Discussion

The monitor’s [recommendedFraming](recommendedframing.md) is `nil` when it is not actively running. Call this method to stop actively monitoring the scene and making framing recommendations. You may start monitoring before or after calling [- startRunning](<../avcapturesession/startrunning().md>), and may stop active monitoring without stopping the capture session by calling [- stopMonitoring](<stopmonitoring().md>) at any time.

## See Also

### Managing the life cycle

- [monitoring](ismonitoring.md) — Yes when the receiver is actively monitoring.
- [- startMonitoringWithError:](<startmonitoring().md>) — Begins monitoring the device’s active scene and making framing recommendations.
