---
title: addImpliedAttributes
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparseroptions/addimpliedattributes
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/addimpliedattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparseroptions/addimpliedattributes.json'
content_hash: 'sha256:6d2d3e9bf422a6b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFXMLParserOptions](../cfxmlparseroptions.md)

# addImpliedAttributes

<sub>Type Property</sub>

Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.

<sub>macOS</sub>

```swift
static var addImpliedAttributes: CFXMLParserOptions { get }
```

## See Also

### Constants

- [kCFXMLParserValidateDocument](validatedocument.md) — Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [kCFXMLParserSkipMetaData](skipmetadata.md) — Silently skip over metadata constructs (the DTD and comments).
- [kCFXMLParserReplacePhysicalEntities](replacephysicalentities.md) — Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [kCFXMLParserSkipWhitespace](skipwhitespace.md)
- [kCFXMLParserResolveExternalEntities](resolveexternalentities.md) — Resolves all external entities.
- [kCFXMLParserAllOptions](alloptions.md) — Makes the parser do the most work, returning only the pure elementtree.
