---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:4119bff2d2887a43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceStatePassSampleBufferAttachmentDescriptorArray](../mtlresourcestatepasssamplebufferattachmentdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets the descriptor object for the specified sample buffer attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLResourceStatePassSampleBufferAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Parameters

- `attachment` — A sample buffer attachment descriptor. If you specify `nil`, the attachment descriptor resets its configuration to default values.

- `attachmentIndex` — The item in the array to replace.

## Discussion

The method copies the `attachment` parameter’s contents into the attachment at the specified index..

## See Also

### Accessing a sample buffer attachment

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the descriptor object for the specified sample buffer attachment.
