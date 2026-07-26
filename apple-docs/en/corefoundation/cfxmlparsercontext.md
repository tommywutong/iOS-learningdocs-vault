---
title: CFXMLParserContext
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparsercontext
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparsercontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparsercontext.json'
content_hash: 'sha256:4ce57976547ace7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserContext

<sub>Structure</sub>

Contains version information and function pointers to callbacks used when handling a program-defined context.

<sub>macOS</sub>

```swift
struct CFXMLParserContext
```

## Overview

You can associate a context with a parser when the parser is created. The context can be anything you wish and will be passed as a parameter to all of the XML parser callbacks.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<cfxmlparsercontext/init().md>)
- [init(version:info:retain:release:copyDescription:)](<cfxmlparsercontext/init(version_info_retain_release_copydescription_).md>)

### Instance Properties

- [copyDescription](cfxmlparsercontext/copydescription.md) — A copy description callback for your program-defined context data. Optional.
- [info](cfxmlparsercontext/info.md) — An arbitrary program-defined value passed to all the callbacks in this structure and in the [CFXMLParserCallBacks](cfxmlparsercallbacks.md) structure.
- [release](cfxmlparsercontext/release.md) — A release callback for your program-defined context data. Optional.
- [retain](cfxmlparsercontext/retain.md) — A retain callback for your program-defined context data. Optional.
- [version](cfxmlparsercontext/version.md) — Version number of this structure. Must be 0.

## See Also

### Data Types

- [CFXMLParserCallBacks](cfxmlparsercallbacks.md) — Contains version information and function pointers to callbacks needed when parsing XML.
