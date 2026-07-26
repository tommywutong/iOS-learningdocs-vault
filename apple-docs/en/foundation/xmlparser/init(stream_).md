---
title: 'init(stream:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparser/init(stream:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/init(stream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/init%28stream%3A%29.json'
content_hash: 'sha256:4043451c8393b54f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# init(stream:)

<sub>Initializer</sub>

Initializes a parser with the XML contents from the specified stream and parses it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(stream: InputStream)
```

## Parameters

- `stream` — The input stream. The content is incrementally loaded from the specified stream and parsed. The `NSXMLParser` will open the stream, and synchronously read from it without scheduling it.

## Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

## See Also

### Initializing a Parser Object

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Initializes a parser with the XML content referenced by the given URL.
- [- initWithData:](<init(data_).md>) — Initializes a parser with the XML contents encapsulated in a given data object.
