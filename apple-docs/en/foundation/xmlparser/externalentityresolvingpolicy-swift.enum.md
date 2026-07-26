---
title: XMLParser.ExternalEntityResolvingPolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/externalentityresolvingpolicy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/externalentityresolvingpolicy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/externalentityresolvingpolicy-swift.enum.json'
content_hash: 'sha256:b71d3be5479d038a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# XMLParser.ExternalEntityResolvingPolicy

<sub>Enumeration</sub>

Defines the external entity resolving policy used by an `NSXMLParser` instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ExternalEntityResolvingPolicy
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSXMLParserResolveExternalEntitiesAlways](externalentityresolvingpolicy-swift.enum/always.md) — The parser always resolves external entities.
- [NSXMLParserResolveExternalEntitiesNever](externalentityresolvingpolicy-swift.enum/never.md) — The parser should never resolve external entities.
- [NSXMLParserResolveExternalEntitiesNoNetwork](externalentityresolvingpolicy-swift.enum/nonetwork.md) — The parser resolves external entities but does not load them over the network.
- [NSXMLParserResolveExternalEntitiesSameOriginOnly](externalentityresolvingpolicy-swift.enum/sameoriginonly.md) — The parser resolves external entities only from the same origin as the original URL. Only applies to `NSXMLParser` instances initialized with `-initWithContentsOfURL:`.
- [NSXMLParserResolveExternalEntitiesAlways](externalentityresolvingpolicy-swift.enum/always.md) — The parser always resolves external entities.
- [NSXMLParserResolveExternalEntitiesNever](externalentityresolvingpolicy-swift.enum/never.md) — The parser should never resolve external entities.
- [NSXMLParserResolveExternalEntitiesNoNetwork](externalentityresolvingpolicy-swift.enum/nonetwork.md) — The parser resolves external entities but does not load them over the network.
- [NSXMLParserResolveExternalEntitiesSameOriginOnly](externalentityresolvingpolicy-swift.enum/sameoriginonly.md) — The parser resolves external entities only from the same origin as the original URL. Only applies to `NSXMLParser` instances initialized with `-initWithContentsOfURL:`.

### Initializers

- [init(rawValue:)](<externalentityresolvingpolicy-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [NSXMLParserErrorDomain](errordomain.md) — Indicates an error in XML parsing.
- [ErrorCode](errorcode.md) — The following error codes are defined by `NSXMLParser`. For error codes not listed here, see the `<libxml/xmlerror.h>` header file.
