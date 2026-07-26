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
doc_path: '/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:d7b55a6a300392d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassColorAttachmentDescriptorArray](../mtlrenderpasscolorattachmentdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets the descriptor for the specified color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLRenderPassColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Parameters

- `attachment` — A descriptor that contains color attachment information. Specify `nil` to reset the attachment to its default values.

- `attachmentIndex` — An index in the color attachment array.

## Discussion

This method copies the color attachment information from the descriptor into the specified attachment in the array. Because the method copies the information, you can modify and reuse the descriptor without affecting a previously set attachment.

## See Also

### Accessing the description of a color attachment

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the descriptor object for the specified color attachment.
