---
title: bypassColorSpaceConversion
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfiguration/bypasscolorspaceconversion.json'
content_hash: 'sha256:4fa308c70db956ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfiguration](../avcaptureexternaldisplayconfiguration.md)

# bypassColorSpaceConversion

<sub>Instance Property</sub>

A property indicating whether the color space of the configurator’s preview layer should be preserved on the output display by avoiding color space conversions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var bypassColorSpaceConversion: Bool { get set }
```

## Discussion

Set [bypassColorSpaceConversion](bypasscolorspaceconversion.md) to `true` if you would like the configurator’s  [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md) color space preserved on the output display. This is accomplished by setting the working color space to match the color space of the external display. The color properties of the `CALayer` remain untouched. The default value is `false`.

## See Also

### Modifying the configuration

- [preferredResolution](preferredresolution.md) — Your preferred external display resolution.
- [shouldMatchFrameRate](shouldmatchframerate.md) — A property indicating whether the frame rate of the external display should be configured to match the camera’s frame rate.
