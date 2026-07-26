---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:0358cb9d406f35d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineColorAttachmentDescriptorArray](../mtlrenderpipelinecolorattachmentdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets the render pipeline state for a specified color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLRenderPipelineColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Parameters

- `attachment` — A descriptor that contains the render pipeline description for a color attachment.

- `attachmentIndex` — An index in the color attachment array.

## Discussion

This method copies the pipeline state from the descriptor into the specified attachment in the array. The descriptor passed into this method can be modified and reused without affecting a previously set attachment.

If this method is called with `nil` for `attachment` for any legal index, its attachment descriptor state is set to the default values.

## See Also

### Accessing render pipeline state for a color attachment

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the render pipeline state for the specified color attachment.
