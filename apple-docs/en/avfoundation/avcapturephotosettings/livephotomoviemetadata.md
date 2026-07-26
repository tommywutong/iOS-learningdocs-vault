---
title: livePhotoMovieMetadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/livephotomoviemetadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/livephotomoviemetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/livephotomoviemetadata.json'
content_hash: 'sha256:ba9a235ed8dfe6bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# livePhotoMovieMetadata

<sub>Instance Property</sub>

A dictionary of metadata to include in the Live Photo movie file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var livePhotoMovieMetadata: [AVMetadataItem]! { get set }
```

## Discussion

Live Photos capture both a still image and a short movie, which the system presents together in user interfaces such as the Photos app. A Live Photo movie always contains a `AVMetadataQuickTimeMetadataKeyContentIdentifier` key, associating the movie with a similar identifier in the [kCGImagePropertyExifMakerNote](../../imageio/kcgimagepropertyexifmakernote.md) property of the corresponding still image. The photo capture output automatically generates a unique content identifier for you if you don’t specify one of your own. You can also use this property to specify additional movie metadata.

This property applies only if the value of the [livePhotoMovieFileURL](livephotomoviefileurl.md) property is to non-`nil`.

## See Also

### Configuring Live Photo settings

- [livePhotoMovieFileURL](livephotomoviefileurl.md) — A URL at which to write Live Photo movie output.
- [livePhotoVideoCodecType](livephotovideocodectype.md) — The video codec to use for encoding the movie portion of Live Photo output.
