---
title: 'parser(_:foundElementDeclarationWithName:model:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparserdelegate/parser(_:foundelementdeclarationwithname:model:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundelementdeclarationwithname:model:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparserdelegate/parser%28_%3Afoundelementdeclarationwithname%3Amodel%3A%29.json'
content_hash: 'sha256:05b0359f4d33c306'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParserDelegate](../xmlparserdelegate.md)

# parser(_:foundElementDeclarationWithName:model:)

<sub>Instance Method</sub>

Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func parser(_ parser: XMLParser, foundElementDeclarationWithName elementName: String, model: String)
```

## Parameters

- `parser` — An `NSXMLParser` object parsing XML.

- `elementName` — A string that is the name of an element.

- `model` — A string that specifies a model for `elementName`.

## See Also

### Related Documentation

- [- parser:didStartElement:namespaceURI:qualifiedName:attributes:](<parser(__didstartelement_namespaceuri_qualifiedname_attributes_).md>) — Sent by a parser object to its delegate when it encounters a start tag for a given element.

### Handling the DTD

- [- parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:](<parser(__foundattributedeclarationwithname_forelement_type_defaultvalue_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [- parser:foundExternalEntityDeclarationWithName:publicID:systemID:](<parser(__foundexternalentitydeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters an external entity declaration.
- [- parser:foundInternalEntityDeclarationWithName:value:](<parser(__foundinternalentitydeclarationwithname_value_).md>) — Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [- parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:](<parser(__foundunparsedentitydeclarationwithname_publicid_systemid_notationname_).md>) — Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [- parser:foundNotationDeclarationWithName:publicID:systemID:](<parser(__foundnotationdeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters a notation declaration.
