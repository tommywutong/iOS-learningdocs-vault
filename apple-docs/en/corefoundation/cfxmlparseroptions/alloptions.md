---
title: allOptions
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparseroptions/alloptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/alloptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparseroptions/alloptions.json'
content_hash: 'sha256:4cad30e1920a48ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFXMLParserOptions](../cfxmlparseroptions.md)

# allOptions

<sub>Type Property</sub>

Makes the parser do the most work, returning only the pure elementtree.

<sub>macOS</sub>

```swift
static var allOptions: CFXMLParserOptions { get }
```

## See Also

### Constants

- [kCFXMLParserValidateDocument](validatedocument.md) — Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [kCFXMLParserSkipMetaData](skipmetadata.md) — Silently skip over metadata constructs (the DTD and comments).
- [kCFXMLParserReplacePhysicalEntities](replacephysicalentities.md) — Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [kCFXMLParserSkipWhitespace](skipwhitespace.md)
- [kCFXMLParserResolveExternalEntities](resolveexternalentities.md) — Resolves all external entities.
- [kCFXMLParserAddImpliedAttributes](addimpliedattributes.md) — Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
