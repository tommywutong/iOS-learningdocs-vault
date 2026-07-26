---
title: isVideoStabilizationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/isvideostabilizationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideostabilizationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideostabilizationsupported.json'
content_hash: 'sha256:c65f92e736c75ae3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoStabilizationSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether this connection supports video stabilization.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVideoStabilizationSupported: Bool { get }
```

## Discussion

The connection only supports video stabilization for video connection types, but may not be available for all resolutions.

## See Also

### Stabilizing video

- [activeVideoStabilizationMode](activevideostabilizationmode.md) — The connection’s current stabilization mode.
- [preferredVideoStabilizationMode](preferredvideostabilizationmode.md) — The stabilization mode that’s the most appropriate for a video connection.
