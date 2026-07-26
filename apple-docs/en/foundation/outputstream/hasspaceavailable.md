---
title: hasSpaceAvailable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/outputstream/hasspaceavailable
source_url: 'https://developer.apple.com/documentation/foundation/outputstream/hasspaceavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream/hasspaceavailable.json'
content_hash: 'sha256:a5238a5a02a0fe92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# hasSpaceAvailable

<sub>Instance Property</sub>

A boolean value that indicates whether the receiver can be written to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasSpaceAvailable: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver can be written to or if a write must be attempted in order to determine if space is available, [false](../../swift/false.md) otherwise.

## See Also

### Using Streams

- [- write:maxLength:](<write(__maxlength_).md>) — Writes the contents of a provided data buffer to the receiver.
