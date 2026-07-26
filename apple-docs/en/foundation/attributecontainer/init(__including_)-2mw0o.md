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
doc_path: '/documentation/foundation/attributecontainer/init(_:including:)-2mw0o'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/init(_:including:)-2mw0o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/init%28_%3Aincluding%3A%29-2mw0o.json'
content_hash: 'sha256:ff18e706b06d19ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# init(_:including:)

<sub>Initializer</sub>

Creates an attribute container from a dictionary and an attribute scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ dictionary: [NSAttributedString.Key : Any], including scope: S.Type) throws where S : AttributeScope
```

## Parameters

- `dictionary` — A dictionary of attribute keys and their values.

- `scope` — The attribute scope of the dictionary keys. This can be a nested scope that contains several scopes.

## Discussion

This initializer only collects attributes from `dictionary` that exist in the provided scope. The resulting attribute container omits any keys in `dictionary` that don’t exist in `scope`.

## See Also

### Creating an Attribute Container

- [init()](<init().md>) — Creates an empty attribute container.
- [init(_:including:)](<init(__including_)-28n0g.md>) — Creates an attribute container from a dictionary and an attribute scope that a key path identifies.
- [init(_:)](<init(__).md>) — Creates an attribute container from a dictionary, using default attribute scopes.
