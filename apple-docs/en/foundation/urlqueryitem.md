---
title: URLQueryItem
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlqueryitem
source_url: 'https://developer.apple.com/documentation/foundation/urlqueryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlqueryitem.json'
content_hash: 'sha256:4b7c0de78107da7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLQueryItem

<sub>Structure</sub>

A single name-value pair from the query portion of a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLQueryItem
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Query Items

- [init(name:value:)](<urlqueryitem/init(name_value_).md>) — Creates a new query item with the name and value you specify.

### Accessing the Item’s Components

- [name](urlqueryitem/name.md) — The name of the query item.
- [value](urlqueryitem/value.md) — The value for the query item.

### Using Reference Types

- [NSURLQueryItem](nsurlqueryitem.md) — An object representing a single name/value pair for an item in the query portion of a URL.

## See Also

### URLs

- [URL](url.md) — A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.
- [URLComponents](urlcomponents.md) — A structure that parses URLs into and constructs URLs from their constituent parts.
