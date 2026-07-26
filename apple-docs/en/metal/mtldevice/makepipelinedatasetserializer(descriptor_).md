---
title: 'makePipelineDataSetSerializer(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makepipelinedatasetserializer(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makepipelinedatasetserializer(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makepipelinedatasetserializer%28descriptor%3A%29.json'
content_hash: 'sha256:fe1eda5be3425765'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makePipelineDataSetSerializer(descriptor:)

<sub>Instance Method</sub>

Creates a new pipeline data set serializer instance from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makePipelineDataSetSerializer(descriptor: MTL4PipelineDataSetSerializerDescriptor) -> any MTL4PipelineDataSetSerializer
```

## Parameters

- `descriptor` — A [MTL4PipelineDataSetSerializerDescriptor](../mtl4pipelinedatasetserializerdescriptor.md) instance that configures the new [MTL4PipelineDataSetSerializer](../mtl4pipelinedatasetserializer.md) instance.

## Return Value

A [MTL4PipelineDataSetSerializer](../mtl4pipelinedatasetserializer.md) instance, or `nil` if the function failed.
