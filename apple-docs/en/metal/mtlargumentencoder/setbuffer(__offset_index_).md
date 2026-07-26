---
title: 'setBuffer(_:offset:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setbuffer(_:offset:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setbuffer(_:offset:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setbuffer%28_%3Aoffset%3Aindex%3A%29.json'
content_hash: 'sha256:ccff4507e747dbe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setBuffer(_:offset:index:)

<sub>Instance Method</sub>

Encodes a reference to a buffer into the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Parameters

- `buffer` — A buffer the method encodes.

- `offset` — A byte offset for `buffer`.

- `index` — The index of a buffer within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding buffers

- [setBuffers(_:offsets:range:)](<setbuffers(__offsets_range_).md>) — Encodes references to an array of buffers into the argument buffer.
