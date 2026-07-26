---
title: MTL4PipelineDataSetSerializer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinedatasetserializer
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinedatasetserializer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinedatasetserializer.json'
content_hash: 'sha256:5392fcf2315ab2fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4PipelineDataSetSerializer

<sub>Protocol</sub>

A fast-addition container for collecting data during pipeline state creation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4PipelineDataSetSerializer : NSObjectProtocol
```

## Overview

Pipeline data serializer instances allow you to create binary archives and serialize pipeline scripts to use with the offline Metal binary generator (`metal-tt`) doc:compiling-binary-archives-from-a-custom-configuration-script.md.

You capture and retain all relevant data for all pipelines a compiler instance creates by providing an instance of this object to its [MTL4CompilerDescriptor](mtl4compilerdescriptor.md).

After capturing data, you can serialize it to a binary archive to persist its contents offline by calling [- serializeAsArchiveAndFlushToURL:error:](<mtl4pipelinedatasetserializer/serializeasarchiveandflush(url_).md>). You can also serialize a pipeline script suitable for the offline binary generator (`metal-tt`) by calling [- serializeAsPipelinesScriptWithError:](<mtl4pipelinedatasetserializer/serializeaspipelinesscript().md>)

> [!note] Note
> The objects [MTL4PipelineDataSetSerializer](mtl4pipelinedatasetserializer.md) contains are opaque and can’t accelerate compilation for compilers they are not attached to. Additionally, your program can’t read data out of data set serializer instances.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- serializeAsArchiveAndFlushToURL:error:](<mtl4pipelinedatasetserializer/serializeasarchiveandflush(url_).md>) — Serializes a pipeline data set to an archive.
- [- serializeAsPipelinesScriptWithError:](<mtl4pipelinedatasetserializer/serializeaspipelinesscript().md>) — Serializes a serializer data set to a pipeline script as raw data.

## See Also

### Pipeline harvesting

- [MTL4PipelineDataSetSerializerConfiguration](mtl4pipelinedatasetserializerconfiguration.md) — Configuration options for pipeline dataset serializer objects.
- [MTL4PipelineDataSetSerializerDescriptor](mtl4pipelinedatasetserializerdescriptor.md) — Groups together properties to create a pipeline data set serializer.
- [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md) — Base type for descriptors you use for building pipeline state objects.
- [MTL4PipelineOptions](mtl4pipelineoptions.md) — Provides options controlling how to compile a pipeline state.
