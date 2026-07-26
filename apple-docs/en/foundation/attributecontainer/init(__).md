---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/init%28_%3A%29.json'
content_hash: 'sha256:81b7da6f90babab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# init(_:)

<sub>Initializer</sub>

Creates an attribute container from a dictionary, using default attribute scopes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ dictionary: [NSAttributedString.Key : Any])
```

## Parameters

- `dictionary` — A dictionary of attribute keys and their values.

## Discussion

This initializer includes all attribute scopes defined by the SDK, such as [FoundationAttributes](../attributescopes/foundationattributes.md), [SwiftUIAttributes](../attributescopes/swiftuiattributes.md), and [AccessibilityAttributes](../attributescopes/accessibilityattributes.md). To use third-party attribute scopes, use the initializers [init(_:including:)](<init(__including_)-2mw0o.md>) and [init(_:including:)](<init(__including_)-28n0g.md>).

## See Also

### Creating an Attribute Container

- [init()](<init().md>) — Creates an empty attribute container.
- [init(_:including:)](<init(__including_)-2mw0o.md>) — Creates an attribute container from a dictionary and an attribute scope.
- [init(_:including:)](<init(__including_)-28n0g.md>) — Creates an attribute container from a dictionary and an attribute scope that a key path identifies.
