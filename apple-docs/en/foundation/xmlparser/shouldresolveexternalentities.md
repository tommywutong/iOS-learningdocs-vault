---
title: shouldResolveExternalEntities
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/shouldresolveexternalentities
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/shouldresolveexternalentities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/shouldresolveexternalentities.json'
content_hash: 'sha256:b4dd25ce6a09b909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# shouldResolveExternalEntities

<sub>Instance Property</sub>

A Boolean value that determines whether the parser reports declarations of external entities.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldResolveExternalEntities: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the parser reports declarations of external entities, [false](../../swift/false.md) otherwise. The default value is [false](../../swift/false.md). If you set this property to [true](../../swift/true.md), you may cause other I/O operations, either network-based or disk-based, to load the external DTD.

The parser reports declarations of external entities with the delegate method [- parser:foundExternalEntityDeclarationWithName:publicID:systemID:](<../xmlparserdelegate/parser(__foundexternalentitydeclarationwithname_publicid_systemid_).md>).

## See Also

### Managing Parser Behavior

- [shouldProcessNamespaces](shouldprocessnamespaces.md) — A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [shouldReportNamespacePrefixes](shouldreportnamespaceprefixes.md) — A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.
