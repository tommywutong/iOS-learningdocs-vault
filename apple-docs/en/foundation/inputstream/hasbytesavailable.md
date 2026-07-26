---
title: hasBytesAvailable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/inputstream/hasbytesavailable
source_url: 'https://developer.apple.com/documentation/foundation/inputstream/hasbytesavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inputstream/hasbytesavailable.json'
content_hash: 'sha256:54802620302730da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# hasBytesAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver has bytes available to read.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasBytesAvailable: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver has bytes available to read, otherwise [false](../../swift/false.md). May also return [true](../../swift/true.md) if a read must be attempted in order to determine the availability of bytes.

## See Also

### Using Streams

- [- read:maxLength:](<read(__maxlength_).md>) — Reads up to a given number of bytes into a given buffer.
- [- getBuffer:length:](<getbuffer(__length_).md>) — Returns by reference a pointer to a read buffer and, by reference, the number of bytes available, and returns a Boolean value that indicates whether the buffer is available.
