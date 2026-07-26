---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:d5b732c4757e4a03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTileRenderPipelineColorAttachmentDescriptorArray](../mtltilerenderpipelinecolorattachmentdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets the render pipeline state for a specified color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLTileRenderPipelineColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Parameters

- `attachment` — A descriptor that contains the render pipeline description for a color attachment. Specify `nil` to reset the entry to default values.

- `attachmentIndex` — An index in the color attachment array.

## Discussion

This method copies the pipeline state from the descriptor into the specified attachment in the array. Afterwards, you can modify and reuse the descriptior without affecting a previously set attachment.

## See Also

### Instance methods

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the render pipeline state for the specified color attachment.
