---
title: CFXMLParserReleaseCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparserreleasecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparserreleasecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparserreleasecallback.json'
content_hash: 'sha256:786fc6af8ee863e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserReleaseCallBack

<sub>Type Alias</sub>

Callback function invoked by the parser when it wants to release a reference to the information pointer.

<sub>macOS</sub>

```swift
typealias CFXMLParserReleaseCallBack = (UnsafeRawPointer?) -> Void
```

## Parameters

- `info` — The program-defined context data you specified in the [CFXMLParserContext](cfxmlparsercontext.md) structure when creating the parser.

## See Also

### Callbacks

- [CFXMLParserAddChildCallBack](cfxmlparseraddchildcallback.md) — Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [CFXMLParserCopyDescriptionCallBack](cfxmlparsercopydescriptioncallback.md) — Callback function invoked by the parser when handling the information pointer.
- [CFXMLParserCreateXMLStructureCallBack](cfxmlparsercreatexmlstructurecallback.md) — Callback function invoked when the parser encounters an XML open tag.
- [CFXMLParserEndXMLStructureCallBack](cfxmlparserendxmlstructurecallback.md) — Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.
- [CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md) — Callback function invoked by the parser to notify your application that an error has occurred.
- [CFXMLParserResolveExternalEntityCallBack](cfxmlparserresolveexternalentitycallback.md) — Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [CFXMLParserRetainCallBack](cfxmlparserretaincallback.md) — Callback function invoked by the parser when it needs another reference to the information pointer.
