---
title: isVideoStabilizationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（8.0 起废弃）, iPadOS 7.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/format/isvideostabilizationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideostabilizationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/isvideostabilizationsupported.json'
content_hash: 'sha256:3121f4b11ecc9142'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isVideoStabilizationSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the format supports video stabilization.

> [!warning] Deprecated
> Use isVideoStabilizationModeSupported: instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isVideoStabilizationSupported: Bool { get }
```

## Discussion

If the format supports video stabilization, you can enable it on an [AVCaptureConnection](../../avcaptureconnection.md) instance.
