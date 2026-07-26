---
title: isLivePhotoCaptureSuspended
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/islivephotocapturesuspended
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islivephotocapturesuspended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/islivephotocapturesuspended.json'
content_hash: 'sha256:c27b1f9f7e9207eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isLivePhotoCaptureSuspended

<sub>Instance Property</sub>

A Boolean value that indicates whether Live Photo capture is currently in a suspended state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLivePhotoCaptureSuspended: Bool { get set }
```

## Discussion

By default, this property’s value is [false](../../swift/false.md). Set this value to [true](../../swift/true.md) to stop any current Live Photo movie captures in progress. Doing this prevents recording additional actions in the Live Photo movie. For example, if you want to capture a still photo that makes a shutter sound, you can prevent recording that action.

When you change this value to [true](../../swift/true.md), the system trims any Live Photo movie captures in progress to the current time. Likewise, when you change this value from [true](../../swift/true.md) to [false](../../swift/false.md), subsequent Live Photo movie captures won’t contain any earlier recordings.

By default, this property resets to [false](../../swift/false.md) when the [AVCaptureSession](../avcapturesession.md) stops. You can prevent this behavior by setting [preservesLivePhotoCaptureSuspendedOnSessionStop](preserveslivephotocapturesuspendedonsessionstop.md) to [true](../../swift/true.md) before stopping the session.

> [!important] Important
> Setting this property to [true](../../swift/true.md) throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if the [livePhotoCaptureEnabled](islivephotocaptureenabled.md) property’s value is [false](../../swift/false.md).

## See Also

### Configuring Live Photo capture

- [livePhotoCaptureSupported](islivephotocapturesupported.md) — A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [livePhotoCaptureEnabled](islivephotocaptureenabled.md) — A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [preservesLivePhotoCaptureSuspendedOnSessionStop](preserveslivephotocapturesuspendedonsessionstop.md) — A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [livePhotoAutoTrimmingEnabled](islivephotoautotrimmingenabled.md) — A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [availableLivePhotoVideoCodecTypes](availablelivephotovideocodectypes.md) — An array of video codecs currently available for Live Photo movie captures.
