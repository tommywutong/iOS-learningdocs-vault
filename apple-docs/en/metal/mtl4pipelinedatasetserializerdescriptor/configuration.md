---
title: configuration
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinedatasetserializerdescriptor/configuration
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializerdescriptor/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinedatasetserializerdescriptor/configuration.json'
content_hash: 'sha256:72c8c6d3a231d8d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4PipelineDataSetSerializerDescriptor](../mtl4pipelinedatasetserializerdescriptor.md)

# configuration

<sub>Instance Property</sub>

Specifies the configuration of the serialization process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var configuration: MTL4PipelineDataSetSerializerConfiguration { get set }
```

## Discussion

The configuration of the serialization process determines the mechanisms you use to serialize pipeline data sets.

When this configuration contains `MTL4PipelineDataSetSerializerConfigurationCaptureDescriptors`, use `serializeAsPipelinesScriptWithError:` to serialize pipeline scripts.

If this option contains `MTL4PipelineDataSetSerializerConfigurationCaptureBinaries`, the serializer can additionally serialize to a binary archive by calling `serializeAsArchiveAndFlushToURL:error::`.
