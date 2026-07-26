---
title: shouldMatchFrameRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfiguration/shouldmatchframerate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration/shouldmatchframerate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfiguration/shouldmatchframerate.json'
content_hash: 'sha256:9a91b5c43d1c36cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfiguration](../avcaptureexternaldisplayconfiguration.md)

# shouldMatchFrameRate

<sub>Instance Property</sub>

A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var shouldMatchFrameRate: Bool { get set }
```

## Discussion

If you want to configure your [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md) to match its source [activeVideoMinFrameDuration](../avcapturedevice/activevideominframeduration.md), set [shouldMatchFrameRate](shouldmatchframerate.md) to `true`. The default value is `false`.

## See Also

### Modifying the configuration

- [bypassColorSpaceConversion](bypasscolorspaceconversion.md) — A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.
- [preferredResolution](preferredresolution.md) — Your preferred external display resolution.
