---
title: supportedMaxPhotoDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceformat/supportedmaxphotodimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/supportedmaxphotodimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceformat/supportedmaxphotodimensions.json'
content_hash: 'sha256:258b028e10ffdcab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [Format](../avcapturedevice/format.md)

# supportedMaxPhotoDimensions

<sub>Instance Property</sub>

The maximum photo dimension this format supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSValue *> * supportedMaxPhotoDimensions;
```

## Discussion

The array contains [NSValue](../../foundation/nsvalue.md) objects that hold a [CMVideoDimensions](../../coremedia/cmvideodimensions.md) structure.

## See Also

### Determining photo quality

- [highPhotoQualitySupported](../avcapturedevice/format/ishighphotoqualitysupported.md) — A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
- [highestPhotoQualitySupported](../avcapturedevice/format/ishighestphotoqualitysupported.md) — A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.
