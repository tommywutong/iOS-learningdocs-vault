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
doc_path: '/documentation/metal/mtlvertexattributedescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexattributedescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:eaa16d624ecb9cba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexAttributeDescriptorArray](../mtlvertexattributedescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets state for the specified vertex attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLVertexAttributeDescriptor *) attributeDesc atIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `attributeDesc` — A descriptor that contains vertex attribute state.

- `index` — A specified index in the array of vertex attribute states.

## Discussion

If this method is called with `nil` for `attributeDesc` for any legal `index`, its vertex attribute state is set to the default values.

## See Also

### Accessing a specified vertex attribute

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the state of the specified vertex attribute.
