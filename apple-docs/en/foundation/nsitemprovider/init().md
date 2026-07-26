---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/init()
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/init%28%29.json'
content_hash: 'sha256:c27409898a39f3af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# init()

<sub>Initializer</sub>

Creates an empty item provider to which you can later register a data or file representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## See Also

### Creating an item provider

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Provides data-backed content from an existing file.
- [init(contentsOf:contentType:openInPlace:coordinated:visibility:)](<init(contentsof_contenttype_openinplace_coordinated_visibility_).md>) — Provides data-backed content from an existing file with the specified parameters.
- [- initWithItem:typeIdentifier:](<init(item_typeidentifier_).md>) — Creates an item provider with an object, according to the item provider type coercion policy. _(deprecated)_
- [- initWithObject:](<init(object_).md>) — Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.
