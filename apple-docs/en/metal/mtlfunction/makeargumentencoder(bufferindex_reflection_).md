---
title: 'makeArgumentEncoder(bufferIndex:reflection:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（16.0 起废弃）, iPadOS 11.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.13+（13.0 起废弃）, tvOS 11.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlfunction/makeargumentencoder(bufferindex:reflection:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/makeargumentencoder(bufferindex:reflection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/makeargumentencoder%28bufferindex%3Areflection%3A%29.json'
content_hash: 'sha256:806efa07a0b2e52f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# makeArgumentEncoder(bufferIndex:reflection:)

<sub>Instance Method</sub>

Creates an argument encoder and returns reflection information for an argument buffer that’s one of this function’s arguments

> [!warning] Deprecated
> Use the [- newArgumentEncoderWithBufferBinding:](<../mtldevice/makeargumentencoder(bufferbinding_).md>) method of an [MTLDevice](../mtldevice.md) instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeArgumentEncoder(bufferIndex: Int, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedArgument?>?) -> any MTLArgumentEncoder
```

## Parameters

- `bufferIndex` — The index of an argument buffer in the function’s argument list. This method fails if the specified index doesn’t correspond to an argument buffer.

- `reflection` — A pointer that Metal populates with the function reflection data in the argument buffer at `bufferIndex`.

## Discussion

Resources encoded into an argument buffer by the [MTLArgumentEncoder](../mtlargumentencoder.md) object need to match the structure of the argument buffer located at the function’s specified buffer index.

## See Also

### Creating argument encoders

- [- newArgumentEncoderWithBufferIndex:](<makeargumentencoder(bufferindex_).md>) — Creates an argument encoder for an argument buffer that’s one of this function’s arguments.
