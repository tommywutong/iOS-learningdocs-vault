---
title: CFXMLTreeCreateXMLData
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmltreecreatexmldata
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmltreecreatexmldata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmltreecreatexmldata.json'
content_hash: 'sha256:457bddcc9e9da522'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLTreeCreateXMLData

<sub>Function</sub>

Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage.

<sub>macOS</sub>

```objc
extern CFDataRefCFXMLTreeCreateXMLData(CFAllocatorRef allocator, CFXMLTreeRef xmlTree);
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `xmlTree` — The CFXMLTree object you wish to convert to an XML document.

## Return Value

The XML data. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function will _not_ regenerate entity references replaced at the parse time (except those required for syntactic correctness). If you need this you must manually walk the tree and re-insert any entity references that should appear in the final output file.

## See Also

### CFXMLTree Miscellaneous Functions

- [CFXMLCreateStringByEscapingEntities](<cfxmlcreatestringbyescapingentities(______).md>) — Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [CFXMLCreateStringByUnescapingEntities](<cfxmlcreatestringbyunescapingentities(______).md>) — Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
- [CFXMLTreeCreateFromData](cfxmltreecreatefromdata.md) — Parses the given XML data and returns the resulting CFXMLTree object. _(deprecated)_
- [CFXMLTreeCreateFromDataWithError](cfxmltreecreatefromdatawitherror.md) — Parses the given XML data and returns the resulting CFXMLTree object and any error information. _(deprecated)_
- [CFXMLTreeCreateWithDataFromURL](cfxmltreecreatewithdatafromurl.md) — Creates a new CFXMLTree object by loading the data to be parsed directly from a data source. _(deprecated)_
- [CFXMLTreeCreateWithNode](cfxmltreecreatewithnode.md) — Creates a childless, parentless CFXMLTree object node for a CFXMLNode object. _(deprecated)_
- [CFXMLTreeGetNode](cfxmltreegetnode.md) — Returns the node of a CFXMLTree object. _(deprecated)_
