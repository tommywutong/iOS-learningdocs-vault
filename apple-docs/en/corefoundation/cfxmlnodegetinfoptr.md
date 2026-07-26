---
title: CFXMLNodeGetInfoPtr
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlnodegetinfoptr
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnodegetinfoptr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnodegetinfoptr.json'
content_hash: 'sha256:41f6a79af63ba9b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLNodeGetInfoPtr

<sub>Function</sub>

Returns the additional information pointer of a CFXMLNode object.

<sub>macOS</sub>

```objc
extern const void *CFXMLNodeGetInfoPtr(CFXMLNodeRef node);
```

## Parameters

- `node` — The CFXMLNode object to examine.

## Return Value

A pointer to a structure containing additional information. The CFXMLNode version together with the node’s type determines the expected structure. See [CFXMLNodeTypeCode](cfxmlnodetypecode.md) for information about the possible structures returned. If the returned value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### CFXMLNode Miscellaneous Functions

- [CFXMLNodeCreate](cfxmlnodecreate.md) — Creates a new CFXMLNode. _(deprecated)_
- [CFXMLNodeCreateCopy](cfxmlnodecreatecopy.md) — Creates a copy of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetString](cfxmlnodegetstring.md) — Returns the data string from a CFXMLNode. _(deprecated)_
- [CFXMLNodeGetTypeCode](cfxmlnodegettypecode.md) — Returns the XML structure type code for a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetTypeID](cfxmlnodegettypeid.md) — Returns the type identifier code for the CFXMLNode opaque type. _(deprecated)_
- [CFXMLNodeGetVersion](cfxmlnodegetversion.md) — Returns the version number for a CFXMLNode object. _(deprecated)_
