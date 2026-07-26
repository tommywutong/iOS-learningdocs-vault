---
title: 'init(data:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparser/init(data:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/init%28data%3A%29.json'
content_hash: 'sha256:fafb56eeb6e0a713'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# init(data:)

<sub>Initializer</sub>

Initializes a parser with the XML contents encapsulated in a given data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(data: Data)
```

## Parameters

- `data` — An [NSData](../nsdata.md) object containing XML markup.

## Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

## Discussion

This method is the designated initializer.

## See Also

### Initializing a Parser Object

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes a parser with the XML content referenced by the given URL.
- [- initWithStream:](<init(stream_).md>) — Initializes a parser with the XML contents from the specified stream and parses it.
