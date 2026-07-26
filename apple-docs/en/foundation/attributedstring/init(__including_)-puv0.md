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
doc_path: '/documentation/foundation/attributedstring/init(_:including:)-puv0'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(_:including:)-puv0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28_%3Aincluding%3A%29-puv0.json'
content_hash: 'sha256:a380d4b84eff1e34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(_:including:)

<sub>Initializer</sub>

Creates a value-type attributed string from a reference type, including an attribute scope that a key path identifies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ nsStr: NSAttributedString, including scope: KeyPath<AttributeScopes, S.Type>) throws where S : AttributeScope
```

## Parameters

- `nsStr` — The [NSAttributedString](../nsattributedstring.md) to convert.

- `scope` — A key path that identifies the attribute scope of the attributes in `nsStr`. This can be a nested scope that contains several scopes.

## Discussion

This initializer only collects attributes from `nsStr` that exist in the provided scope. The resulting attributed string omits any keys in `nsStr` that don’t exist in `scope`.

## See Also

### Creating an Attributed String from a Reference Type

- [init(_:including:)](<init(__including_)-9no47.md>) — Creates a value-type attributed string from a reference type, including an attribute scope.
- [init(_:)](<init(__)-1fru0.md>) — Creates a value-type attributed string from a reference type.
