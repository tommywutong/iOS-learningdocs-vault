---
title: 'init(contentsOf:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlparser/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlparser/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlparser/init%28contentsof%3A%29.json'
content_hash: 'sha256:733fb0df738dae66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLParser](../xmlparser.md)

# init(contentsOf:)

<sub>Initializer</sub>

Initializes a parser with the XML content referenced by the given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOf url: URL)
```

## Parameters

- `url` — An [NSURL](../nsurl.md) object specifying a URL. The URL must be fully qualified and refer to a scheme that is supported by the `NSURL` class.

## Return Value

An initialized `NSXMLParser` object or `nil` if an error occurs.

## See Also

### Related Documentation

- [Event-Driven XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/XMLParsing.html#//apple_ref/doc/uid/10000186i)

### Initializing a Parser Object

- [- initWithData:](<init(data_).md>) — Initializes a parser with the XML contents encapsulated in a given data object.
- [- initWithStream:](<init(stream_).md>) — Initializes a parser with the XML contents from the specified stream and parses it.
