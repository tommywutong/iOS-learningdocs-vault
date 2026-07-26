---
title: 'makeArgumentEncoderForBuffer(atIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/makeargumentencoderforbuffer(atindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/makeargumentencoderforbuffer(atindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/makeargumentencoderforbuffer%28atindex%3A%29.json'
content_hash: 'sha256:9f8fd078268cd8cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# makeArgumentEncoderForBuffer(atIndex:)

<sub>Instance Method</sub>

Creates a new argument encoder for a nested argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeArgumentEncoderForBuffer(atIndex index: Int) -> (any MTLArgumentEncoder)?
```

## Parameters

- `index` — The index of a nested argument-buffer within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## Return Value

An argument encoder targeting the nested argument buffer.

## Discussion

If an argument buffer contains nested argument buffers in its structure, then each nested argument buffer needs to use its own [MTLArgumentEncoder](../mtlargumentencoder.md) object to encode its individual resources.
