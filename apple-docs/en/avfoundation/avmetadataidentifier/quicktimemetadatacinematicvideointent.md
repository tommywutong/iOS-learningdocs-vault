---
title: quickTimeMetadataCinematicVideoIntent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataidentifier/quicktimemetadatacinematicvideointent
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/quicktimemetadatacinematicvideointent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataidentifier/quicktimemetadatacinematicvideointent.json'
content_hash: 'sha256:c4937e18e1b5eaa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataIdentifier](../avmetadataidentifier.md)

# quickTimeMetadataCinematicVideoIntent

<sub>Type Property</sub>

A value of type `kCMMetadataBaseDataType_UInt8` indicating whether this movie is intended as a Cinematic Video (1) or not (0).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let quickTimeMetadataCinematicVideoIntent: AVMetadataIdentifier
```

## Discussion

This movie-level metadata is automatically added (with a value of 1) to a movie recorded using the Cinematic Video API. Clients can override it with a value of 0 to signal that this movie is not to be treated as a Cinematic Video by Apple’s software like Photos.

## See Also

### QuickTime metadata identifiers

- [AVMetadataIdentifierQuickTimeMetadataAIMEData](quicktimemetadataaimedata.md) — A value of type kCMMetadataBaseDataType_RawData
- [AVMetadataIdentifierQuickTimeMetadataAccessibilityDescription](quicktimemetadataaccessibilitydescription.md) — An identifier that represents the accessibility description for the movie file content.
- [AVMetadataIdentifierQuickTimeMetadataAlbum](quicktimemetadataalbum.md) — An identifier that represents the name of the album or collection in QuickTime.
- [AVMetadataIdentifierQuickTimeMetadataArranger](quicktimemetadataarranger.md) — An identifier that represents the name of the arranger of the movie file content.
- [AVMetadataIdentifierQuickTimeMetadataArtist](quicktimemetadataartist.md) — An identifier that represents the name of the artist of the movie file content.
- [AVMetadataIdentifierQuickTimeMetadataArtwork](quicktimemetadataartwork.md) — An identifier that represents an image relating to the movie file content.
- [AVMetadataIdentifierQuickTimeMetadataAuthor](quicktimemetadataauthor.md) — An identifier that represents the name of the author of the movie file content.
- [AVMetadataIdentifierQuickTimeMetadataAutoLivePhoto](quicktimemetadataautolivephoto.md) — An identifier that represents whether the live photo movie used auto mode.
- [AVMetadataIdentifierQuickTimeMetadataCameraFocalLength35mmEquivalent](quicktimemetadatacamerafocallength35mmequivalent.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating focal length normalized to the 35mm film equivalent value (e.g. “50.00mm”).
- [AVMetadataIdentifierQuickTimeMetadataCameraFrameReadoutTime](quicktimemetadatacameraframereadouttime.md) — An identifier that represents the camera frame readout time in QuickTime.
- [AVMetadataIdentifierQuickTimeMetadataCameraISOSensitivity](quicktimemetadatacameraisosensitivity.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the sensitivity of the camera to light in terms of ISO exposure index (e.g. “800”). See SMPTE RDD 18.
- [AVMetadataIdentifierQuickTimeMetadataCameraIdentifier](quicktimemetadatacameraidentifier.md) — An identifier that represents the camera identifier in QuickTime.
- [AVMetadataIdentifierQuickTimeMetadataCameraLensIrisFNumber](quicktimemetadatacameralensirisfnumber.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating measure of the amount of light transmitted through the lens. It is the focal length divided by the effective lens aperture diameter (e.g. “F2.8” or “2.8”).
- [AVMetadataIdentifierQuickTimeMetadataCameraLensModel](quicktimemetadatacameralensmodel.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the lens model (e.g. “iPhone 16 Pro back camera 6.765mm f/1.78”).
- [AVMetadataIdentifierQuickTimeMetadataCameraShutterSpeedAngle](quicktimemetadatacamerashutterspeedangle.md) — A value of type kCMMetadataBaseDataType_UTF8 indicating the exposure period expressed as an angle in minutes (1/60 degree) (e.g. “21600” or “360.00deg””).
