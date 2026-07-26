---
title: isHighResolutionCaptureEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（16.0 起废弃）, iPadOS 10.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotooutput/ishighresolutioncaptureenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/ishighresolutioncaptureenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/ishighresolutioncaptureenabled.json'
content_hash: 'sha256:fd07634e30be993d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isHighResolutionCaptureEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether to configure the capture pipeline for high resolution still image capture.

> [!warning] Deprecated
> Use [maxPhotoDimensions](maxphotodimensions.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var isHighResolutionCaptureEnabled: Bool { get set }
```

## Discussion

Some capture formats support output of still images at a resolution higher than the resolution they use for live preview and video capture (see the [Format](../avcapturedevice/format.md) [highResolutionStillImageDimensions](../avcapturedevice/format/highresolutionstillimagedimensions.md) property). Under some conditions, a capture session needs to set up its internal rendering pipeline differently to support high resolution still image capture.

If you intend to take high resolution still images at all, set this property to  before calling the [AVCaptureSession](../avcapturesession.md)  [- startRunning](<../avcapturesession/startrunning().md>) method. Changing this property while the session is running requires a lengthy reconfiguration of the capture render pipeline: Live Photo captures in progress will end immediately, unfulfilled photo requests will abort, and video preview will temporarily freeze.

You must enable this option before initiating a photo capture with the [highResolutionPhotoEnabled](../avcapturephotosettings/ishighresolutionphotoenabled.md) property of your photo settings object set to [true](../../swift/true.md). However, after you’ve enabled this option, you are free to issue photo capture requests with any [highResolutionPhotoEnabled](../avcapturephotosettings/ishighresolutionphotoenabled.md) setting.
