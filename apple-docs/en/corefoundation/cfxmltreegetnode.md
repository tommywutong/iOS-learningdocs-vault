---
title: CFXMLTreeGetNode
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmltreegetnode
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmltreegetnode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmltreegetnode.json'
content_hash: 'sha256:e36691781c5de625'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLTreeGetNode

<sub>Function</sub>

Returns the node of a CFXMLTree object.

<sub>macOS</sub>

```objc
extern CFXMLNodeRefCFXMLTreeGetNode(CFXMLTreeRef xmlTree);
```

## Parameters

- `xmlTree` — The CFXMLTree object whose node you wish to obtain.

## Return Value

The node of `xmlTree`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### CFXMLTree Miscellaneous Functions

- [CFXMLCreateStringByEscapingEntities](<cfxmlcreatestringbyescapingentities(______).md>) — Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [CFXMLCreateStringByUnescapingEntities](<cfxmlcreatestringbyunescapingentities(______).md>) — Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
- [CFXMLTreeCreateFromData](cfxmltreecreatefromdata.md) — Parses the given XML data and returns the resulting CFXMLTree object. _(deprecated)_
- [CFXMLTreeCreateFromDataWithError](cfxmltreecreatefromdatawitherror.md) — Parses the given XML data and returns the resulting CFXMLTree object and any error information. _(deprecated)_
- [CFXMLTreeCreateWithDataFromURL](cfxmltreecreatewithdatafromurl.md) — Creates a new CFXMLTree object by loading the data to be parsed directly from a data source. _(deprecated)_
- [CFXMLTreeCreateWithNode](cfxmltreecreatewithnode.md) — Creates a childless, parentless CFXMLTree object node for a CFXMLNode object. _(deprecated)_
- [CFXMLTreeCreateXMLData](cfxmltreecreatexmldata.md) — Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage. _(deprecated)_
