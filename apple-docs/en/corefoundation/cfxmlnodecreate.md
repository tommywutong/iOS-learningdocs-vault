---
title: CFXMLNodeCreate
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlnodecreate
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnodecreate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnodecreate.json'
content_hash: 'sha256:8d95bd775235e173'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLNodeCreate

<sub>Function</sub>

Creates a new CFXMLNode.

<sub>macOS</sub>

```objc
extern CFXMLNodeRefCFXMLNodeCreate(CFAllocatorRef alloc, CFXMLNodeTypeCode xmlType, CFStringRef dataString, const void *additionalInfoPtr, CFIndex version);
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `xmlType` — Type identifier code for the XML structure you want this node to describe.

- `dataString` — The XML data.

- `additionalInfoPtr` — A pointer to a structure containing additional information about the XML data.

- `version` — The version number of the CFXMLNode object you want to create. Pass one of the pre-defined constants, typically [kCFXMLNodeCurrentVersion](kcfxmlnodecurrentversion.md).

## Return Value

A new CFXMLNode object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFXMLNode Miscellaneous Functions

- [CFXMLNodeCreateCopy](cfxmlnodecreatecopy.md) — Creates a copy of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) — Returns the additional information pointer of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetString](cfxmlnodegetstring.md) — Returns the data string from a CFXMLNode. _(deprecated)_
- [CFXMLNodeGetTypeCode](cfxmlnodegettypecode.md) — Returns the XML structure type code for a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetTypeID](cfxmlnodegettypeid.md) — Returns the type identifier code for the CFXMLNode opaque type. _(deprecated)_
- [CFXMLNodeGetVersion](cfxmlnodegetversion.md) — Returns the version number for a CFXMLNode object. _(deprecated)_
