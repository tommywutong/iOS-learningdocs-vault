---
title: CFXMLParserCopyErrorDescription
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlparsercopyerrordescription
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparsercopyerrordescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparsercopyerrordescription.json'
content_hash: 'sha256:6e2bcfe275ddb499'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserCopyErrorDescription

<sub>Function</sub>

Returns the user-readable description of the current error condition.

<sub>macOS</sub>

```objc
extern CFStringRefCFXMLParserCopyErrorDescription(CFXMLParserRef parser);
```

## Parameters

- `parser` — The XML parser to examine.

## Return Value

A user-readable description of the current error condition, or `NULL` if no error occurred. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFXMLParser Miscellaneous Functions

- [CFXMLParserAbort](cfxmlparserabort.md) — Causes a parser to abort with the given error code and description. _(deprecated)_
- [CFXMLParserCreate](cfxmlparsercreate.md) — Creates a new XML parser for the specified XML data. _(deprecated)_
- [CFXMLParserCreateWithDataFromURL](cfxmlparsercreatewithdatafromurl.md) — Creates a new XML parser for the specified XML data at the specified URL. _(deprecated)_
- [CFXMLParserGetCallBacks](cfxmlparsergetcallbacks.md) — Returns the callbacks associated with an XML parser when it was created. _(deprecated)_
- [CFXMLParserGetContext](cfxmlparsergetcontext.md) — Returns the context for an XML parser. _(deprecated)_
- [CFXMLParserGetDocument](cfxmlparsergetdocument.md) — Returns the top-most object returned by the create XML structure callback. _(deprecated)_
- [CFXMLParserGetLineNumber](cfxmlparsergetlinenumber.md) — Returns the line number of the current parse location. _(deprecated)_
- [CFXMLParserGetLocation](cfxmlparsergetlocation.md) — Returns the character index of the current parse location. _(deprecated)_
- [CFXMLParserGetSourceURL](cfxmlparsergetsourceurl.md) — Returns the URL for the XML data being parsed. _(deprecated)_
- [CFXMLParserGetStatusCode](cfxmlparsergetstatuscode.md) — Returns a numeric code indicating the current status of the parser. _(deprecated)_
- [CFXMLParserGetTypeID](cfxmlparsergettypeid.md) — Returns the type identifier for the CFXMLParser opaque type. _(deprecated)_
- [CFXMLParserParse](cfxmlparserparse.md) — Begins a parse of the XML data that was associated with the parser when it was created. _(deprecated)_
