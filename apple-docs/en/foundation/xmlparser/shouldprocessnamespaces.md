---
title: shouldProcessNamespaces
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/shouldprocessnamespaces
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/shouldprocessnamespaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/shouldprocessnamespaces.json'
content_hash: 'sha256:26a8fe7e5ea3305d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# shouldProcessNamespaces

<sub>Instance Property</sub>

A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var shouldProcessNamespaces: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the parser reports namespace and qualified name, [false](../../swift/false.md) otherwise.

The parser reports element names with the delegate methods [- parser:didStartElement:namespaceURI:qualifiedName:attributes:](<../xmlparserdelegate/parser(__didstartelement_namespaceuri_qualifiedname_attributes_).md>) and [- parser:didEndElement:namespaceURI:qualifiedName:](<../xmlparserdelegate/parser(__didendelement_namespaceuri_qualifiedname_).md>).

## See Also

### Managing Parser Behavior

- [shouldReportNamespacePrefixes](shouldreportnamespaceprefixes.md) — A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.
- [shouldResolveExternalEntities](shouldresolveexternalentities.md) — A Boolean value that determines whether the parser reports declarations of external entities.
