---
title: 'setVertexAmplificationCount:viewMappings:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setvertexamplificationcount:viewmappings:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setvertexamplificationcount:viewmappings:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setvertexamplificationcount%3Aviewmappings%3A.json'
content_hash: 'sha256:02bdda80a1f40a29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setVertexAmplificationCount:viewMappings:

<sub>Instance Method</sub>

Sets the vertex amplification count and its view mapping for each amplification ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setVertexAmplificationCount:(NSUInteger) count viewMappings:(const MTLVertexAmplificationViewMapping *) viewMappings;
```

## Parameters

- `count` — The number of outputs to create. The maximum value is `2`.

- `viewMappings` — Array of [MTLVertexAmplificationViewMapping](../mtlvertexamplificationviewmapping.md) instances. Each instance provides per-output offsets to a specific render target and viewport.

## Discussion

Each view mapping element describes how to route the corresponding amplification ID to a specific viewport and render target array index by using offsets from the base array index provided by the `[[ render_target_array_index ]]` and/or `[[ viewport_array_index ]]` output attributes in the vertex shader. This allows Metal to route each amplified vertex to a different `[[ render_target_array_index ]]` and `[[ viewport_array_index ]]`, even though you can’t directly amplify these attributes.
