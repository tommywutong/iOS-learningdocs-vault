---
title: livePhotoMovieFileURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/livephotomoviefileurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/livephotomoviefileurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/livephotomoviefileurl.json'
content_hash: 'sha256:02a5298884061cf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# livePhotoMovieFileURL

<sub>Instance Property</sub>

A URL at which to write Live Photo movie output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var livePhotoMovieFileURL: URL? { get set }
```

## Discussion

Live Photos capture both a still image and a short movie, which the system presents together in user interfaces such as the Photos app. By default, this property’s value is `nil`, disabling Live Photo capture. Set this property to a file URL to capture Live Photos.

When you enable Live Photo capture, the following requirements apply:

- The photo output’s [livePhotoCaptureEnabled](../avcapturephotooutput/islivephotocaptureenabled.md) property must be [true](../../swift/true.md), and its and [livePhotoCaptureSuspended](../avcapturephotooutput/islivephotocapturesuspended.md) property must be [false](../../swift/false.md).
- The URL you specify must be a file URL to an accessible location in your app’s sandbox.
- Your delegate object must implement the [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) method.

The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## See Also

### Configuring Live Photo settings

- [livePhotoMovieMetadata](livephotomoviemetadata.md) — A dictionary of metadata to include in the Live Photo movie file.
- [livePhotoVideoCodecType](livephotovideocodectype.md) — The video codec to use for encoding the movie portion of Live Photo output.
