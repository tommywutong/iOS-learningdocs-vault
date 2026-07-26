---
title: 'setFunctions:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlintersectionfunctiontable/setfunctions:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable/setfunctions:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctiontable/setfunctions%3Awithrange%3A.json'
content_hash: 'sha256:82d8043bf26c7336'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md)

# setFunctions:withRange:

<sub>Instance Method</sub>

Sets a range of entries in the table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setFunctions:(id<MTLFunctionHandle> const[]) functions withRange:(NSRange) range;
```

## Parameters

- `functions` — A pointer to an array of function handles.

- `range` — A range of indices to change in the table.

## See Also

### Setting a table entry

- [- setFunction:atIndex:](<setfunction(__index_).md>) — Sets an entry in the table.
