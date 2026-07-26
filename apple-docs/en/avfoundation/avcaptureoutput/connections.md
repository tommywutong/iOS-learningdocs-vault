---
title: connections
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureoutput/connections
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/connections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/connections.json'
content_hash: 'sha256:8e6ac4508345aeed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureOutput](../avcaptureoutput.md)

# connections

<sub>Instance Property</sub>

The capture output object’s connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var connections: [AVCaptureConnection] { get }
```

## Discussion

Each connection object in the array describes the mapping between the output and the capture input ports.

## See Also

### Accessing connections

- [- connectionWithMediaType:](<connection(with_).md>) — Returns the first connection with an input port of a specified media type.
- [DataDroppedReason](datadroppedreason.md) — Constants that define reasons for why the system dropped a frame.
