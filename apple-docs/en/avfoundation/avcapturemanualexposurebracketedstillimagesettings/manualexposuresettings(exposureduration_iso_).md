---
title: 'manualExposureSettings(exposureDuration:iso:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/manualexposuresettings(exposureduration:iso:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/manualexposuresettings(exposureduration:iso:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/manualexposuresettings%28exposureduration%3Aiso%3A%29.json'
content_hash: 'sha256:b6d86a38cdb8371c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureManualExposureBracketedStillImageSettings](../avcapturemanualexposurebracketedstillimagesettings.md)

# manualExposureSettings(exposureDuration:iso:)

<sub>Type Method</sub>

Creates a configuration of still image settings using the specified exposure duration and ISO.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func manualExposureSettings(exposureDuration duration: CMTime, iso ISO: Float) -> Self
```

## Parameters

- `duration` — The exposure duration in seconds. Pass `AVCaptureExposureDurationCurrent` to leave the duration unchanged for this bracketed image.

- `ISO` — The film speed in the ISO format. Pass `AVCaptureISOCurrent` to leave the ISO unchanged for this bracketed image.

## Return Value

An initialized `AVCaptureManualExposureBracketedStillImageSettings` instance.
