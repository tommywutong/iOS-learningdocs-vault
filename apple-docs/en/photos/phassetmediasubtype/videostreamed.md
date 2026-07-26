---
title: videoStreamed
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetmediasubtype/videostreamed
source_url: 'https://developer.apple.com/documentation/photos/phassetmediasubtype/videostreamed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetmediasubtype/videostreamed.json'
content_hash: 'sha256:56f34f63d7d84e54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetMediaSubtype](../phassetmediasubtype.md)

# videoStreamed

<sub>Type Property</sub>

The asset is a video with contents that always stream over a network connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var videoStreamed: PHAssetMediaSubtype { get }
```

## Discussion

This subtype identifies video assets that are never stored on the local device, such as shared videos in a subscribed iCloud Photo Stream.

## See Also

### Media Subtypes

- [PHAssetMediaSubtypePhotoPanorama](photopanorama.md) — The asset is a large-format panorama photo.
- [PHAssetMediaSubtypePhotoHDR](photohdr.md) — The asset is a high-dynamic range photo.
- [PHAssetMediaSubtypePhotoScreenshot](photoscreenshot.md) — The asset is an image captured with the device’s screenshot feature.
- [PHAssetMediaSubtypePhotoLive](photolive.md) — The asset is a Live Photo that includes movement and sounds from the moments just before and after its capture.
- [PHAssetMediaSubtypeVideoCinematic](videocinematic.md) — The asset is a cinematic video.
- [PHAssetMediaSubtypeVideoHighFrameRate](videohighframerate.md) — The asset is a high-frame-rate video.
- [PHAssetMediaSubtypeVideoTimelapse](videotimelapse.md) — The asset is a time-lapse video.
- [PHAssetMediaSubtypePhotoDepthEffect](photodeptheffect.md) — The asset is a photo captured with the Camera app’s Portrait mode depth effect.
