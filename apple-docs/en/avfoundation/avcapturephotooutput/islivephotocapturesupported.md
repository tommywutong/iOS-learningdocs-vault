---
title: isLivePhotoCaptureSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/islivephotocapturesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotocapturesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/islivephotocapturesupported.json'
content_hash: 'sha256:b7a0d396773d9b5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isLivePhotoCaptureSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture output currently supports Live Photo capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLivePhotoCaptureSupported: Bool { get }
```

## Discussion

Live Photo captures both a still image and a short movie centered on the moment of capture, and the system presents them together in user interfaces such as the Photos app.

Not all devices and capture formats support Live Photo capture. This property’s value can change if the [sessionPreset](../avcapturesession/sessionpreset.md) property of the current capture session or the [activeFormat](../avcapturedevice/activeformat.md) property of the underlying capture device changes.

When this value changes to [false](../../swift/false.md), the [livePhotoCaptureEnabled](islivephotocaptureenabled.md) property’s value also changes to [false](../../swift/false.md). If you previously opted in for Live Photo capture and then change configurations, you may need to set [livePhotoCaptureEnabled](islivephotocaptureenabled.md) to [true](../../swift/true.md) again.

## See Also

### Configuring Live Photo capture

- [livePhotoCaptureEnabled](islivephotocaptureenabled.md) — A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [livePhotoCaptureSuspended](islivephotocapturesuspended.md) — A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [preservesLivePhotoCaptureSuspendedOnSessionStop](preserveslivephotocapturesuspendedonsessionstop.md) — A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [livePhotoAutoTrimmingEnabled](islivephotoautotrimmingenabled.md) — A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [availableLivePhotoVideoCodecTypes](availablelivephotovideocodectypes.md) — An array of video codecs currently available for Live Photo movie captures.
