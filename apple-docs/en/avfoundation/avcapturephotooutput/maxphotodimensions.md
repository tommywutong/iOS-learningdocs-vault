---
title: maxPhotoDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/maxphotodimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/maxphotodimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/maxphotodimensions.json'
content_hash: 'sha256:173a8d1b4763c8f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# maxPhotoDimensions

<sub>Instance Property</sub>

The maximum resolution of the requested photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var maxPhotoDimensions: CMVideoDimensions { get set }
```

## Discussion

Set a value for this property to request images up to the specified dimensions. Images that a photo output returns may be smaller than the dimensions, but are never be larger. Once set, you can request images with any valid maximum photo dimensions by setting [maxPhotoDimensions](../avcapturephotosettings/maxphotodimensions.md) on [AVCapturePhotoSettings](../avcapturephotosettings.md) on a per photo basis.

The dimensions you set must match one returned by [supportedMaxPhotoDimensions](../avcapturedevice/format/supportedmaxphotodimensions.md) for the current active format.

> [!tip] Tip
> Changing this property may trigger a lengthy reconfiguration of the capture pipeline, so set this value before calling [- startRunning](<../avcapturesession/startrunning().md>) on the capture session.
