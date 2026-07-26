---
title: isLivePhotoCaptureEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/islivephotocaptureenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotocaptureenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/islivephotocaptureenabled.json'
content_hash: 'sha256:bf3428284c6b6bfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isLivePhotoCaptureEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLivePhotoCaptureEnabled: Bool { get set }
```

## Discussion

This value defaults to [false](../../swift/false.md). Changing this value while your session is running requires a lengthy reconfiguration of the capture render pipeline. If you intend to take any Live Photo captures, set this value to [true](../../swift/true.md) before calling [AVCaptureSession](../avcapturesession.md) [- startRunning](<../avcapturesession/startrunning().md>). If you change this property while the session is running, in-progress Live Photo captures end immediately, unfulfilled photo requests cancel, and the video preview temporarily freezes.

You must enable this option before initiating a photo capture with the [livePhotoMovieFileURL](../avcapturephotosettings/livephotomoviefileurl.md) property of your photo settings object set to non-`nil`. However, after you’ve enabled this option, you can issue photo capture requests for both Live Photo captures and still photos.

## See Also

### Configuring Live Photo capture

- [livePhotoCaptureSupported](islivephotocapturesupported.md) — A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [livePhotoCaptureSuspended](islivephotocapturesuspended.md) — A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [preservesLivePhotoCaptureSuspendedOnSessionStop](preserveslivephotocapturesuspendedonsessionstop.md) — A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [livePhotoAutoTrimmingEnabled](islivephotoautotrimmingenabled.md) — A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [availableLivePhotoVideoCodecTypes](availablelivephotovideocodectypes.md) — An array of video codecs currently available for Live Photo movie captures.
