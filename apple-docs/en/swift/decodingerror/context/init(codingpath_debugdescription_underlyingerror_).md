---
title: 'init(codingPath:debugDescription:underlyingError:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/decodingerror/context/init(codingpath:debugdescription:underlyingerror:)'
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/context/init(codingpath:debugdescription:underlyingerror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/context/init%28codingpath%3Adebugdescription%3Aunderlyingerror%3A%29.json'
content_hash: 'sha256:839ea083d7f0901e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [DecodingError](../../decodingerror.md) · [Context](../context.md)

# init(codingPath:debugDescription:underlyingError:)

<sub>Initializer</sub>

Creates a new context with the given path of coding keys and a description of what went wrong.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(codingPath: [any CodingKey], debugDescription: String, underlyingError: (any Error)? = nil)
```

## Parameters

- `codingPath` — The path of coding keys taken to get to the point of the failing decode call.

- `debugDescription` — A description of what went wrong, for debugging purposes.

- `underlyingError` — The underlying error which caused this error, if any.
