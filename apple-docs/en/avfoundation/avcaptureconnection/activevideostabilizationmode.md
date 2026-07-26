---
title: activeVideoStabilizationMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/activevideostabilizationmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/activevideostabilizationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/activevideostabilizationmode.json'
content_hash: 'sha256:cec5dd028ccda6ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# activeVideoStabilizationMode

<sub>Instance Property</sub>

The connection’s current stabilization mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var activeVideoStabilizationMode: AVCaptureVideoStabilizationMode { get }
```

## Discussion

The property only applies to a video connection, and it explicitly indicates whether it’s using stabilization, which means the value is never [AVCaptureVideoStabilizationModeAuto](../avcapturevideostabilizationmode/auto.md).

> [!note] Note
> Devices with a video stabilization feature may only support a subset of available source formats.

You can monitor this property to detect when the connection applies video stabilization to its video data with key-value observation. See [NSKeyValueObserving](../../objectivec/nskeyvalueobserving.md) and [Using Key-Value Observing in Swift](../../swift/using-key-value-observing-in-swift.md) for more information.

## See Also

### Stabilizing video

- [supportsVideoStabilization](isvideostabilizationsupported.md) — A Boolean value that indicates whether this connection supports video stabilization.
- [preferredVideoStabilizationMode](preferredvideostabilizationmode.md) — The stabilization mode that’s the most appropriate for a video connection.
