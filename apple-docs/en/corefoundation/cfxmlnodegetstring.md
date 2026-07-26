---
title: CFXMLNodeGetString
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlnodegetstring
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnodegetstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnodegetstring.json'
content_hash: 'sha256:d4ea7f91492ceb44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLNodeGetString

<sub>Function</sub>

Returns the data string from a CFXMLNode.

<sub>macOS</sub>

```objc
extern CFStringRefCFXMLNodeGetString(CFXMLNodeRef node);
```

## Parameters

- `node` — The CFXMLNode object to examine.

## Return Value

The data string from `node`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### CFXMLNode Miscellaneous Functions

- [CFXMLNodeCreate](cfxmlnodecreate.md) — Creates a new CFXMLNode. _(deprecated)_
- [CFXMLNodeCreateCopy](cfxmlnodecreatecopy.md) — Creates a copy of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) — Returns the additional information pointer of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetTypeCode](cfxmlnodegettypecode.md) — Returns the XML structure type code for a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetTypeID](cfxmlnodegettypeid.md) — Returns the type identifier code for the CFXMLNode opaque type. _(deprecated)_
- [CFXMLNodeGetVersion](cfxmlnodegetversion.md) — Returns the version number for a CFXMLNode object. _(deprecated)_
