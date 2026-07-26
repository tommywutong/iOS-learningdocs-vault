---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4pipelinedescriptor/label
source_url: 'https://developer.apple.com/documentation/metal/mtl4pipelinedescriptor/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4pipelinedescriptor/label.json'
content_hash: 'sha256:45ba28e7f0825505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4PipelineDescriptor](../mtl4pipelinedescriptor.md)

# label

<sub>Instance Property</sub>

Assigns an optional string that uniquely identifies a pipeline descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

After you provide this label, you can use it to look up a pipeline state object by name in a binary archive.
