---
title: videoMaxFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 14.0+（14.0 起废弃）, macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureconnection/videomaxframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videomaxframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/videomaxframeduration.json'
content_hash: 'sha256:71b2187307ee3e88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# videoMaxFrameDuration

<sub>Instance Property</sub>

The largest time interval the connection can apply between consecutive video frames.

> [!warning] Deprecated
> Use AVCaptureDevice's activeVideoMaxFrameDuration instead.

<sub>Mac Catalyst, macOS</sub>

```swift
var videoMaxFrameDuration: CMTime { get set }
```

## Discussion

When [supportsVideoMaxFrameDuration](isvideomaxframedurationsupported.md) is [true](../../swift/true.md), the value of the property configures the upper bound for the amount of time a video connection separates consecutive frames. The value is equivalent to the reciprocal of the minimum frame rate.

You can set an unlimited frame rate with [zero](../../coremedia/cmtime/zero.md) or [invalid](../../coremedia/cmtime/invalid.md) (which is the default).

## See Also

### Configuring a video’s frame rate

- [supportsVideoMinFrameDuration](isvideominframedurationsupported.md) — A Boolean value that indicates whether the connection supports a minimum frame duration. _(deprecated)_
- [videoMinFrameDuration](videominframeduration.md) — The smallest time interval the connection can apply between consecutive video frames. _(deprecated)_
- [supportsVideoMaxFrameDuration](isvideomaxframedurationsupported.md) — A Boolean value that indicates whether the connection supports a maximum frame duration. _(deprecated)_
