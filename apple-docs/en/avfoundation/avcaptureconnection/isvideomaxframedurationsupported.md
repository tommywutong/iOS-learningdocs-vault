---
title: isVideoMaxFrameDurationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 14.0+（14.0 起废弃）, macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureconnection/isvideomaxframedurationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideomaxframedurationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideomaxframedurationsupported.json'
content_hash: 'sha256:013800019adf053a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoMaxFrameDurationSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the connection supports a maximum frame duration.

> [!warning] Deprecated
> Use AVCaptureDevice's activeFormat.videoSupportedFrameRateRanges instead.

<sub>Mac Catalyst, macOS</sub>

```swift
var isVideoMaxFrameDurationSupported: Bool { get }
```

## Discussion

The property indicates whether the connection honors the [videoMaxFrameDuration](videomaxframeduration.md) property for a video connection.

## See Also

### Configuring a video’s frame rate

- [supportsVideoMinFrameDuration](isvideominframedurationsupported.md) — A Boolean value that indicates whether the connection supports a minimum frame duration. _(deprecated)_
- [videoMinFrameDuration](videominframeduration.md) — The smallest time interval the connection can apply between consecutive video frames. _(deprecated)_
- [videoMaxFrameDuration](videomaxframeduration.md) — The largest time interval the connection can apply between consecutive video frames. _(deprecated)_
