---
title: resolveExternalEntities
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparseroptions/resolveexternalentities
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/resolveexternalentities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparseroptions/resolveexternalentities.json'
content_hash: 'sha256:1b9856f716eba73d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFXMLParserOptions](../cfxmlparseroptions.md)

# resolveExternalEntities

<sub>Type Property</sub>

Resolves all external entities.

<sub>macOS</sub>

```swift
static var resolveExternalEntities: CFXMLParserOptions { get }
```

## See Also

### Constants

- [kCFXMLParserValidateDocument](validatedocument.md) — Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [kCFXMLParserSkipMetaData](skipmetadata.md) — Silently skip over metadata constructs (the DTD and comments).
- [kCFXMLParserReplacePhysicalEntities](replacephysicalentities.md) — Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [kCFXMLParserSkipWhitespace](skipwhitespace.md)
- [kCFXMLParserAddImpliedAttributes](addimpliedattributes.md) — Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
- [kCFXMLParserAllOptions](alloptions.md) — Makes the parser do the most work, returning only the pure elementtree.
