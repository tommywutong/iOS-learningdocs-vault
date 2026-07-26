---
title: CFXMLNodeCreateCopy
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlnodecreatecopy
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnodecreatecopy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnodecreatecopy.json'
content_hash: 'sha256:76cae2cdc26d5cf3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLNodeCreateCopy

<sub>Function</sub>

Creates a copy of a CFXMLNode object.

<sub>macOS</sub>

```objc
extern CFXMLNodeRefCFXMLNodeCreateCopy(CFAllocatorRef alloc, CFXMLNodeRef origNode);
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `origNode` — The node to copy. Do not pass `NULL`.

## Return Value

A new CFXMLNode object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFXMLNode Miscellaneous Functions

- [CFXMLNodeCreate](cfxmlnodecreate.md) — Creates a new CFXMLNode. _(deprecated)_
- [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) — Returns the additional information pointer of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetString](cfxmlnodegetstring.md) — Returns the data string from a CFXMLNode. _(deprecated)_
- [CFXMLNodeGetTypeCode](cfxmlnodegettypecode.md) — Returns the XML structure type code for a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetTypeID](cfxmlnodegettypeid.md) — Returns the type identifier code for the CFXMLNode opaque type. _(deprecated)_
- [CFXMLNodeGetVersion](cfxmlnodegetversion.md) — Returns the version number for a CFXMLNode object. _(deprecated)_
