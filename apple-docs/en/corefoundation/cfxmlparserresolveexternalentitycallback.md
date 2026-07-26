---
title: CFXMLParserResolveExternalEntityCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparserresolveexternalentitycallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparserresolveexternalentitycallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparserresolveexternalentitycallback.json'
content_hash: 'sha256:7a2946742e4baf2c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserResolveExternalEntityCallBack

<sub>Type Alias</sub>

Callback function invoked by the parser to notify your application that an external entity has been referenced.

<sub>macOS</sub>

```swift
typealias CFXMLParserResolveExternalEntityCallBack = (CFXMLParser?, UnsafeMutablePointer<CFXMLExternalID>?, UnsafeMutableRawPointer?) -> Unmanaged<CFData>?
```

## Parameters

- `parser` — The CFXMLParser object making the callback.

- `extID` — The identifier for the external entity.

- `info` — The program-defined context data you specified in the [CFXMLParserContext](cfxmlparsercontext.md) structure when creating the parser.

## Return Value

The external entity or `NULL` if it should not be resolved.

## Discussion

If this callback is not defined, the parser uses its internal routines to try and resolve the entity. Otherwise, if this callback returns NULL, a place holder for the external entity is inserted into the tree. In this manner, the parser’s client can prevent any external network or file accesses. This callback is optional.

## See Also

### Callbacks

- [CFXMLParserAddChildCallBack](cfxmlparseraddchildcallback.md) — Callback function invoked by the parser to notify your application of parent/child relationships between XML structures.
- [CFXMLParserCopyDescriptionCallBack](cfxmlparsercopydescriptioncallback.md) — Callback function invoked by the parser when handling the information pointer.
- [CFXMLParserCreateXMLStructureCallBack](cfxmlparsercreatexmlstructurecallback.md) — Callback function invoked when the parser encounters an XML open tag.
- [CFXMLParserEndXMLStructureCallBack](cfxmlparserendxmlstructurecallback.md) — Callback function invoked by the parser to notify your application that an XML structure (and all its children) have been completely parsed.
- [CFXMLParserHandleErrorCallBack](cfxmlparserhandleerrorcallback.md) — Callback function invoked by the parser to notify your application that an error has occurred.
- [CFXMLParserReleaseCallBack](cfxmlparserreleasecallback.md) — Callback function invoked by the parser when it wants to release a reference to the information pointer.
- [CFXMLParserRetainCallBack](cfxmlparserretaincallback.md) — Callback function invoked by the parser when it needs another reference to the information pointer.
