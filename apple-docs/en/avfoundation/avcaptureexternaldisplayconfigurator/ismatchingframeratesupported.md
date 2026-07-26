---
title: isMatchingFrameRateSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureexternaldisplayconfigurator/ismatchingframeratesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/ismatchingframeratesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureexternaldisplayconfigurator/ismatchingframeratesupported.json'
content_hash: 'sha256:9907fcd49e3e7cb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureExternalDisplayConfigurator](../avcaptureexternaldisplayconfigurator.md)

# isMatchingFrameRateSupported

<sub>Type Property</sub>

Whether the external display supports matching frame rate to a capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var isMatchingFrameRateSupported: Bool { get }
```

## Discussion

If `true`, you may instantiate a configurator with a configuration specifying [shouldMatchFrameRate](../avcaptureexternaldisplayconfiguration/shouldmatchframerate.md) set to `true`.

## See Also

### Determining configuration support

- [supportsPreferredResolution](ispreferredresolutionsupported.md) — Whether the external display supports configuration to your preferred resolution.
- [supportsBypassingColorSpaceConversion](isbypassingcolorspaceconversionsupported.md) — Whether the external display supports bypassing color space conversion.
