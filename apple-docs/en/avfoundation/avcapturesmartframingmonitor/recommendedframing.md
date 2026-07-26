---
title: recommendedFraming
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesmartframingmonitor/recommendedframing
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesmartframingmonitor/recommendedframing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesmartframingmonitor/recommendedframing.json'
content_hash: 'sha256:1f2cedc4b758adbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSmartFramingMonitor](../avcapturesmartframingmonitor.md)

# recommendedFraming

<sub>Instance Property</sub>

The latest recommended framing from the monitor.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var recommendedFraming: AVCaptureFraming? { get }
```

## Discussion

While your [AVCaptureSession](../avcapturesession.md) is running, the monitor continuously observes its device’s scene to recommend the best framing. This recommended framing is always one of the values in [enabledFramings](enabledframings.md). This property may return `nil` if smart framing isn’t supported for the device in its current configuration. Its default value is `nil`. This property is key-value observable, and when you observe a change, you may respond to the new recommendation by calling [- setDynamicAspectRatio:completionHandler:](<../avcapturedevice/setdynamicaspectratio(__completionhandler_).md>) and setting [videoZoomFactor](../avcapturedevice/videozoomfactor.md) on the associated device in whatever order best matches your animation between old and new framings.

## See Also

### Configuring framings

- [supportedFramings](supportedframings.md) — An array of framings supported by the monitor in its current configuration.
- [enabledFramings](enabledframings.md) — An array of framings that the monitor is allowed to suggest.
