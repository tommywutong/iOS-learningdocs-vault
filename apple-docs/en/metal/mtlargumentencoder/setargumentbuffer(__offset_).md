---
title: 'setArgumentBuffer(_:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setargumentbuffer(_:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setargumentbuffer(_:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setargumentbuffer%28_%3Aoffset%3A%29.json'
content_hash: 'sha256:898fd69f49cbfd33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setArgumentBuffer(_:offset:)

<sub>Instance Method</sub>

Specifies the position in a buffer where the encoder writes argument data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setArgumentBuffer(_ argumentBuffer: (any MTLBuffer)?, offset: Int)
```

## Parameters

- `argumentBuffer` — The destination buffer that represents an argument buffer.

- `offset` — The byte offset of the buffer.

## See Also

### Creating an argument buffer

- [- setArgumentBuffer:startOffset:arrayElement:](<setargumentbuffer(__startoffset_arrayelement_).md>) — Specifies an array element within a buffer where the encoder writes argument data.
- [encodedLength](encodedlength.md) — The number of bytes required to store the encoded resources of an argument buffer.
