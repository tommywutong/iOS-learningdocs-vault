---
title: CFXMLParserOptions
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparseroptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparseroptions.json'
content_hash: 'sha256:ff0b5faac760a2ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFXMLParserOptions

<sub>Structure</sub>

Options you can use to control the parser’s treatment of an XML document.

<sub>macOS</sub>

```swift
struct CFXMLParserOptions
```

## Overview

These are the various options you use to configure the parser. An option flag of 0 ([kCFXMLParserNoOptions](cfxmlparseroptions/kcfxmlparsernooptions.md)) leaves the XML as “intact” as possible (reports all structures; performs no replacements). Hence, to make the parser do the most work, returning only the pure element tree, set the option flag to [kCFXMLParserAllOptions](cfxmlparseroptions/alloptions.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFXMLParserValidateDocument](cfxmlparseroptions/validatedocument.md) — Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [kCFXMLParserSkipMetaData](cfxmlparseroptions/skipmetadata.md) — Silently skip over metadata constructs (the DTD and comments).
- [kCFXMLParserReplacePhysicalEntities](cfxmlparseroptions/replacephysicalentities.md) — Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [kCFXMLParserSkipWhitespace](cfxmlparseroptions/skipwhitespace.md)
- [kCFXMLParserResolveExternalEntities](cfxmlparseroptions/resolveexternalentities.md) — Resolves all external entities.
- [kCFXMLParserAddImpliedAttributes](cfxmlparseroptions/addimpliedattributes.md) — Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
- [kCFXMLParserAllOptions](cfxmlparseroptions/alloptions.md) — Makes the parser do the most work, returning only the pure elementtree.

### Initializers

- [init(rawValue:)](<cfxmlparseroptions/init(rawvalue_).md>)

## See Also

### Constants

- [CFXMLParserStatusCode](cfxmlparserstatuscode.md) — The various status and error flags that can be returned by the parser.
