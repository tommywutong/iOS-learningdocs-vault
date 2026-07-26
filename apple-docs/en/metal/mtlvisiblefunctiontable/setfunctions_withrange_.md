---
title: 'setFunctions:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlvisiblefunctiontable/setfunctions:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable/setfunctions:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvisiblefunctiontable/setfunctions%3Awithrange%3A.json'
content_hash: 'sha256:c537e51130a95b0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVisibleFunctionTable](../mtlvisiblefunctiontable.md)

# setFunctions:withRange:

<sub>Instance Method</sub>

Sets a range of table entries to point to an array of callable functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setFunctions:(id<MTLFunctionHandle> const[]) functions withRange:(NSRange) range;
```

## Parameters

- `functions` — An array of function handles for the functions to be called.

- `range` — A range of indices to change in the table.

## See Also

### Setting a table entry

- [- setFunction:atIndex:](<setfunction(__index_).md>) — Sets a table entry to point to a callable function.
