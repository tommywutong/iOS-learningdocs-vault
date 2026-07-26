---
title: URL.ParseStrategy.ComponentParseStrategy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/parsestrategy/componentparsestrategy
source_url: 'https://developer.apple.com/documentation/foundation/url/parsestrategy/componentparsestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/parsestrategy/componentparsestrategy.json'
content_hash: 'sha256:66d8ecb803f3492b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [ParseStrategy](../parsestrategy.md)

# URL.ParseStrategy.ComponentParseStrategy

<sub>Enumeration</sub>

The strategy used to parse one component of a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ComponentParseStrategy<Component> where Component : Decodable, Component : Encodable, Component : Hashable, Component : Sendable
```

## Overview

Use this type with the [ParseStrategy](../parsestrategy.md) initializer and static accessors, or its modifier methods, to specify behavior for parsing components of a URL. This allows you to reject URL candidate strings that lack required components — such as a scheme, host, or path — or to fill in default values while parsing.

## Relationships

- **Conforms To**: [CustomStringConvertible](../../../swift/customstringconvertible.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Component parse strategies

- [URL.ParseStrategy.ComponentParseStrategy.required](componentparsestrategy/required.md) — A strategy that requires the presence of the associated component for parsing to succeed.
- [URL.ParseStrategy.ComponentParseStrategy.optional](componentparsestrategy/optional.md) — A strategy that treats the presence of the associated component as optional.
- [URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)](<componentparsestrategy/defaultvalue(__).md>) — A strategy that provides a default value for a component if it’s absent in the source string.

## See Also

### Creating a URL parse strategy

- [init(scheme:user:password:host:port:path:query:fragment:)](<init(scheme_user_password_host_port_path_query_fragment_).md>) — Creates a URL parse strategy with the specified component-parsing behaviors.
