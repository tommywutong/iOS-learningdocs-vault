---
title: skipWhitespace
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfxmlparseroptions/skipwhitespace
source_url: 'https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/skipwhitespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfxmlparseroptions/skipwhitespace.json'
content_hash: 'sha256:c8db4772ee888031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFXMLParserOptions](../cfxmlparseroptions.md)

# skipWhitespace

<sub>Type Property</sub>

<sub>macOS</sub>

```swift
static var skipWhitespace: CFXMLParserOptions { get }
```

## Discussion

Skip over all whitespace that does not abut non-whitespace character data. In other words, given “`<foo>  <bar> blah </bar></foo>`,” the whitespace between foo’s open tag and bar’s open tag would be suppressed, but the whitespace around `blah` would be preserved.

## See Also

### Constants

- [kCFXMLParserValidateDocument](validatedocument.md) — Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [kCFXMLParserSkipMetaData](skipmetadata.md) — Silently skip over metadata constructs (the DTD and comments).
- [kCFXMLParserReplacePhysicalEntities](replacephysicalentities.md) — Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [kCFXMLParserResolveExternalEntities](resolveexternalentities.md) — Resolves all external entities.
- [kCFXMLParserAddImpliedAttributes](addimpliedattributes.md) — Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
- [kCFXMLParserAllOptions](alloptions.md) — Makes the parser do the most work, returning only the pure elementtree.
