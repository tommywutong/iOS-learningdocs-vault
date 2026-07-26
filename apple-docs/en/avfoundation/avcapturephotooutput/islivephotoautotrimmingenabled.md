---
title: isLivePhotoAutoTrimmingEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/islivephotoautotrimmingenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotoautotrimmingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/islivephotoautotrimmingenabled.json'
content_hash: 'sha256:6c8275ff731654ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isLivePhotoAutoTrimmingEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLivePhotoAutoTrimmingEnabled: Bool { get set }
```

## Discussion

This value defaults to [true](../../swift/true.md) when [livePhotoCaptureSupported](islivephotocapturesupported.md) is [true](../../swift/true.md).

Use this option to enable the same automatic trimming behavior found in the Camera app. By default, a Live Photo capture is about three seconds in duration, centered on the time of the capture request. If the user moves the camera during capture, iOS analyzes the capture and automatically trims the duration of the Live Photo to avoid capturing excess movement.

Changing this value while your session is running requires a lengthy reconfiguration of the session. If you intend to take any Live Photo captures, set this value to [true](../../swift/true.md) before calling [AVCaptureSession](../avcapturesession.md) [- startRunning](<../avcapturesession/startrunning().md>). If you change this property while the session is running, in-progress Live Photo captures end immediately, unfulfilled photo requests cancel, and the video preview temporarily freezes.

## See Also

### Configuring Live Photo capture

- [livePhotoCaptureSupported](islivephotocapturesupported.md) — A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [livePhotoCaptureEnabled](islivephotocaptureenabled.md) — A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [livePhotoCaptureSuspended](islivephotocapturesuspended.md) — A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [preservesLivePhotoCaptureSuspendedOnSessionStop](preserveslivephotocapturesuspendedonsessionstop.md) — A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [availableLivePhotoVideoCodecTypes](availablelivephotovideocodectypes.md) — An array of video codecs currently available for Live Photo movie captures.
