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
doc_path: '/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:02f7974968733817'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitPassSampleBufferAttachmentDescriptorArray](../mtlblitpasssamplebufferattachmentdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Copies the properties of a blit pass sample buffer attachment descriptor instance to the properties of one of the array’s instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLBlitPassSampleBufferAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Parameters

- `attachment` — An [MTLBlitPassSampleBufferAttachmentDescriptor](../mtlblitpasssamplebufferattachmentdescriptor.md) instance that the method assigns its properties values to the properties of the array’s instance at `attachmentIndex`. You can reset the property configuration of the array’s instance at `attachmentIndex` to its default values by passing `nil`.

- `attachmentIndex` — An index into the array’s copies of attachment descriptor instances.

## Discussion

The array has at

## See Also

### Accessing a sample buffer attachment descriptor

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Accesses one of the array’s blit pass sample buffer attachment descriptor instances.
