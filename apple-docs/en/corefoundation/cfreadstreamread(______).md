---
title: 'CFReadStreamRead(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamread(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamread(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamread%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:dc8dd7c72684b59d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamRead(_:_:_:)

<sub>Function</sub>

Reads data from a readable stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamRead(_ stream: CFReadStream!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex
```

## Parameters

- `stream` — The stream from which to read.

- `buffer` — The buffer into which to place the data.

- `bufferLength` — The size of `buffer` and the maximum number of bytes to read.

## Return Value

The number of bytes read; `0` if the stream has reached its end; or `-1` if either the stream is not open or an error occurs.

## Discussion

If `stream` is in the process of opening, this function waits until it has completed. This function blocks until at least one byte is available; it does not block until `buffer` is filled. To avoid blocking, call this function only if [CFReadStreamHasBytesAvailable](<cfreadstreamhasbytesavailable(__).md>) returns `TRUE` or after the stream’s client (set with [CFReadStreamSetClient](<cfreadstreamsetclient(________).md>)) is notified of a [kCFStreamEventHasBytesAvailable](cfstreameventtype/hasbytesavailable.md) event.
