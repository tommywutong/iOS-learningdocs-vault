---
title: nominalFocalLengthIn35mmFilm
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/nominalfocallengthin35mmfilm
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/nominalfocallengthin35mmfilm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/nominalfocallengthin35mmfilm.json'
content_hash: 'sha256:b9ae122921da4806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# nominalFocalLengthIn35mmFilm

<sub>Instance Property</sub>

The nominal 35mm equivalent focal length of the capture device’s lens.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var nominalFocalLengthIn35mmFilm: Float { get }
```

## Discussion

This value represents a nominal measurement of the device’s field of view, expressed as a 35mm equivalent focal length, measured diagonally. The value is similar to the `FocalLengthIn35mmFormat` EXIF entry (see [kCGImagePropertyExifFocalLenIn35mmFilm](../../imageio/kcgimagepropertyexiffocallenin35mmfilm.md)) for a photo captured using the device’s format where [highestPhotoQualitySupported](format/ishighestphotoqualitysupported.md) is `true` or when you’ve configured the session with the [AVCaptureSessionPresetPhoto](../avcapturesession/preset/photo.md) preset.

This property value is `0` for virtual devices and external cameras.
