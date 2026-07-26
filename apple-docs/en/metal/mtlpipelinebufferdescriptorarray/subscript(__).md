---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlpipelinebufferdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelinebufferdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:eedc17d7a58b992b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPipelineBufferDescriptorArray](../mtlpipelinebufferdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the pipeline buffer descriptor at the specified array index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(bufferIndex: Int) -> MTLPipelineBufferDescriptor! { get set }
```

## Parameters

- `bufferIndex` — The array index of the requested pipeline buffer descriptor.

## Return Value

The descriptor for the buffer bound at this index.
