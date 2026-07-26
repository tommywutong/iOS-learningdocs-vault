---
title: 'parser(_:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparserdelegate/parser(_:foundunparsedentitydeclarationwithname:publicid:systemid:notationname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundunparsedentitydeclarationwithname:publicid:systemid:notationname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparserdelegate/parser%28_%3Afoundunparsedentitydeclarationwithname%3Apublicid%3Asystemid%3Anotationname%3A%29.json'
content_hash: 'sha256:51b13c59397f9219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParserDelegate](../xmlparserdelegate.md)

# parser(_:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:)

<sub>Instance Method</sub>

Sent by a parser object to its delegate when it encounters an unparsed entity declaration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func parser(_ parser: XMLParser, foundUnparsedEntityDeclarationWithName name: String, publicID: String?, systemID: String?, notationName: String?)
```

## Parameters

- `parser` — An `NSXMLParser` object parsing XML.

- `name` — A string that is the name of the unparsed entity in the declaration.

- `publicID` — A string specifying the public ID associated with the entity `name`.

- `systemID` — A string specifying the system ID associated with the entity `name`.

- `notationName` — A string specifying a notation of the declaration of entity `name`.

## See Also

### Related Documentation

- [- parser:resolveExternalEntityName:systemID:](<parser(__resolveexternalentityname_systemid_).md>) — Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.

### Handling the DTD

- [- parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:](<parser(__foundattributedeclarationwithname_forelement_type_defaultvalue_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [- parser:foundElementDeclarationWithName:model:](<parser(__foundelementdeclarationwithname_model_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [- parser:foundExternalEntityDeclarationWithName:publicID:systemID:](<parser(__foundexternalentitydeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters an external entity declaration.
- [- parser:foundInternalEntityDeclarationWithName:value:](<parser(__foundinternalentitydeclarationwithname_value_).md>) — Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [- parser:foundNotationDeclarationWithName:publicID:systemID:](<parser(__foundnotationdeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters a notation declaration.
