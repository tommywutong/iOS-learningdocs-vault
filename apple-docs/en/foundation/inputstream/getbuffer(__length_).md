---
title: 'getBuffer(_:length:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inputstream/getbuffer(_:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/inputstream/getbuffer(_:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inputstream/getbuffer%28_%3Alength%3A%29.json'
content_hash: 'sha256:3847a7011a57d397'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# getBuffer(_:length:)

<sub>Instance Method</sub>

Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getBuffer(_ buffer: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>, length len: UnsafeMutablePointer<Int>) -> Bool
```

## Parameters

- `buffer` — Upon return, contains a pointer to a read buffer. The buffer is only valid until the next stream operation is performed.

- `len` — Upon return, contains the number of bytes available.

## Return Value

[true](../../swift/true.md) if the buffer is available, otherwise [false](../../swift/false.md).

## Discussion

Subclasses of `NSInputStream` may return [false](../../swift/false.md) if this operation is not appropriate for the stream type.

## See Also

### Using Streams

- [- read:maxLength:](<read(__maxlength_).md>) — Reads up to a given number of bytes into a given buffer.
- [hasBytesAvailable](hasbytesavailable.md) — A Boolean value that indicates whether the receiver has bytes available to read.
