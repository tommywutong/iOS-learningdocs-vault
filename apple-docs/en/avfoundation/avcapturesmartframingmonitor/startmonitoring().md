---
title: startMonitoring()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesmartframingmonitor/startmonitoring()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/startmonitoring()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesmartframingmonitor/startmonitoring%28%29.json'
content_hash: 'sha256:ef5f829fcf836733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSmartFramingMonitor](../avcapturesmartframingmonitor.md)

# startMonitoring()

<sub>Instance Method</sub>

Begins monitoring the device’s active scene and making framing recommendations.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func startMonitoring() throws
```

## Discussion

The monitor’s [recommendedFraming](recommendedframing.md) is `nil` when it is not actively running. Call this method to start monitoring. You may start monitoring before or after calling [- startRunning](<../avcapturesession/startrunning().md>),  and you may stop active monitoring without stopping the capture session by calling [- stopMonitoring](<stopmonitoring().md>) at any time, but you must set [enabledFramings](enabledframings.md) before running your capture session so that the monitor is prepared for your desired framing recommendations. While the monitor is running, you may set [enabledFramings](enabledframings.md) at any time to change the framing choices the monitor should consider in its recommendations.

## See Also

### Managing the life cycle

- [monitoring](ismonitoring.md) — Yes when the receiver is actively monitoring.
- [- stopMonitoring](<stopmonitoring().md>) — Stops monitoring the device’s active scene and making framing recommendations.
