---
title: CFXMLNodeGetVersion
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlnodegetversion
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlnodegetversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlnodegetversion.json'
content_hash: 'sha256:2d1f584884d521d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLNodeGetVersion

<sub>Function</sub>

Returns the version number for a CFXMLNode object.

<sub>macOS</sub>

```objc
extern CFIndex CFXMLNodeGetVersion(CFXMLNodeRef node);
```

## Parameters

- `node` — The CFXMLNode object to examine.

## Return Value

The version number of `node`.

## See Also

### CFXMLNode Miscellaneous Functions

- [CFXMLNodeCreate](cfxmlnodecreate.md) — Creates a new CFXMLNode. _(deprecated)_
- [CFXMLNodeCreateCopy](cfxmlnodecreatecopy.md) — Creates a copy of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetInfoPtr](cfxmlnodegetinfoptr.md) — Returns the additional information pointer of a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetString](cfxmlnodegetstring.md) — Returns the data string from a CFXMLNode. _(deprecated)_
- [CFXMLNodeGetTypeCode](cfxmlnodegettypecode.md) — Returns the XML structure type code for a CFXMLNode object. _(deprecated)_
- [CFXMLNodeGetTypeID](cfxmlnodegettypeid.md) — Returns the type identifier code for the CFXMLNode opaque type. _(deprecated)_
