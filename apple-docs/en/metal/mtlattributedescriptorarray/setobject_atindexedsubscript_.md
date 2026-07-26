---
title: 'setObject:atIndexedSubscript:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlattributedescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlattributedescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributedescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:731f49221d3250fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAttributeDescriptorArray](../mtlattributedescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets state for the specified attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLAttributeDescriptor *) attributeDesc atIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `attributeDesc` — A descriptor that contains attribute state.

- `index` — A specified index in the array of vertex attribute states.

## See Also

### Accessing attribute state objects

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the state of the specified attribute.
