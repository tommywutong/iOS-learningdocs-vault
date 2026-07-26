---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlpipelinebufferdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlpipelinebufferdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpipelinebufferdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:dec786c63f4fc4cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPipelineBufferDescriptorArray](../mtlpipelinebufferdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets a pipeline buffer descriptor at the specified array index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLPipelineBufferDescriptor *) buffer atIndexedSubscript:(NSUInteger) bufferIndex;
```

## Parameters

- `buffer` — The pipeline buffer descriptor to set in the array.

- `bufferIndex` — The array index in which to set the given pipeline buffer descriptor.

## See Also

### Accessing array elements

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the pipeline buffer descriptor at the specified array index.
