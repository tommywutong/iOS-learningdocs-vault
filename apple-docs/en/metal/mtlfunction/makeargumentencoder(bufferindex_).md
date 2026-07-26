---
title: 'makeArgumentEncoder(bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunction/makeargumentencoder(bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/makeargumentencoder(bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/makeargumentencoder%28bufferindex%3A%29.json'
content_hash: 'sha256:797a0759338fdb5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# makeArgumentEncoder(bufferIndex:)

<sub>Instance Method</sub>

Creates an argument encoder for an argument buffer that’s one of this function’s arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeArgumentEncoder(bufferIndex: Int) -> any MTLArgumentEncoder
```

## Parameters

- `bufferIndex` — The index of an argument buffer in the function’s argument list. This method fails if the specified index doesn’t correspond to an argument buffer.

## Discussion

Resources encoded into an argument buffer by the [MTLArgumentEncoder](../mtlargumentencoder.md) object need to match the structure of the argument buffer located at the specified buffer index. If you want to interpret a regular structure as an argument buffer, at least one of the members of the structure needs to have an `[[id(n)]]` attribute.

## See Also

### Creating argument encoders

- [- newArgumentEncoderWithBufferIndex:reflection:](<makeargumentencoder(bufferindex_reflection_).md>) — Creates an argument encoder and returns reflection information for an argument buffer that’s one of this function’s arguments _(deprecated)_
