---
title: encodedLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentencoder/encodedlength
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/encodedlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/encodedlength.json'
content_hash: 'sha256:921dcee6205682a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# encodedLength

<sub>Instance Property</sub>

The number of bytes required to store the encoded resources of an argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var encodedLength: Int { get }
```

## Discussion

After creating an [MTLArgumentEncoder](../mtlargumentencoder.md) instance, use this value to create the [MTLBuffer](../mtlbuffer.md) instance that represents an argument buffer.

```swift
id <MTLArgumentEncoder> encoder = [_function newArgumentEncoderWithBufferIndex:0];
id <MTLBuffer> buffer = [_device newBufferWithLength:encoder.encodedLength options:_options];
[encoder setArgumentBuffer:buffer offset:0];
```

## See Also

### Creating an argument buffer

- [- setArgumentBuffer:offset:](<setargumentbuffer(__offset_).md>) — Specifies the position in a buffer where the encoder writes argument data.
- [- setArgumentBuffer:startOffset:arrayElement:](<setargumentbuffer(__startoffset_arrayelement_).md>) — Specifies an array element within a buffer where the encoder writes argument data.
