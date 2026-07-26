---
title: XMLParserDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparserdelegate
source_url: 'https://developer.apple.com/documentation/foundation/xmlparserdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparserdelegate.json'
content_hash: 'sha256:79c6a74e0d947e06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XMLParserDelegate

<sub>Protocol</sub>

The interface an XML parser uses to inform its delegate about the content of the parsed document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol XMLParserDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling XML

- [- parserDidStartDocument:](<xmlparserdelegate/parserdidstartdocument(__).md>) — Sent by the parser object to the delegate when it begins parsing a document.
- [- parserDidEndDocument:](<xmlparserdelegate/parserdidenddocument(__).md>) — Sent by the parser object to the delegate when it has successfully completed parsing.
- [- parser:didStartElement:namespaceURI:qualifiedName:attributes:](<xmlparserdelegate/parser(__didstartelement_namespaceuri_qualifiedname_attributes_).md>) — Sent by a parser object to its delegate when it encounters a start tag for a given element.
- [- parser:didEndElement:namespaceURI:qualifiedName:](<xmlparserdelegate/parser(__didendelement_namespaceuri_qualifiedname_).md>) — Sent by a parser object to its delegate when it encounters an end tag for a specific element.
- [- parser:didStartMappingPrefix:toURI:](<xmlparserdelegate/parser(__didstartmappingprefix_touri_).md>) — Sent by a parser object to its delegate the first time it encounters a given namespace prefix, which is mapped to a URI.
- [- parser:didEndMappingPrefix:](<xmlparserdelegate/parser(__didendmappingprefix_).md>) — Sent by a parser object to its delegate when a given namespace prefix goes out of scope.
- [- parser:resolveExternalEntityName:systemID:](<xmlparserdelegate/parser(__resolveexternalentityname_systemid_).md>) — Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.
- [- parser:parseErrorOccurred:](<xmlparserdelegate/parser(__parseerroroccurred_).md>) — Sent by a parser object to its delegate when it encounters a fatal error.
- [- parser:validationErrorOccurred:](<xmlparserdelegate/parser(__validationerroroccurred_).md>) — Sent by a parser object to its delegate when it encounters a fatal validation error. `NSXMLParser` currently does not invoke this method and does not perform validation.
- [- parser:foundCharacters:](<xmlparserdelegate/parser(__foundcharacters_).md>) — Sent by a parser object to provide its delegate with a string representing all or part of the characters of the current element.
- [- parser:foundIgnorableWhitespace:](<xmlparserdelegate/parser(__foundignorablewhitespace_).md>) — Reported by a parser object to provide its delegate with a string representing all or part of the ignorable whitespace characters of the current element.
- [- parser:foundProcessingInstructionWithTarget:data:](<xmlparserdelegate/parser(__foundprocessinginstructionwithtarget_data_).md>) — Sent by a parser object to its delegate when it encounters a processing instruction.
- [- parser:foundComment:](<xmlparserdelegate/parser(__foundcomment_).md>) — Sent by a parser object to its delegate when it encounters a comment in the XML.
- [- parser:foundCDATA:](<xmlparserdelegate/parser(__foundcdata_).md>) — Sent by a parser object to its delegate when it encounters a CDATA block.

### Handling the DTD

- [- parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:](<xmlparserdelegate/parser(__foundattributedeclarationwithname_forelement_type_defaultvalue_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [- parser:foundElementDeclarationWithName:model:](<xmlparserdelegate/parser(__foundelementdeclarationwithname_model_).md>) — Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [- parser:foundExternalEntityDeclarationWithName:publicID:systemID:](<xmlparserdelegate/parser(__foundexternalentitydeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters an external entity declaration.
- [- parser:foundInternalEntityDeclarationWithName:value:](<xmlparserdelegate/parser(__foundinternalentitydeclarationwithname_value_).md>) — Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [- parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:](<xmlparserdelegate/parser(__foundunparsedentitydeclarationwithname_publicid_systemid_notationname_).md>) — Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [- parser:foundNotationDeclarationWithName:publicID:systemID:](<xmlparserdelegate/parser(__foundnotationdeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters a notation declaration.

## See Also

### Event-Based Processing

- [XMLParser](xmlparser.md) — An event driven parser of XML documents (including DTD declarations).
