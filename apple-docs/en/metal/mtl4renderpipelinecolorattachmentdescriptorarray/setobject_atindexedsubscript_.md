---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4renderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderpipelinecolorattachmentdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:6e7c3a7f688bc875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderPipelineColorAttachmentDescriptorArray](../mtl4renderpipelinecolorattachmentdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets an attachment at an index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTL4RenderPipelineColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Parameters

- `attachment` — The descriptor of the attachment to set.

- `attachmentIndex` — The index of the attachment within the array.

## Discussion

This function offers ‘copy’ semantics.

You can safely set the color attachment at any legal index to nil. This has the effect of resetting that attachment descriptor’s state to its default values.
