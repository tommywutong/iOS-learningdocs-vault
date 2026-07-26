---
title: CFXMLParserCallBacks
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparsercallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparsercallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparsercallbacks.json'
content_hash: 'sha256:0a3fb85d5d99f647'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserCallBacks

<sub>Structure</sub>

Contains version information and function pointers to callbacks needed when parsing XML.

<sub>macOS</sub>

```swift
struct CFXMLParserCallBacks
```

## Overview

This structure is passed to one of the `CFXMLParserCreate...` functions. Only the `createXMLStructure`, `addChild`, and `endXMLStructure` fields are required. Set the others to `NULL` if you don’t wish to implement them.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfxmlparsercallbacks/init().md>)
- [init(version:createXMLStructure:addChild:endXMLStructure:resolveExternalEntity:handleError:)](<cfxmlparsercallbacks/init(version_createxmlstructure_addchild_endxmlstructure_resolveexternalentity_handleerror_).md>)

### Instance Properties

- [addChild](cfxmlparsercallbacks/addchild.md) — Called when a child is added.
- [createXMLStructure](cfxmlparsercallbacks/createxmlstructure.md) — Called when an XML structure is created.
- [endXMLStructure](cfxmlparsercallbacks/endxmlstructure.md) — Called when an XML structure has ended.
- [handleError](cfxmlparsercallbacks/handleerror.md) — Called when a parse error needs to be handled.
- [resolveExternalEntity](cfxmlparsercallbacks/resolveexternalentity.md) — Called when an external entity needs to be resolved.
- [version](cfxmlparsercallbacks/version.md) — Version number. Must be `0`.

## See Also

### Data Types

- [CFXMLParserContext](cfxmlparsercontext.md) — Contains version information and function pointers to callbacks used when handling a program-defined context.
