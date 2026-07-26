---
title: CFXMLTreeCreateWithDataFromURL
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmltreecreatewithdatafromurl
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmltreecreatewithdatafromurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmltreecreatewithdatafromurl.json'
content_hash: 'sha256:6da6e21fa068ccd9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLTreeCreateWithDataFromURL

<sub>Function</sub>

Creates a new CFXMLTree object by loading the data to be parsed directly from a data source.

<sub>macOS</sub>

```objc
extern CFXMLTreeRefCFXMLTreeCreateWithDataFromURL(CFAllocatorRef allocator, CFURLRef dataSource, CFOptionFlags parseOptions, CFIndex versionOfNodes);
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `dataSource` — The URL from which the XML data is obtained. The URL is used to resolve any relative references found in XML Data. Pass `NULL` if a valid URL is unavailable.

- `parseOptions` — Flags which control how the XML data will be parsed. See [CFXMLParserOptions](cfxmlparseroptions.md) for the list of available options.

- `versionOfNodes` — Determines which version of CFXMLNode objects are produced by the parser.

## Return Value

A new CFXMLTree object containing the data from the specified XML data source. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFXMLTree Miscellaneous Functions

- [CFXMLCreateStringByEscapingEntities](<cfxmlcreatestringbyescapingentities(______).md>) — Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [CFXMLCreateStringByUnescapingEntities](<cfxmlcreatestringbyunescapingentities(______).md>) — Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
- [CFXMLTreeCreateFromData](cfxmltreecreatefromdata.md) — Parses the given XML data and returns the resulting CFXMLTree object. _(deprecated)_
- [CFXMLTreeCreateFromDataWithError](cfxmltreecreatefromdatawitherror.md) — Parses the given XML data and returns the resulting CFXMLTree object and any error information. _(deprecated)_
- [CFXMLTreeCreateWithNode](cfxmltreecreatewithnode.md) — Creates a childless, parentless CFXMLTree object node for a CFXMLNode object. _(deprecated)_
- [CFXMLTreeCreateXMLData](cfxmltreecreatexmldata.md) — Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage. _(deprecated)_
- [CFXMLTreeGetNode](cfxmltreegetnode.md) — Returns the node of a CFXMLTree object. _(deprecated)_
