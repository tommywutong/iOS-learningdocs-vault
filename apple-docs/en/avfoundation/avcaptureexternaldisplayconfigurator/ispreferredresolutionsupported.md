---
title: isPreferredResolutionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfigurator/ispreferredresolutionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/ispreferredresolutionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfigurator/ispreferredresolutionsupported.json'
content_hash: 'sha256:91bb1c0b8053d048'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md)

# isPreferredResolutionSupported

<sub>Type Property</sub>

Whether the external display supports configuration to your preferred resolution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var isPreferredResolutionSupported: Bool { get }
```

## Discussion

If `true`, you may instantiate a configurator with a configuration specifying [preferredResolution](../avcaptureexternaldisplayconfiguration/preferredresolution.md) set to `true`.

## See Also

### Determining configuration support

- [shouldMatchFrameRateSupported](ismatchingframeratesupported.md) — Whether the external display supports matching frame rate to a capture device.
- [supportsBypassingColorSpaceConversion](isbypassingcolorspaceconversionsupported.md) — Whether the external display supports bypassing color space conversion.
