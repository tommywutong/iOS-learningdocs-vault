---
title: isAudioZoomEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/isaudiozoomenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/isaudiozoomenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/isaudiozoomenabled.json'
content_hash: 'sha256:33f552fead14c590'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# isAudioZoomEnabled

<sub>Instance Property</sub>

Whether or not audio zoom is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isAudioZoomEnabled: Bool { get set }
```

## Discussion

Setting this property to `true` throws an exception if [audioZoomSupported](isaudiozoomsupported.md) is `false`. Default is `true` when supported. When enabled, the sound field narrows or expands to match the field of view of the video device’s zoom factor. Set this property to `false` if you want to capture the full sound field regardless of video zoom. This property only takes effect when added to a session with a video device, and [AVCaptureMultichannelAudioMode](../avcapturemultichannelaudiomode.md) is set to any value other than `AVCaptureMultichannelAudioModeNone`. When using multiple cameras in [AVCaptureMultiCamSession](../avcapturemulticamsession.md), audio zoom is determined by the zoom factor of the preferred camera. The preferred camera is selected to match the mic position, either front or back. If more than one camera is available in that position, the camera with the widest field of view is chosen with virtual cameras preferred over single camera ones. If no camera is found to match the mic position, audio zoom is unavailable.
