---
title: 'write(_:maxLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/outputstream/write(_:maxlength:)'
source_url: 'https://developer.apple.com/documentation/foundation/outputstream/write(_:maxlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream/write%28_%3Amaxlength%3A%29.json'
content_hash: 'sha256:88f9ec23a619327d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# write(_:maxLength:)

<sub>Instance Method</sub>

Writes the contents of a provided data buffer to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(_ buffer: UnsafePointer<UInt8>, maxLength len: Int) -> Int
```

## Parameters

- `buffer` — The data to write.

- `len` — The length of the data buffer, in bytes. > [!important] Important > The behavior of this method is undefined if you pass a negative or zero number.

## Return Value

A number indicating the outcome of the operation:

- A positive number indicates the number of bytes written.
- `0` indicates that a fixed-length stream and has reached its capacity.
- `-1` means that the operation failed; more information about the error can be obtained with [streamError](../stream/streamerror.md).

## See Also

### Using Streams

- [hasSpaceAvailable](hasspaceavailable.md) — A boolean value that indicates whether the receiver can be written to.
