---
title: smartFramingMonitor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/smartframingmonitor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/smartframingmonitor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/smartframingmonitor.json'
content_hash: 'sha256:7c14fda3fbfbba9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# smartFramingMonitor

<sub>Instance Property</sub>

A monitor owned by the device that recommends an optimal framing based on the content in the scene.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var smartFramingMonitor: AVCaptureSmartFramingMonitor? { get }
```

## Discussion

An ultra wide camera device that supports dynamic aspect ratio configuration may also support “smart framing monitoring”. If this property returns non `nil`, you may use it to listen for framing recommendations by configuring its [enabledFramings](../avcapturesmartframingmonitor/enabledframings.md) and calling [- startMonitoringWithError:](<../avcapturesmartframingmonitor/startmonitoring().md>). The smart framing monitor only makes recommendations when the current [activeFormat](activeformat.md) supports smart framing (see [smartFramingSupported](format/issmartframingsupported.md)).

## See Also

### Configuring smart framing

- [AVCaptureSmartFramingMonitor](../avcapturesmartframingmonitor.md) — An object associated with a capture device that monitors the scene and suggests an optimal framing.
- [AVCaptureFraming](../avcaptureframing.md) — A framing, consisting of an aspect ratio and a zoom factor.
