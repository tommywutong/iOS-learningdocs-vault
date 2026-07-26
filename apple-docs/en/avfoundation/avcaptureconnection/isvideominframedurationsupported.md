---
title: isVideoMinFrameDurationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 14.0+（14.0 起废弃）, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureconnection/isvideominframedurationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideominframedurationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideominframedurationsupported.json'
content_hash: 'sha256:97c8ac6732baa329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoMinFrameDurationSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the connection supports a minimum frame duration.

> [!warning] Deprecated
> Use AVCaptureDevice's activeFormat.videoSupportedFrameRateRanges instead.

<sub>Mac Catalyst, macOS</sub>

```swift
var isVideoMinFrameDurationSupported: Bool { get }
```

## Discussion

The property indicates whether the connection honors the [videoMinFrameDuration](videominframeduration.md) property for a video connection.

## See Also

### Configuring a video’s frame rate

- [videoMinFrameDuration](videominframeduration.md) — The smallest time interval the connection can apply between consecutive video frames. _(deprecated)_
- [supportsVideoMaxFrameDuration](isvideomaxframedurationsupported.md) — A Boolean value that indicates whether the connection supports a maximum frame duration. _(deprecated)_
- [videoMaxFrameDuration](videomaxframeduration.md) — The largest time interval the connection can apply between consecutive video frames. _(deprecated)_
