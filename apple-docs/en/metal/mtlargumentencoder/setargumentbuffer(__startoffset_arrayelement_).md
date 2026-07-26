---
title: 'setArgumentBuffer(_:startOffset:arrayElement:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setargumentbuffer(_:startoffset:arrayelement:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setargumentbuffer(_:startoffset:arrayelement:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setargumentbuffer%28_%3Astartoffset%3Aarrayelement%3A%29.json'
content_hash: 'sha256:7d5688f2535e9b2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setArgumentBuffer(_:startOffset:arrayElement:)

<sub>Instance Method</sub>

Specifies an array element within a buffer where the encoder writes argument data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setArgumentBuffer(_ argumentBuffer: (any MTLBuffer)?, startOffset: Int, arrayElement: Int)
```

## Parameters

- `argumentBuffer` — The destination buffer that represents an argument buffer.

- `startOffset` — The starting byte offset of the buffer data.

- `arrayElement` — The desired element of the argument buffer array targeted by encoding.

## See Also

### Creating an argument buffer

- [- setArgumentBuffer:offset:](<setargumentbuffer(__offset_).md>) — Specifies the position in a buffer where the encoder writes argument data.
- [encodedLength](encodedlength.md) — The number of bytes required to store the encoded resources of an argument buffer.
