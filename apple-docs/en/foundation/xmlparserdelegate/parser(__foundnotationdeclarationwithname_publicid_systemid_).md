---
title: 'parser(_:foundNotationDeclarationWithName:publicID:systemID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparserdelegate/parser(_:foundnotationdeclarationwithname:publicid:systemid:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundnotationdeclarationwithname:publicid:systemid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparserdelegate/parser%28_%3Afoundnotationdeclarationwithname%3Apublicid%3Asystemid%3A%29.json'
content_hash: 'sha256:89d046e93d1a02ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParserDelegate](../xmlparserdelegate.md)

# parser(_:foundNotationDeclarationWithName:publicID:systemID:)

<sub>Instance Method</sub>

Sent by a parser object to its delegate when it encounters a notation declaration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func parser(_ parser: XMLParser, foundNotationDeclarationWithName name: String, publicID: String?, systemID: String?)
```

## Parameters

- `parser` — An `NSXMLParser` object parsing XML.

- `name` — A string that is the name of the notation.

- `publicID` — A string specifying the public ID associated with the notation `name`.

- `systemID` — A string specifying the system ID associated with the notation `name`.

## See Also

### Handling the DTD

- [- parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:](<parser(__foundattributedeclarationwithname_forelement_type_defaultvalue_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [- parser:foundElementDeclarationWithName:model:](<parser(__foundelementdeclarationwithname_model_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [- parser:foundExternalEntityDeclarationWithName:publicID:systemID:](<parser(__foundexternalentitydeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters an external entity declaration.
- [- parser:foundInternalEntityDeclarationWithName:value:](<parser(__foundinternalentitydeclarationwithname_value_).md>) — Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [- parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:](<parser(__foundunparsedentitydeclarationwithname_publicid_systemid_notationname_).md>) — Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
