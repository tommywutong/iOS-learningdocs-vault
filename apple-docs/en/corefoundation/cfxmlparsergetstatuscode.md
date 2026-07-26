---
title: CFXMLParserGetStatusCode
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlparsergetstatuscode
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparsergetstatuscode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparsergetstatuscode.json'
content_hash: 'sha256:50d0f013145100e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserGetStatusCode

<sub>Function</sub>

Returns a numeric code indicating the current status of the parser.

<sub>macOS</sub>

```objc
extern CFXMLParserStatusCode CFXMLParserGetStatusCode(CFXMLParserRef parser);
```

## Parameters

- `parser` — The XML parser to examine.

## Return Value

A status code indicating the current parser. See [CFXMLParserStatusCode](cfxmlparserstatuscode.md) for a list of possible status codes.

## Discussion

If an error has occurred, the code for the last error is returned. If no error has occurred, a status code is returned.

## See Also

### CFXMLParser Miscellaneous Functions

- [CFXMLParserAbort](cfxmlparserabort.md) — Causes a parser to abort with the given error code and description. _(deprecated)_
- [CFXMLParserCopyErrorDescription](cfxmlparsercopyerrordescription.md) — Returns the user-readable description of the current error condition. _(deprecated)_
- [CFXMLParserCreate](cfxmlparsercreate.md) — Creates a new XML parser for the specified XML data. _(deprecated)_
- [CFXMLParserCreateWithDataFromURL](cfxmlparsercreatewithdatafromurl.md) — Creates a new XML parser for the specified XML data at the specified URL. _(deprecated)_
- [CFXMLParserGetCallBacks](cfxmlparsergetcallbacks.md) — Returns the callbacks associated with an XML parser when it was created. _(deprecated)_
- [CFXMLParserGetContext](cfxmlparsergetcontext.md) — Returns the context for an XML parser. _(deprecated)_
- [CFXMLParserGetDocument](cfxmlparsergetdocument.md) — Returns the top-most object returned by the create XML structure callback. _(deprecated)_
- [CFXMLParserGetLineNumber](cfxmlparsergetlinenumber.md) — Returns the line number of the current parse location. _(deprecated)_
- [CFXMLParserGetLocation](cfxmlparsergetlocation.md) — Returns the character index of the current parse location. _(deprecated)_
- [CFXMLParserGetSourceURL](cfxmlparsergetsourceurl.md) — Returns the URL for the XML data being parsed. _(deprecated)_
- [CFXMLParserGetTypeID](cfxmlparsergettypeid.md) — Returns the type identifier for the CFXMLParser opaque type. _(deprecated)_
- [CFXMLParserParse](cfxmlparserparse.md) — Begins a parse of the XML data that was associated with the parser when it was created. _(deprecated)_
