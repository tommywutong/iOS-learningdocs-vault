---
title: CFXMLParserCopyDescriptionCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparsercopydescriptioncallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparsercopydescriptioncallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparsercopydescriptioncallback.json'
content_hash: 'sha256:6cbdc52daef80f15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserCopyDescriptionCallBack

<sub>Type Alias</sub>

Callback function invoked by the parser when handling the information pointer.

<sub>macOS</sub>

```swift
typealias CFXMLParserCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

## Parameters

- `info` — The program-defined context data you specified in the [CFXMLParserContext](cfxmlparsercontext.md) structure when creating the parser.

## Return Value

A textual description of `info`. The caller is responsible for releasing this object.

## See Also

### Callbacks

- [CFXMLParserAddChildCallBack](cfxmlparseraddchildcallback.md) — Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [CFXMLParserCreateXMLStructureCallBack](cfxmlparsercreatexmlstructurecallback.md) — Callback function invoked when the parser encounters an XML open tag.
- [CFXMLParserEndXMLStructureCallBack](cfxmlparserendxmlstructurecallback.md) — Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.
- [CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md) — Callback function invoked by the parser to notify your application that an error has occurred.
- [CFXMLParserReleaseCallBack](cfxmlparserreleasecallback.md) — Callback function invoked by the parser when it wants to release a reference to the information pointer.
- [CFXMLParserResolveExternalEntityCallBack](cfxmlparserresolveexternalentitycallback.md) — Callback function invoked by the parser to notify your application that an external entity has been referenced.
- [CFXMLParserRetainCallBack](cfxmlparserretaincallback.md) — Callback function invoked by the parser when it needs another reference to the information pointer.
