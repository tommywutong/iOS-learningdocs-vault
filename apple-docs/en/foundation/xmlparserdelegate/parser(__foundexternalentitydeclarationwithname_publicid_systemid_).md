---
title: 'parser(_:foundExternalEntityDeclarationWithName:publicID:systemID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparserdelegate/parser(_:foundexternalentitydeclarationwithname:publicid:systemid:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundexternalentitydeclarationwithname:publicid:systemid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparserdelegate/parser%28_%3Afoundexternalentitydeclarationwithname%3Apublicid%3Asystemid%3A%29.json'
content_hash: 'sha256:17548f45ef1e5e82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParserDelegate](../xmlparserdelegate.md)

# parser(_:foundExternalEntityDeclarationWithName:publicID:systemID:)

<sub>Instance Method</sub>

Sent by a parser object to its delegate when it encounters an external entity declaration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func parser(_ parser: XMLParser, foundExternalEntityDeclarationWithName name: String, publicID: String?, systemID: String?)
```

## Parameters

- `parser` — An `NSXMLParser` object parsing XML.

- `name` — A string that is the name of an entity.

- `publicID` — A string that specifies the public ID associated with `entityName`.

- `systemID` — A string that specifies the system ID associated with `entityName`.

## See Also

### Related Documentation

- [- parser:resolveExternalEntityName:systemID:](<parser(__resolveexternalentityname_systemid_).md>) — Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.

### Handling the DTD

- [- parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:](<parser(__foundattributedeclarationwithname_forelement_type_defaultvalue_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [- parser:foundElementDeclarationWithName:model:](<parser(__foundelementdeclarationwithname_model_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [- parser:foundInternalEntityDeclarationWithName:value:](<parser(__foundinternalentitydeclarationwithname_value_).md>) — Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [- parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:](<parser(__foundunparsedentitydeclarationwithname_publicid_systemid_notationname_).md>) — Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [- parser:foundNotationDeclarationWithName:publicID:systemID:](<parser(__foundnotationdeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters a notation declaration.
