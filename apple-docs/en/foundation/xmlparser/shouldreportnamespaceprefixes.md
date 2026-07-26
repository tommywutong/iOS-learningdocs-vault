---
title: shouldReportNamespacePrefixes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/shouldreportnamespaceprefixes
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/shouldreportnamespaceprefixes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/shouldreportnamespaceprefixes.json'
content_hash: 'sha256:b552a52ce8a9ef32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# shouldReportNamespacePrefixes

<sub>Instance Property</sub>

A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldReportNamespacePrefixes: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the parser reports the scope of namespace declarations, [false](../../swift/false.md) otherwise. The default value is [false](../../swift/false.md).

The parser reports prefixes with the delegate methods [- parser:didStartMappingPrefix:toURI:](<../xmlparserdelegate/parser(__didstartmappingprefix_touri_).md>) and [- parser:didEndMappingPrefix:](<../xmlparserdelegate/parser(__didendmappingprefix_).md>).

## See Also

### Managing Parser Behavior

- [shouldProcessNamespaces](shouldprocessnamespaces.md) — A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [shouldResolveExternalEntities](shouldresolveexternalentities.md) — A Boolean value that determines whether the parser reports declarations of external entities.
