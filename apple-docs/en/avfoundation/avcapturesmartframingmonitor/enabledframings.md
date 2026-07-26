---
title: enabledFramings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesmartframingmonitor/enabledframings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/enabledframings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesmartframingmonitor/enabledframings.json'
content_hash: 'sha256:9eddccc3d47503eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSmartFramingMonitor](../avcapturesmartframingmonitor.md)

# enabledFramings

<sub>Instance Property</sub>

An array of framings that the monitor is allowed to suggest.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var enabledFramings: [AVCaptureFraming] { get set }
```

## Discussion

The monitor is capable of recommending any of the framings in the [supportedFramings](supportedframings.md) array. This property contains the subset of [supportedFramings](supportedframings.md) you would like to have recommended to you. You may set this property at any time while running your [AVCaptureSession](../avcapturesession.md). This property’s default value is the empty array.

## See Also

### Configuring framings

- [supportedFramings](supportedframings.md) — An array of framings supported by the monitor in its current configuration.
- [recommendedFraming](recommendedframing.md) — The latest recommended framing from the monitor.
