---
title: CFXMLTreeCreateFromData
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmltreecreatefromdata
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmltreecreatefromdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmltreecreatefromdata.json'
content_hash: 'sha256:5995b22117bdd2c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLTreeCreateFromData

<sub>Function</sub>

Parses the given XML data and returns the resulting CFXMLTree object.

<sub>macOS</sub>

```objc
extern CFXMLTreeRefCFXMLTreeCreateFromData(CFAllocatorRef allocator, CFDataRef xmlData, CFURLRef dataSource, CFOptionFlags parseOptions, CFIndex versionOfNodes);
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `xmlData` — The XML data you wish to parse.

- `dataSource` — The URL from which the XML data was obtained. The URL is used to resolve any relative references found in `xmlData`. Pass `NULL` if a valid URL is unavailable.

- `parseOptions` — Flags which control how the XML data will be parsed. See [CFXMLParserOptions](cfxmlparseroptions.md) for the list of available options.

- `versionOfNodes` — Determines which version of CFXMLNode objects are produced by the parser.

## Return Value

A new CFXMLTree object containing the data from the specified XML document. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function represents the high-level interface to the XML parser. This single function creates a parser for the specified XML data using the specified options. The parser creates and returns a CFXMLTree object that you can examine and modify with the CFTree functions or obtain the node using the [CFXMLTreeGetNode](cfxmltreegetnode.md) function and examine its attributes using CFXMLNode functions.

## See Also

### CFXMLTree Miscellaneous Functions

- [CFXMLCreateStringByEscapingEntities](<cfxmlcreatestringbyescapingentities(______).md>) — Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [CFXMLCreateStringByUnescapingEntities](<cfxmlcreatestringbyunescapingentities(______).md>) — Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
- [CFXMLTreeCreateFromDataWithError](cfxmltreecreatefromdatawitherror.md) — Parses the given XML data and returns the resulting CFXMLTree object and any error information. _(deprecated)_
- [CFXMLTreeCreateWithDataFromURL](cfxmltreecreatewithdatafromurl.md) — Creates a new CFXMLTree object by loading the data to be parsed directly from a data source. _(deprecated)_
- [CFXMLTreeCreateWithNode](cfxmltreecreatewithnode.md) — Creates a childless, parentless CFXMLTree object node for a CFXMLNode object. _(deprecated)_
- [CFXMLTreeCreateXMLData](cfxmltreecreatexmldata.md) — Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage. _(deprecated)_
- [CFXMLTreeGetNode](cfxmltreegetnode.md) — Returns the node of a CFXMLTree object. _(deprecated)_
