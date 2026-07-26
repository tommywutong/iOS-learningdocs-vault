---
title: isStillImageStabilizationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationsupported.json'
content_hash: 'sha256:176e74979de96623'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# isStillImageStabilizationSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the  still image currently being captured supports still image stabilization.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isStillImageStabilizationSupported: Bool { get }
```

## Discussion

The  [automaticallyEnablesStillImageStabilizationWhenAvailable](automaticallyenablesstillimagestabilizationwhenavailable.md) property can only be set if this property returns [true](../../swift/true.md).

The value may change as the session’s [sessionPreset](../avcapturesession/sessionpreset.md) or the input device’s [activeFormat](../avcapturedevice/activeformat.md) changes.

## See Also

### Getting and setting image stabilization settings

- [stillImageStabilizationActive](isstillimagestabilizationactive.md) — Indicates whether still image stabilization is in use for the current capture. _(deprecated)_
- [automaticallyEnablesStillImageStabilizationWhenAvailable](automaticallyenablesstillimagestabilizationwhenavailable.md) — A Boolean value that indicates whether still image stabilization should be automatically enabled. _(deprecated)_
