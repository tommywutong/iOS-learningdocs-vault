---
title: 'connection(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureoutput/connection(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/connection(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/connection%28with%3A%29.json'
content_hash: 'sha256:e53a8e9fd7fec85e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureOutput](../avcaptureoutput.md)

# connection(with:)

<sub>Instance Method</sub>

Returns the first connection with an input port of a specified media type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func connection(with mediaType: AVMediaType) -> AVCaptureConnection?
```

## Parameters

- `mediaType` — A media type such as [AVMediaTypeVideo](../avmediatype/video.md) or [AVMediaTypeAudio](../avmediatype/audio.md).

## Return Value

The first capture connection that has the specified media type, or `nil` if no connection for the media type exists.

## See Also

### Accessing connections

- [connections](connections.md) — The capture output object’s connections.
- [DataDroppedReason](datadroppedreason.md) — Constants that define reasons for why the system dropped a frame.
