---
title: automaticallyEnablesStillImageStabilizationWhenAvailable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable.json'
content_hash: 'sha256:527fab70393bb675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# automaticallyEnablesStillImageStabilizationWhenAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether still image stabilization should be automatically enabled.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var automaticallyEnablesStillImageStabilizationWhenAvailable: Bool { get set }
```

## Discussion

If [stillImageStabilizationSupported](isstillimagestabilizationsupported.md) returns [true](../../swift/true.md), image stabilization may be applied to reduce blur commonly found in low light photos. When stabilization is enabled, still image captures incur additional latency.

The default value is [true](../../swift/true.md) when supported by the input device; otherwise [false](../../swift/false.md).

Setting this property throws an exception ([invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)) if [stillImageStabilizationSupported](isstillimagestabilizationsupported.md) returns [false](../../swift/false.md).

## See Also

### Getting and setting image stabilization settings

- [stillImageStabilizationActive](isstillimagestabilizationactive.md) — Indicates whether still image stabilization is in use for the current capture. _(deprecated)_
- [stillImageStabilizationSupported](isstillimagestabilizationsupported.md) — A Boolean value that indicates whether the  still image currently being captured supports still image stabilization. _(deprecated)_
