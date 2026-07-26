---
title: DecodingError.Context
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/decodingerror/context
source_url: 'https://developer.apple.com/documentation/swift/decodingerror/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/decodingerror/context.json'
content_hash: 'sha256:520329b427857812'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DecodingError](../decodingerror.md)

# DecodingError.Context

<sub>Structure</sub>

The context in which the error occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Context
```

## Relationships

- **Conforms To**: [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Initializers

- [init(codingPath:debugDescription:underlyingError:)](<context/init(codingpath_debugdescription_underlyingerror_).md>) — Creates a new context with the given path of coding keys and a description of what went wrong.

### Instance Properties

- [codingPath](context/codingpath.md) — The path of coding keys taken to get to the point of the failing decode call.
- [debugDescription](context/debugdescription.md) — A description of what went wrong, for debugging purposes.
- [underlyingError](context/underlyingerror.md) — The underlying error which caused this error, if any.
