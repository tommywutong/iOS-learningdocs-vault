---
title: isCameraLensSmudgeDetectionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/iscameralenssmudgedetectionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/iscameralenssmudgedetectionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/iscameralenssmudgedetectionsupported.json'
content_hash: 'sha256:d68ea3e5e77c4114'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isCameraLensSmudgeDetectionSupported

<sub>Instance Property</sub>

Whether camera lens smudge detection is supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isCameraLensSmudgeDetectionSupported: Bool { get }
```

## Discussion

This property returns `true` if the session’s current configuration supports lens smudge detection. When switching cameras or formats, this property may change. When this property changes from `true` to `false`, [cameraLensSmudgeDetectionEnabled](../iscameralenssmudgedetectionenabled.md) also reverts to `false`. If you opt in for lens smudge detection and then change configurations, you should set [cameraLensSmudgeDetectionEnabled](../iscameralenssmudgedetectionenabled.md) to `true` again.
