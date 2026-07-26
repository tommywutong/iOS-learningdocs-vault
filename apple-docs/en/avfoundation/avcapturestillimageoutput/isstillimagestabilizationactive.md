---
title: isStillImageStabilizationActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/isstillimagestabilizationactive.json'
content_hash: 'sha256:b24415597f5eb6c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# isStillImageStabilizationActive

<sub>Instance Property</sub>

Indicates whether still image stabilization is in use for the current capture.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isStillImageStabilizationActive: Bool { get }
```

## Discussion

The property returns [true](../../swift/true.md) if video stabilization is currently in use; otherwise [false](../../swift/false.md).

This property supports key-value observing.

## See Also

### Getting and setting image stabilization settings

- [automaticallyEnablesStillImageStabilizationWhenAvailable](automaticallyenablesstillimagestabilizationwhenavailable.md) — A Boolean value that indicates whether still image stabilization should be automatically enabled. _(deprecated)_
- [stillImageStabilizationSupported](isstillimagestabilizationsupported.md) — A Boolean value that indicates whether the  still image currently being captured supports still image stabilization. _(deprecated)_
