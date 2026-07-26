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
doc_path: '/documentation/metal/mtlvertexbufferlayoutdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexbufferlayoutdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:5c2ce4b8ea3d96d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexBufferLayoutDescriptorArray](../mtlvertexbufferlayoutdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets the state of the specified vertex buffer layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLVertexBufferLayoutDescriptor *) bufferDesc atIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `bufferDesc` — A descriptor that contains vertex buffer layout state.

- `index` — An index in the array of vertex buffer layouts.

## Discussion

If this method is called with `nil` for `bufferDesc` for any legal index, the [MTLVertexBufferLayoutDescriptor](../mtlvertexbufferlayoutdescriptor.md) object in the array is set to the default values.

## See Also

### Accessing a specified vertex buffer layout

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the state of the specified vertex buffer layout.
