---
title: canAcceptBytes
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreameventtype/canacceptbytes
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreameventtype/canacceptbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreameventtype/canacceptbytes.json'
content_hash: 'sha256:dc0e3e4b27b99fca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStreamEventType](../cfstreameventtype.md)

# canAcceptBytes

<sub>Type Property</sub>

The stream can accept bytes for writing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var canAcceptBytes: CFStreamEventType { get }
```

## See Also

### Constants

- [kCFStreamEventOpenCompleted](opencompleted.md) — The open has completed successfully.
- [kCFStreamEventHasBytesAvailable](hasbytesavailable.md) — The stream has bytes to be read.
- [kCFStreamEventErrorOccurred](erroroccurred.md) — An error has occurred on the stream.
- [kCFStreamEventEndEncountered](endencountered.md) — The end of the stream has been reached.
