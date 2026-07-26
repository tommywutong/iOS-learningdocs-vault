---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:281efd9bb3c9c952'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePassSampleBufferAttachmentDescriptorArray](../mtlcomputepasssamplebufferattachmentdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets the descriptor object for the specified sample buffer attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLComputePassSampleBufferAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Parameters

- `attachment` — A sample buffer attachment descriptor. When set to `nil`, removes any existing buffer attachment descriptor at `attachmentIndex`.

- `attachmentIndex` — The attachment in the array to replace.

## Discussion

The method copies the `attachment` parameter’s contents into the attachment at the specified index.

## See Also

### Accessing a sample buffer attachment

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the descriptor object for the specified sample buffer attachment.
