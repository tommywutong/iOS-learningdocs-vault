---
title: kCFXMLParserNoOptions
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparseroptions/kcfxmlparsernooptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/kcfxmlparsernooptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparseroptions/kcfxmlparsernooptions.json'
content_hash: 'sha256:4460a836aae9914a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFXMLParserOptions](../cfxmlparseroptions.md)

# kCFXMLParserNoOptions

<sub>Enumeration Case</sub>

Leaves the XML as “intact” as possible (reports all structures; performs no replacements).

<sub>macOS</sub>

```objc
kCFXMLParserNoOptions
```

## See Also

### Constants

- [kCFXMLParserValidateDocument](validatedocument.md) — Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [kCFXMLParserSkipMetaData](skipmetadata.md) — Silently skip over metadata constructs (the DTD and comments).
- [kCFXMLParserReplacePhysicalEntities](replacephysicalentities.md) — Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [kCFXMLParserSkipWhitespace](skipwhitespace.md)
- [kCFXMLParserResolveExternalEntities](resolveexternalentities.md) — Resolves all external entities.
- [kCFXMLParserAddImpliedAttributes](addimpliedattributes.md) — Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
- [kCFXMLParserAllOptions](alloptions.md) — Makes the parser do the most work, returning only the pure elementtree.
