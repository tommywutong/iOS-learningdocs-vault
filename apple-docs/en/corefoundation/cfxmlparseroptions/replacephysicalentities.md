---
title: replacePhysicalEntities
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparseroptions/replacephysicalentities
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/replacephysicalentities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparseroptions/replacephysicalentities.json'
content_hash: 'sha256:96bc512b078e5efd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFXMLParserOptions](../cfxmlparseroptions.md)

# replacePhysicalEntities

<sub>Type Property</sub>

Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.

<sub>macOS</sub>

```swift
static var replacePhysicalEntities: CFXMLParserOptions { get }
```

## See Also

### Constants

- [kCFXMLParserValidateDocument](validatedocument.md) — Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [kCFXMLParserSkipMetaData](skipmetadata.md) — Silently skip over metadata constructs (the DTD and comments).
- [kCFXMLParserSkipWhitespace](skipwhitespace.md)
- [kCFXMLParserResolveExternalEntities](resolveexternalentities.md) — Resolves all external entities.
- [kCFXMLParserAddImpliedAttributes](addimpliedattributes.md) — Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
- [kCFXMLParserAllOptions](alloptions.md) — Makes the parser do the most work, returning only the pure elementtree.
