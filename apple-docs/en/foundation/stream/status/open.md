---
title: Stream.Status.open
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/status/open
source_url: 'https://developer.apple.com/documentation/foundation/stream/status/open'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/status/open.json'
content_hash: 'sha256:9584788e1984e40e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Stream](../../stream.md) · [Status](../status.md)

# Stream.Status.open

<sub>Case</sub>

The stream is open, but no reading or writing is occurring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case open
```

## See Also

### Enumeration Cases

- [NSStreamStatusAtEnd](atend.md) — There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.
- [NSStreamStatusClosed](closed.md) — The stream is closed ([- close](<../close().md>) has been called on it).
- [NSStreamStatusError](error.md) — The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.
- [NSStreamStatusNotOpen](notopen.md) — The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [NSStreamStatusOpening](opening.md) — The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.
- [NSStreamStatusReading](reading.md) — Data is being read from the stream. This status would be returned if code on another thread were to call [streamStatus](../streamstatus.md) on the stream while a [- read:maxLength:](<../../inputstream/read(__maxlength_).md>) call ([InputStream](../../inputstream.md)) was in progress.
- [NSStreamStatusWriting](writing.md) — Data is being written to the stream. This status would be returned if code on another thread were to call [streamStatus](../streamstatus.md) on the stream while a [- write:maxLength:](<../../outputstream/write(__maxlength_).md>) call ([OutputStream](../../outputstream.md)) was in progress.
