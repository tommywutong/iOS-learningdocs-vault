---
title: CFXMLParserCreateWithDataFromURL
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlparsercreatewithdatafromurl
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparsercreatewithdatafromurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparsercreatewithdatafromurl.json'
content_hash: 'sha256:f2638eb439b1c9c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserCreateWithDataFromURL

<sub>Function</sub>

Creates a new XML parser for the specified XML data at the specified URL.

<sub>macOS</sub>

```objc
extern CFXMLParserRefCFXMLParserCreateWithDataFromURL(CFAllocatorRef allocator, CFURLRef dataSource, CFOptionFlags parseOptions, CFIndex versionOfNodes, CFXMLParserCallBacks *callBacks, CFXMLParserContext *context);
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `dataSource` — The URL from which to load the XML data. The URL is used to resolve any relative references found in XML Data. It must be a valid CFURL object; `NULL` is an unacceptable value.

- `parseOptions` — Flags which control how the XML data will be parsed. See [CFXMLParserOptions](cfxmlparseroptions.md) for the list of available options.

- `versionOfNodes` — Determines which version of CFXMLNode objects are produced by the parser.

- `callBacks` — Callbacks called by the parser as the XML is processed. The callbacks are called as each XML tag is encountered, when an external entity needs to be resolved, and when an error occurs. See [CFXMLParserCallBacks](cfxmlparsercallbacks.md) and the individual callbacks for more details. Do not pass `NULL`.

- `context` — Determines what, if any, information pointer is passed to the callbacks as the parse progresses; may be `NULL`.

## Return Value

The newly created parser. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFXMLParser Miscellaneous Functions

- [CFXMLParserAbort](cfxmlparserabort.md) — Causes a parser to abort with the given error code and description. _(deprecated)_
- [CFXMLParserCopyErrorDescription](cfxmlparsercopyerrordescription.md) — Returns the user-readable description of the current error condition. _(deprecated)_
- [CFXMLParserCreate](cfxmlparsercreate.md) — Creates a new XML parser for the specified XML data. _(deprecated)_
- [CFXMLParserGetCallBacks](cfxmlparsergetcallbacks.md) — Returns the callbacks associated with an XML parser when it was created. _(deprecated)_
- [CFXMLParserGetContext](cfxmlparsergetcontext.md) — Returns the context for an XML parser. _(deprecated)_
- [CFXMLParserGetDocument](cfxmlparsergetdocument.md) — Returns the top-most object returned by the create XML structure callback. _(deprecated)_
- [CFXMLParserGetLineNumber](cfxmlparsergetlinenumber.md) — Returns the line number of the current parse location. _(deprecated)_
- [CFXMLParserGetLocation](cfxmlparsergetlocation.md) — Returns the character index of the current parse location. _(deprecated)_
- [CFXMLParserGetSourceURL](cfxmlparsergetsourceurl.md) — Returns the URL for the XML data being parsed. _(deprecated)_
- [CFXMLParserGetStatusCode](cfxmlparsergetstatuscode.md) — Returns a numeric code indicating the current status of the parser. _(deprecated)_
- [CFXMLParserGetTypeID](cfxmlparsergettypeid.md) — Returns the type identifier for the CFXMLParser opaque type. _(deprecated)_
- [CFXMLParserParse](cfxmlparserparse.md) — Begins a parse of the XML data that was associated with the parser when it was created. _(deprecated)_
