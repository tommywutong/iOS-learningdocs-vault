---
title: 'autoExposureSettings(exposureTargetBias:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/autoexposuresettings(exposuretargetbias:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/autoexposuresettings(exposuretargetbias:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/autoexposuresettings%28exposuretargetbias%3A%29.json'
content_hash: 'sha256:224a175b8f804ba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAutoExposureBracketedStillImageSettings](../avcaptureautoexposurebracketedstillimagesettings.md)

# autoExposureSettings(exposureTargetBias:)

<sub>Type Method</sub>

Creates an `AVCaptureAutoExposureBracketedStillImageSettings` using the specified exposure target bias.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func autoExposureSettings(exposureTargetBias: Float) -> Self
```

## Parameters

- `exposureTargetBias` — The exposure target bias. Pass `AVCaptureExposureTargetBiasCurrent` to leave the [exposureTargetBias](exposuretargetbias.md) unchanged for this image.

## Return Value

An initialized `AVCaptureAutoExposureBracketedStillImageSettings` instance.
