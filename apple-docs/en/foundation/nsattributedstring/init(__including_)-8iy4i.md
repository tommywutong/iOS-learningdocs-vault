---
title: 'init(_:including:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(_:including:)-8iy4i'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(_:including:)-8iy4i'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28_%3Aincluding%3A%29-8iy4i.json'
content_hash: 'sha256:137112d86fd02612'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(_:including:)

<sub>Initializer</sub>

Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope that a key path identifies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init<S>(_ attrStr: AttributedString, including scope: KeyPath<AttributeScopes, S.Type>) throws where S : AttributeScope
```

## Parameters

- `attrStr` — The value-type attributed string that provides the text and attributes of the new object.

- `scope` — A key path that identifies the attribute scope of the attributes in `attrStr`. This can be a nested scope that contains several scopes.

## See Also

### Creating a formatted string

- [init(_:)](<init(__).md>) — Creates a reference-type attributed string from the specified value-type attributed string.
- [init(_:including:)](<init(__including_)-9gogq.md>) — Creates a reference-type attributed string from the specified value-type attributed string, including an attribute scope.
