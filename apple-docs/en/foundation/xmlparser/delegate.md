---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlparser/delegate
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/delegate.json'
content_hash: 'sha256:bbfe999ad79a900f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# delegate

<sub>Instance Property</sub>

A delegate object that receives messages about the parsing process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var delegate: (any XMLParserDelegate)? { get set }
```

## Discussion

For methods to be implemented by the delegate, see [XMLParserDelegate](../xmlparserdelegate.md).
