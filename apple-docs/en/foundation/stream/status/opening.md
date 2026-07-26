---
title: Stream.Status.opening
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/status/opening
source_url: 'https://developer.apple.com/documentation/foundation/stream/status/opening'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/status/opening.json'
content_hash: 'sha256:eac8ae52b579a1fb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Stream](../../stream.md) · [Status](../status.md)

# Stream.Status.opening

<sub>Case</sub>

The stream is in the process of being opened for reading or for writing. For network streams, this status might include the time after the stream was opened, but while network DNS resolution is happening.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case opening
```

## See Also

### Enumeration Cases

- [NSStreamStatusAtEnd](atend.md) — There is no more data to read, or no more data can be written to the stream. When this status is returned, the stream is in a “non-blocking” mode and no data are available.
- [NSStreamStatusClosed](closed.md) — The stream is closed ([- close](<../close().md>) has been called on it).
- [NSStreamStatusError](error.md) — The remote end of the connection can’t be contacted, or the connection has been severed for some other reason.
- [NSStreamStatusNotOpen](notopen.md) — The stream is not open for reading or writing. This status is returned before the underlying call to open a stream but after it’s been created.
- [NSStreamStatusOpen](open.md) — The stream is open, but no reading or writing is occurring.
- [NSStreamStatusReading](reading.md) — Data is being read from the stream. This status would be returned if code on another thread were to call [streamStatus](../streamstatus.md) on the stream while a [- read:maxLength:](<../../inputstream/read(__maxlength_).md>) call ([InputStream](../../inputstream.md)) was in progress.
- [NSStreamStatusWriting](writing.md) — Data is being written to the stream. This status would be returned if code on another thread were to call [streamStatus](../streamstatus.md) on the stream while a [- write:maxLength:](<../../outputstream/write(__maxlength_).md>) call ([OutputStream](../../outputstream.md)) was in progress.
