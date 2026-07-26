---
title: 'parserDidStartDocument(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparserdelegate/parserdidstartdocument(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparserdelegate/parserdidstartdocument(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparserdelegate/parserdidstartdocument%28_%3A%29.json'
content_hash: 'sha256:c7e58b37a5a7f935'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParserDelegate](../xmlparserdelegate.md)

# parserDidStartDocument(_:)

<sub>Instance Method</sub>

Sent by the parser object to the delegate when it begins parsing a document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func parserDidStartDocument(_ parser: XMLParser)
```

## Parameters

- `parser` — A parser object.

## See Also

### Related Documentation

- [Event-Driven XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/XMLParsing.html#//apple_ref/doc/uid/10000186i)

### Handling XML

- [- parserDidEndDocument:](<parserdidenddocument(__).md>) — Sent by the parser object to the delegate when it has successfully completed parsing.
- [- parser:didStartElement:namespaceURI:qualifiedName:attributes:](<parser(__didstartelement_namespaceuri_qualifiedname_attributes_).md>) — Sent by a parser object to its delegate when it encounters a start tag for a given element.
- [- parser:didEndElement:namespaceURI:qualifiedName:](<parser(__didendelement_namespaceuri_qualifiedname_).md>) — Sent by a parser object to its delegate when it encounters an end tag for a specific element.
- [- parser:didStartMappingPrefix:toURI:](<parser(__didstartmappingprefix_touri_).md>) — Sent by a parser object to its delegate the first time it encounters a given namespace prefix, which is mapped to a URI.
- [- parser:didEndMappingPrefix:](<parser(__didendmappingprefix_).md>) — Sent by a parser object to its delegate when a given namespace prefix goes out of scope.
- [- parser:resolveExternalEntityName:systemID:](<parser(__resolveexternalentityname_systemid_).md>) — Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.
- [- parser:parseErrorOccurred:](<parser(__parseerroroccurred_).md>) — Sent by a parser object to its delegate when it encounters a fatal error.
- [- parser:validationErrorOccurred:](<parser(__validationerroroccurred_).md>) — Sent by a parser object to its delegate when it encounters a fatal validation error. `NSXMLParser` currently does not invoke this method and does not perform validation.
- [- parser:foundCharacters:](<parser(__foundcharacters_).md>) — Sent by a parser object to provide its delegate with a string representing all or part of the characters of the current element.
- [- parser:foundIgnorableWhitespace:](<parser(__foundignorablewhitespace_).md>) — Reported by a parser object to provide its delegate with a string representing all or part of the ignorable whitespace characters of the current element.
- [- parser:foundProcessingInstructionWithTarget:data:](<parser(__foundprocessinginstructionwithtarget_data_).md>) — Sent by a parser object to its delegate when it encounters a processing instruction.
- [- parser:foundComment:](<parser(__foundcomment_).md>) — Sent by a parser object to its delegate when it encounters a comment in the XML.
- [- parser:foundCDATA:](<parser(__foundcdata_).md>) — Sent by a parser object to its delegate when it encounters a CDATA block.
