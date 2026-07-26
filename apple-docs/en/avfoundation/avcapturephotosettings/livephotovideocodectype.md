---
title: livePhotoVideoCodecType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/livephotovideocodectype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/livephotovideocodectype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/livephotovideocodectype.json'
content_hash: 'sha256:42ae1bd65a3dd90e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# livePhotoVideoCodecType

<sub>Instance Property</sub>

The video codec to use for encoding the movie portion of Live Photo output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var livePhotoVideoCodecType: AVVideoCodecType { get set }
```

## Discussion

This value must be one of the video codec types listed in the photo output’s [availableLivePhotoVideoCodecTypes](../avcapturephotooutput/availablelivephotovideocodectypes.md) array.

## See Also

### Configuring Live Photo settings

- [livePhotoMovieFileURL](livephotomoviefileurl.md) — A URL at which to write Live Photo movie output.
- [livePhotoMovieMetadata](livephotomoviemetadata.md) — A dictionary of metadata to include in the Live Photo movie file.
