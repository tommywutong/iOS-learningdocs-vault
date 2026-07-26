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
doc_path: '/documentation/metal/mtlbufferlayoutdescriptorarray/setobject:atindexedsubscript:'
source_url: 'https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray/setobject:atindexedsubscript:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbufferlayoutdescriptorarray/setobject%3Aatindexedsubscript%3A.json'
content_hash: 'sha256:bddb6b63e9be0e74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBufferLayoutDescriptorArray](../mtlbufferlayoutdescriptorarray.md)

# setObject:atIndexedSubscript:

<sub>Instance Method</sub>

Sets the state of the specified buffer layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setObject:(MTLBufferLayoutDescriptor *) bufferDesc atIndexedSubscript:(NSUInteger) index;
```

## Parameters

- `bufferDesc` — A descriptor that contains buffer layout state.

- `index` — An index in the array of buffer layouts.

## See Also

### Array accessors

- [- objectAtIndexedSubscript:](<subscript(__).md>) — Returns the state of the specified buffer layout.
