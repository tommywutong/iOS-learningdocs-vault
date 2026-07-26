---
title: photoLive
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetmediasubtype/photolive
source_url: 'https://developer.apple.com/documentation/photos/phassetmediasubtype/photolive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetmediasubtype/photolive.json'
content_hash: 'sha256:5aef86c2fa6bf017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetMediaSubtype](../phassetmediasubtype.md)

# photoLive

<sub>Type Property</sub>

The asset is a Live Photo that includes movement and sounds from the moments just before and after its capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var photoLive: PHAssetMediaSubtype { get }
```

## Discussion

To display a Live Photo asset with its associated video content, retrieve a [PHLivePhoto](../phlivephoto.md) object using the [PHImageManager](../phimagemanager.md) class and assign it to a [PHLivePhotoView](../../photosui/phlivephotoview.md) object.

## See Also

### Media Subtypes

- [PHAssetMediaSubtypePhotoPanorama](photopanorama.md) — The asset is a large-format panorama photo.
- [PHAssetMediaSubtypePhotoHDR](photohdr.md) — The asset is a high-dynamic range photo.
- [PHAssetMediaSubtypePhotoScreenshot](photoscreenshot.md) — The asset is an image captured with the device’s screenshot feature.
- [PHAssetMediaSubtypeVideoCinematic](videocinematic.md) — The asset is a cinematic video.
- [PHAssetMediaSubtypeVideoStreamed](videostreamed.md) — The asset is a video with contents that always stream over a network connection.
- [PHAssetMediaSubtypeVideoHighFrameRate](videohighframerate.md) — The asset is a high-frame-rate video.
- [PHAssetMediaSubtypeVideoTimelapse](videotimelapse.md) — The asset is a time-lapse video.
- [PHAssetMediaSubtypePhotoDepthEffect](photodeptheffect.md) — The asset is a photo captured with the Camera app’s Portrait mode depth effect.
