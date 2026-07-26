---
title: StreamDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/streamdelegate
source_url: 'https://developer.apple.com/documentation/foundation/streamdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/streamdelegate.json'
content_hash: 'sha256:46a0df23d621827f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# StreamDelegate

<sub>Protocol</sub>

An interface that delegates of a stream instance use to handle events on the stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol StreamDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Using Streams

- [- stream:handleEvent:](<streamdelegate/stream(__handle_).md>) — The delegate receives this message when a given event has occurred on a given stream.

## See Also

### Streams

- [Stream](stream.md) — An abstract class representing a stream.
- [InputStream](inputstream.md) — A stream that provides read-only stream functionality.
- [OutputStream](outputstream.md) — A stream that provides write-only stream functionality.
