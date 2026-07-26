---
title: preferredResolution
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfiguration/preferredresolution
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration/preferredresolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfiguration/preferredresolution.json'
content_hash: 'sha256:bcadda07f9acf662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfiguration](../avcaptureexternaldisplayconfiguration.md)

# preferredResolution

<sub>Instance Property</sub>

Your preferred external display resolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var preferredResolution: CMVideoDimensions { get set }
```

## Discussion

Use [preferredResolution](preferredresolution.md) to set your desired resolution of the external display. When left at the default value of { 0, 0 },  the native resolution of the external display is used.

## See Also

### Modifying the configuration

- [bypassColorSpaceConversion](bypasscolorspaceconversion.md) — A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.
- [shouldMatchFrameRate](shouldmatchframerate.md) — A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.
