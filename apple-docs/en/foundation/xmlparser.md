---
title: XMLParser
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser.json'
content_hash: 'sha256:e5ce755659df2b37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# XMLParser

<sub>Class</sub>

An event driven parser of XML documents (including DTD declarations).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class XMLParser
```

## Overview

An [XMLParser](xmlparser.md) notifies its delegate about the items (elements, attributes, CDATA blocks, comments, and so on) that it encounters as it processes an XML document. It does not itself do anything with those parsed items except report them. It also reports parsing errors. For convenience, an [XMLParser](xmlparser.md) object in the following descriptions is sometimes referred to as a parser object. Unless used in a callback, the [XMLParser](xmlparser.md) is a thread-safe class as long as any given instance is only used in one thread.

> [!note] Note
> Namespace support was implemented in [XMLParser](xmlparser.md) starting in macOS 10.4. Namespace-related methods of [XMLParser](xmlparser.md) prior to this version have no effect.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Parser Object

- [- initWithContentsOfURL:](<xmlparser/init(contentsof_).md>) — Initializes a parser with the XML content referenced by the given URL.
- [- initWithData:](<xmlparser/init(data_).md>) — Initializes a parser with the XML contents encapsulated in a given data object.
- [- initWithStream:](<xmlparser/init(stream_).md>) — Initializes a parser with the XML contents from the specified stream and parses it.

### Managing Delegates

- [delegate](xmlparser/delegate.md) — A delegate object that receives messages about the parsing process.

### Managing Parser Behavior

- [shouldProcessNamespaces](xmlparser/shouldprocessnamespaces.md) — A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [shouldReportNamespacePrefixes](xmlparser/shouldreportnamespaceprefixes.md) — A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.
- [shouldResolveExternalEntities](xmlparser/shouldresolveexternalentities.md) — A Boolean value that determines whether the parser reports declarations of external entities.

### Parsing

- [- parse](<xmlparser/parse().md>) — Starts the event-driven parsing operation.
- [- abortParsing](<xmlparser/abortparsing().md>) — Stops the parser object.
- [parserError](xmlparser/parsererror.md) — An [NSError](nserror.md) object from which you can obtain information about a parsing error.

### Obtaining Parser State

- [columnNumber](xmlparser/columnnumber.md) — The column number of the XML document being processed by the parser.
- [lineNumber](xmlparser/linenumber.md) — The line number of the XML document being processed by the parser.
- [publicID](xmlparser/publicid.md) — The public identifier of the external entity referenced in the XML document.
- [systemID](xmlparser/systemid.md) — The system identifier of the external entity referenced in the XML document.

### Constants

- [ExternalEntityResolvingPolicy](xmlparser/externalentityresolvingpolicy-swift.enum.md) — Defines the external entity resolving policy used by an `NSXMLParser` instance.
- [NSXMLParserErrorDomain](xmlparser/errordomain.md) — Indicates an error in XML parsing.
- [ErrorCode](xmlparser/errorcode.md) — The following error codes are defined by `NSXMLParser`. For error codes not listed here, see the `<libxml/xmlerror.h>` header file.

### Initializers

- [init(contentsOfURL:)](<xmlparser/init(contentsofurl_).md>)

### Instance Properties

- [allowedExternalEntityURLs](xmlparser/allowedexternalentityurls.md) — The set of external entity URLs that the parser is allowed to load.
- [externalEntityResolvingPolicy](xmlparser/externalentityresolvingpolicy-swift.property.md) — The external entity resolving policy for the parser.

## See Also

### Event-Based Processing

- [XMLParserDelegate](xmlparserdelegate.md) — The interface an XML parser uses to inform its delegate about the content of the parsed document.
