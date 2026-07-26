---
title: CFXMLParserGetLineNumber
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.8 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfxmlparsergetlinenumber
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparsergetlinenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparsergetlinenumber.json'
content_hash: 'sha256:05bf0a3fee270158'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserGetLineNumber

<sub>Function</sub>

Returns the line number of the current parse location.

<sub>macOS</sub>

```objc
extern CFIndex CFXMLParserGetLineNumber(CFXMLParserRef parser);
```

## Parameters

- `parser` — The XML parser to examine.

## Return Value

The line number of the current location.

## Discussion

This function is typically used in conjunction with the [CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md) function so that error location information can be reported.

## See Also

### CFXMLParser Miscellaneous Functions

- [CFXMLParserAbort](cfxmlparserabort.md) — Causes a parser to abort with the given error code and description. _(deprecated)_
- [CFXMLParserCopyErrorDescription](cfxmlparsercopyerrordescription.md) — Returns the user-readable description of the current error condition. _(deprecated)_
- [CFXMLParserCreate](cfxmlparsercreate.md) — Creates a new XML parser for the specified XML data. _(deprecated)_
- [CFXMLParserCreateWithDataFromURL](cfxmlparsercreatewithdatafromurl.md) — Creates a new XML parser for the specified XML data at the specified URL. _(deprecated)_
- [CFXMLParserGetCallBacks](cfxmlparsergetcallbacks.md) — Returns the callbacks associated with an XML parser when it was created. _(deprecated)_
- [CFXMLParserGetContext](cfxmlparsergetcontext.md) — Returns the context for an XML parser. _(deprecated)_
- [CFXMLParserGetDocument](cfxmlparsergetdocument.md) — Returns the top-most object returned by the create XML structure callback. _(deprecated)_
- [CFXMLParserGetLocation](cfxmlparsergetlocation.md) — Returns the character index of the current parse location. _(deprecated)_
- [CFXMLParserGetSourceURL](cfxmlparsergetsourceurl.md) — Returns the URL for the XML data being parsed. _(deprecated)_
- [CFXMLParserGetStatusCode](cfxmlparsergetstatuscode.md) — Returns a numeric code indicating the current status of the parser. _(deprecated)_
- [CFXMLParserGetTypeID](cfxmlparsergettypeid.md) — Returns the type identifier for the CFXMLParser opaque type. _(deprecated)_
- [CFXMLParserParse](cfxmlparserparse.md) — Begins a parse of the XML data that was associated with the parser when it was created. _(deprecated)_
