---
title: hasSpaceAvailable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/event/hasspaceavailable
source_url: 'https://developer.apple.com/documentation/foundation/stream/event/hasspaceavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/event/hasspaceavailable.json'
content_hash: 'sha256:634af32e01bfeedc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Stream](../../stream.md) · [Event](../event.md)

# hasSpaceAvailable

<sub>Type Property</sub>

The stream can accept bytes for writing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hasSpaceAvailable: Stream.Event { get }
```

## See Also

### Constants

- [NSStreamEventOpenCompleted](opencompleted.md) — The open has completed successfully.
- [NSStreamEventHasBytesAvailable](hasbytesavailable.md) — The stream has bytes to be read.
- [NSStreamEventErrorOccurred](erroroccurred.md) — An error has occurred on the stream.
- [NSStreamEventEndEncountered](endencountered.md) — The end of the stream has been reached.
