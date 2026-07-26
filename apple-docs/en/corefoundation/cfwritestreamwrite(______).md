---
title: 'CFWriteStreamWrite(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamwrite(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamwrite(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamwrite%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b3a27098f057a990'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamWrite(_:_:_:)

<sub>Function</sub>

Writes data to a writable stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamWrite(_ stream: CFWriteStream!, _ buffer: UnsafePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex
```

## Parameters

- `stream` — The stream to which to write.

- `buffer` — The buffer holding the data to write.

- `bufferLength` — The number of bytes from `buffer` to write.

## Return Value

The number of bytes successfully written, `0` if the stream has been filled to capacity (for fixed-length streams), or `-1` if either the stream is not open or an error occurs.

## Discussion

If `stream` is in the process of opening, this function waits until it has completed. If the stream is not full, this call blocks until at least one byte is written; it does not block until all the bytes in `buffer` is written. To avoid blocking, call this function only if [CFWriteStreamCanAcceptBytes](<cfwritestreamcanacceptbytes(__).md>) returns `true` or after the stream’s client (set with [CFWriteStreamSetClient](<cfwritestreamsetclient(________).md>)) is notified of a [kCFStreamEventCanAcceptBytes](cfstreameventtype/canacceptbytes.md) event.
