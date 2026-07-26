---
title: 'read(_:maxLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inputstream/read(_:maxlength:)'
source_url: 'https://developer.apple.com/documentation/foundation/inputstream/read(_:maxlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inputstream/read%28_%3Amaxlength%3A%29.json'
content_hash: 'sha256:c224ea4a3968bb6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# read(_:maxLength:)

<sub>Instance Method</sub>

Reads up to a given number of bytes into a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func read(_ buffer: UnsafeMutablePointer<UInt8>, maxLength len: Int) -> Int
```

## Parameters

- `buffer` — A data buffer. The buffer must be large enough to contain the number of bytes specified by `len`.

- `len` — The maximum number of bytes to read.

## Return Value

A number indicating the outcome of the operation:

## Discussion

- A positive number indicates the number of bytes read.
- `0` indicates that the end of the buffer was reached.
- `-1` means that the operation failed; more information about the error can be obtained with [streamError](../stream/streamerror.md).

## See Also

### Using Streams

- [- getBuffer:length:](<getbuffer(__length_).md>) — Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.
- [hasBytesAvailable](hasbytesavailable.md) — A Boolean value that indicates whether the receiver has bytes available to read.
