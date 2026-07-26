---
title: 'init(object:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/init(object:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/init(object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/init%28object%3A%29.json'
content_hash: 'sha256:8f062a60ad09d054'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# init(object:)

<sub>Initializer</sub>

Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(object: any NSItemProviderWriting)
```

## Parameters

- `object` — An object containing the data you want to provide.

## See Also

### Creating an item provider

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Provides data-backed content from an existing file.
- [init(contentsOf:contentType:openInPlace:coordinated:visibility:)](<init(contentsof_contenttype_openinplace_coordinated_visibility_).md>) — Provides data-backed content from an existing file with the specified parameters.
- [- initWithItem:typeIdentifier:](<init(item_typeidentifier_).md>) — Creates an item provider with an object, according to the item provider type coercion policy. _(deprecated)_
- [- init](<init().md>) — Creates an empty item provider to which you can later register a data or file representation.
