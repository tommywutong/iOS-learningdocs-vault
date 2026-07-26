---
title: captureBinaries
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinedatasetserializerconfiguration/capturebinaries
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializerconfiguration/capturebinaries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinedatasetserializerconfiguration/capturebinaries.json'
content_hash: 'sha256:f51a438387048d7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4PipelineDataSetSerializerConfiguration](../mtl4pipelinedatasetserializerconfiguration.md)

# captureBinaries

<sub>Type Property</sub>

Enables serializing pipeline binary functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var captureBinaries: MTL4PipelineDataSetSerializerConfiguration { get }
```

## Discussion

Set this mask to use `MTL4PipelineDataSetSerializer.serializeAsArchiveAndFlush(toURL:error:)`.
