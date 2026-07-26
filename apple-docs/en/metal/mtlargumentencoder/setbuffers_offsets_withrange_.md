---
title: 'setBuffers:offsets:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setbuffers:offsets:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setbuffers:offsets:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setbuffers%3Aoffsets%3Awithrange%3A.json'
content_hash: 'sha256:b57ab30107661573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setBuffers:offsets:withRange:

<sub>Instance Method</sub>

Encodes references to an array of buffers into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

## Parameters

- `buffers` — An array of buffers the method encodes.

- `offsets` — An array of byte offsets for each element in `buffers`.

- `range` — A range of indices within the argument buffer for each element in `buffers`. The values correspond to either the index IDs of declarations in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instances.

## See Also

### Encoding buffers

- [- setBuffer:offset:atIndex:](<setbuffer(__offset_index_).md>) — Encodes a reference to a buffer into the argument buffer.
