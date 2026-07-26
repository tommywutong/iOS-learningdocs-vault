---
title: availableLivePhotoVideoCodecTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/availablelivephotovideocodectypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablelivephotovideocodectypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/availablelivephotovideocodectypes.json'
content_hash: 'sha256:eb10158a081deee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# availableLivePhotoVideoCodecTypes

<sub>Instance Property</sub>

An array of video codecs currently available for Live Photo movie captures.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var availableLivePhotoVideoCodecTypes: [AVVideoCodecType] { get }
```

## Discussion

By default, Live Photo capture encodes the movie portion of a Live Photo using the H.264 codec. To use a different codec, set the [livePhotoVideoCodecType](../avcapturephotosettings/livephotovideocodectype.md) property of your photo settings object to one of the values in this array.

The system always presents its default video codec first. If you haven’t added the photo output to an [AVCaptureSession](../avcapturesession.md) with a video source, no codecs are available.

This property is key-value observable.

## See Also

### Configuring Live Photo capture

- [livePhotoCaptureSupported](islivephotocapturesupported.md) — A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [livePhotoCaptureEnabled](islivephotocaptureenabled.md) — A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [livePhotoCaptureSuspended](islivephotocapturesuspended.md) — A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [preservesLivePhotoCaptureSuspendedOnSessionStop](preserveslivephotocapturesuspendedonsessionstop.md) — A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [livePhotoAutoTrimmingEnabled](islivephotoautotrimmingenabled.md) — A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
