---
title: 'setBuffers(_:offsets:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setbuffers(_:offsets:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setbuffers(_:offsets:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setbuffers%28_%3Aoffsets%3Arange%3A%29.json'
content_hash: 'sha256:8cc40d976c2aa092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setBuffers(_:offsets:range:)

<sub>Instance Method</sub>

Encodes references to an array of buffers into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

## Parameters

- `buffers` — An array of buffers the method encodes.

- `offsets` — An array of byte offsets for each element in `buffers`.

- `range` — A range of indices within the argument buffer for each element in `buffers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding buffers

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Encodes a reference to a buffer into the argument buffer.
