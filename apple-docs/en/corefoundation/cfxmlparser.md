---
title: CFXMLParser
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparser
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparser.json'
content_hash: 'sha256:6d7d46d791a0fc25'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParser

<sub>Class</sub>

<sub>macOS</sub>

```swift
class CFXMLParser
```

## Overview

CFXMLParser provides an XML parser you can use to find and extract data in XML documents. You can use a high-level interface to load an XML document into a Core Foundation collection object. A low-level callback-based interface allows you to perform any action you wish on an XML structured type when it is detected by the parser. This opaque type is relevant for applications that need information about an XML document’s structure or content.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Callbacks

- [CFXMLParserAddChildCallBack](cfxmlparseraddchildcallback.md) — Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [CFXMLParserCopyDescriptionCallBack](cfxmlparsercopydescriptioncallback.md) — Callback function invoked by the parser when handling the information pointer.
- [CFXMLParserCreateXMLStructureCallBack](cfxmlparsercreatexmlstructurecallback.md) — Callback function invoked when the parser encounters an XML open tag.
- [CFXMLParserEndXMLStructureCallBack](cfxmlparserendxmlstructurecallback.md) — Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.
- [CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md) — Callback function invoked by the parser to notify your application that an error has occurred.
- [CFXMLParserReleaseCallBack](cfxmlparserreleasecallback.md) — Callback function invoked by the parser when it wants to release a reference to the information pointer.
- [CFXMLParserResolveExternalEntityCallBack](cfxmlparserresolveexternalentitycallback.md) — Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [CFXMLParserRetainCallBack](cfxmlparserretaincallback.md) — Callback function invoked by the parser when it needs another reference to the information pointer.

### Data Types

- [CFXMLParserCallBacks](cfxmlparsercallbacks.md) — Contains version information and function pointers to callbacks needed when parsing XML.
- [CFXMLParserContext](cfxmlparsercontext.md) — Contains version information and function pointers to callbacks used when handling a program-defined context.

### Constants

- [CFXMLParserStatusCode](cfxmlparserstatuscode.md) — The various status and error flags that can be returned by the parser.
- [CFXMLParserOptions](cfxmlparseroptions.md) — Options you can use to control the parser’s treatment of an XML document.

## See Also

### Related Documentation

- [XML Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
