---
title: inputPriority
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/preset/inputpriority
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/inputpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/preset/inputpriority.json'
content_hash: 'sha256:a3adb92073b4a695'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureSession](../../avcapturesession.md) · [Preset](../preset.md)

# inputPriority

<sub>Type Property</sub>

A preset that doesn’t specify audio and video output settings for a capture session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let inputPriority: AVCaptureSession.Preset
```

## Discussion

To enable capture settings not supported by any session presets (such as high frame rate), change the value of the [activeFormat](../../avcapturedevice/activeformat.md) property on the appropriate capture device. When you change the device’s format, the session preset automatically changes to this value, indicating that the [AVCaptureSession](../../avcapturesession.md) object has relinquished responsibility for configuring its inputs and outputs. (Instead, the capture device’s active format dictates the quality of service level provided at the outputs). To return to automatic configuration, use the session’s [sessionPreset](../sessionpreset.md) property to choose another preset.
