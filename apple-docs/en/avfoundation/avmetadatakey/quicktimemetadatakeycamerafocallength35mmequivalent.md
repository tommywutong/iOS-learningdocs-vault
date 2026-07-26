---
title: quickTimeMetadataKeyCameraFocalLength35mmEquivalent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatakey/quicktimemetadatakeycamerafocallength35mmequivalent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatakey/quicktimemetadatakeycamerafocallength35mmequivalent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatakey/quicktimemetadatakeycamerafocallength35mmequivalent.json'
content_hash: 'sha256:5fc888e9c75f9e2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataKey](../avmetadatakey.md)

# quickTimeMetadataKeyCameraFocalLength35mmEquivalent

<sub>Type Property</sub>

A value of type kCMMetadataBaseDataType_UTF8 indicating focal length normalized to the 35mm film equivalent value (e.g. “50.00mm”).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let quickTimeMetadataKeyCameraFocalLength35mmEquivalent: AVMetadataKey
```

## Discussion

This is track-level metadata for video track that is associated with the camera.

## See Also

### QuickTime metadata keys

- [AVMetadataQuickTimeMetadataKeyAccessibilityDescription](quicktimemetadatakeyaccessibilitydescription.md) — A key that represents the accessibility description for the movie file content.
- [AVMetadataQuickTimeMetadataKeyAlbum](quicktimemetadatakeyalbum.md) — A key that represents the name of the album or collection in QuickTime.
- [AVMetadataQuickTimeMetadataKeyArranger](quicktimemetadatakeyarranger.md) — A key that represents the name of the arranger of the movie file content.
- [AVMetadataQuickTimeMetadataKeyArtist](quicktimemetadatakeyartist.md) — A key that represents the name of the artist of the movie file content.
- [AVMetadataQuickTimeMetadataKeyArtwork](quicktimemetadatakeyartwork.md) — A key that represents an image relating to the movie file content.
- [AVMetadataQuickTimeMetadataKeyAuthor](quicktimemetadatakeyauthor.md) — A key that represents the name of the author of the movie file content.
- [AVMetadataQuickTimeMetadataKeyCameraFrameReadoutTime](quicktimemetadatakeycameraframereadouttime.md) — A key that represents the camera frame readout time in QuickTime.
- [AVMetadataQuickTimeMetadataKeyCameraISOSensitivity](quicktimemetadatakeycameraisosensitivity.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the sensitivity of the camera to light in terms of ISO exposure index (e.g. “800”). See SMPTE RDD 18.
- [AVMetadataQuickTimeMetadataKeyCameraIdentifier](quicktimemetadatakeycameraidentifier.md) — A key that represents the camera identifier in QuickTime.
- [AVMetadataQuickTimeMetadataKeyCameraLensIrisFNumber](quicktimemetadatakeycameralensirisfnumber.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating measure of the amount of light transmitted through the lens. It is the focal length divided by the effective lens aperture diameter (e.g. “F2.8” or “2.8”).
- [AVMetadataQuickTimeMetadataKeyCameraLensModel](quicktimemetadatakeycameralensmodel.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the lens model (e.g. “iPhone 16 Pro back camera 6.765mm f/1.78”).
- [AVMetadataQuickTimeMetadataKeyCameraShutterSpeedAngle](quicktimemetadatakeycamerashutterspeedangle.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the exposure period expressed as an angle in minutes (1/60 degree) (e.g. “21600” or “360.00deg””).
- [AVMetadataQuickTimeMetadataKeyCameraShutterSpeedTime](quicktimemetadatakeycamerashutterspeedtime.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the exposure period expressed as a time per one frame/field period in seconds.
- [AVMetadataQuickTimeMetadataKeyCameraWhiteBalance](quicktimemetadatakeycamerawhitebalance.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the white balance value defined by the temperature in Kelvin units (e.g. “5500K” or “5500”). See SMPTE RDD 18.
- [AVMetadataQuickTimeMetadataKeyCinematicVideoIntent](quicktimemetadatakeycinematicvideointent.md) — A value of type `kCMMetadataBaseDataType_UInt8` indicating whether this movie is intended as a Cinematic Video (1) or not (0).
