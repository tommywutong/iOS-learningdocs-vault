---
title: preservesLivePhotoCaptureSuspendedOnSessionStop
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop.json'
content_hash: 'sha256:060634eaf9c257fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# preservesLivePhotoCaptureSuspendedOnSessionStop

<sub>Instance Property</sub>

A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var preservesLivePhotoCaptureSuspendedOnSessionStop: Bool { get set }
```

## Discussion

This value defaults to [false](../../swift/false.md), which means that Live Photo capture resumes when the session stops. Set the value to [true](../../swift/true.md) to save the state of the [livePhotoCaptureSuspended](islivephotocapturesuspended.md) property across session restarts.

## See Also

### Configuring Live Photo capture

- [livePhotoCaptureSupported](islivephotocapturesupported.md) — A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [livePhotoCaptureEnabled](islivephotocaptureenabled.md) — A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [livePhotoCaptureSuspended](islivephotocapturesuspended.md) — A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [livePhotoAutoTrimmingEnabled](islivephotoautotrimmingenabled.md) — A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [availableLivePhotoVideoCodecTypes](availablelivephotovideocodectypes.md) — An array of video codecs currently available for Live Photo movie captures.
