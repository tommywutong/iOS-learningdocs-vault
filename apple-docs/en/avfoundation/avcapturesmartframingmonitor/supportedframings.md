---
title: supportedFramings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesmartframingmonitor/supportedframings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/supportedframings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesmartframingmonitor/supportedframings.json'
content_hash: 'sha256:8cddb24072a4d491'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSmartFramingMonitor](../avcapturesmartframingmonitor.md)

# supportedFramings

<sub>Instance Property</sub>

An array of framings supported by the monitor in its current configuration.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var supportedFramings: [AVCaptureFraming] { get }
```

## Discussion

The monitor is capable of recommending any of the framings in this array. This property is key-value observable and may change as the target capture device’s [activeFormat](../avcapturedevice/activeformat.md) property changes. This array contains the full set of framings supported by the monitor in the device’s current configuration. You must tell the monitor which smart framings you are interested in having recommended to you by setting the [enabledFramings](enabledframings.md) property.

## See Also

### Configuring framings

- [enabledFramings](enabledframings.md) — An array of framings that the monitor is allowed to suggest.
- [recommendedFraming](recommendedframing.md) — The latest recommended framing from the monitor.
