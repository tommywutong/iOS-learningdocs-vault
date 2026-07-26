---
title: 'parser(_:resolveExternalEntityName:systemID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparserdelegate/parser(_:resolveexternalentityname:systemid:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:resolveexternalentityname:systemid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparserdelegate/parser%28_%3Aresolveexternalentityname%3Asystemid%3A%29.json'
content_hash: 'sha256:68a7cdef264ff62e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParserDelegate](../xmlparserdelegate.md)

# parser(_:resolveExternalEntityName:systemID:)

<sub>Instance Method</sub>

Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func parser(_ parser: XMLParser, resolveExternalEntityName name: String, systemID: String?) -> Data?
```

## Parameters

- `parser` — A parser object.

- `name` — A string that specifies the external name of an entity.

- `systemID` — A string that specifies the system ID for the external entity.

## Return Value

An [NSData](../nsdata.md) object that contains the resolution of the given external entity.

## Discussion

The delegate can resolve the external entity (for example, locating and reading an externally declared DTD) and provide the result to the parser object as an `NSData` object.

## See Also

### Related Documentation

- [- parser:foundExternalEntityDeclarationWithName:publicID:systemID:](<parser(__foundexternalentitydeclarationwithname_publicid_systemid_).md>) — Sent by a parser object to its delegate when it encounters an external entity declaration.
- [- parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:](<parser(__foundunparsedentitydeclarationwithname_publicid_systemid_notationname_).md>) — Sent by a parser object to its delegate when it encounters an unparsed entity declaration.

### Handling XML

- [- parserDidStartDocument:](<parserdidstartdocument(__).md>) — Sent by the parser object to the delegate when it begins parsing a document.
- [- parserDidEndDocument:](<parserdidenddocument(__).md>) — Sent by the parser object to the delegate when it has successfully completed parsing.
- [- parser:didStartElement:namespaceURI:qualifiedName:attributes:](<parser(__didstartelement_namespaceuri_qualifiedname_attributes_).md>) — Sent by a parser object to its delegate when it encounters a start tag for a given element.
- [- parser:didEndElement:namespaceURI:qualifiedName:](<parser(__didendelement_namespaceuri_qualifiedname_).md>) — Sent by a parser object to its delegate when it encounters an end tag for a specific element.
- [- parser:didStartMappingPrefix:toURI:](<parser(__didstartmappingprefix_touri_).md>) — Sent by a parser object to its delegate the first time it encounters a given namespace prefix, which is mapped to a URI.
- [- parser:didEndMappingPrefix:](<parser(__didendmappingprefix_).md>) — Sent by a parser object to its delegate when a given namespace prefix goes out of scope.
- [- parser:parseErrorOccurred:](<parser(__parseerroroccurred_).md>) — Sent by a parser object to its delegate when it encounters a fatal error.
- [- parser:validationErrorOccurred:](<parser(__validationerroroccurred_).md>) — Sent by a parser object to its delegate when it encounters a fatal validation error. `NSXMLParser` currently does not invoke this method and does not perform validation.
- [- parser:foundCharacters:](<parser(__foundcharacters_).md>) — Sent by a parser object to provide its delegate with a string representing all or part of the characters of the current element.
- [- parser:foundIgnorableWhitespace:](<parser(__foundignorablewhitespace_).md>) — Reported by a parser object to provide its delegate with a string representing all or part of the ignorable whitespace characters of the current element.
- [- parser:foundProcessingInstructionWithTarget:data:](<parser(__foundprocessinginstructionwithtarget_data_).md>) — Sent by a parser object to its delegate when it encounters a processing instruction.
- [- parser:foundComment:](<parser(__foundcomment_).md>) — Sent by a parser object to its delegate when it encounters a comment in the XML.
- [- parser:foundCDATA:](<parser(__foundcdata_).md>) — Sent by a parser object to its delegate when it encounters a CDATA block.
