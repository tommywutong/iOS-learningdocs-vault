---
title: 'init(item:typeIdentifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsitemprovider/init(item:typeidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/init(item:typeidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/init%28item%3Atypeidentifier%3A%29.json'
content_hash: 'sha256:68231b84fdcbe80b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# init(item:typeIdentifier:)

<sub>Initializer</sub>

Creates an item provider with an object, according to the item provider type coercion policy.

> [!warning] Deprecated
> Use initWithObject: instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(item: (any NSSecureCoding)?, typeIdentifier: String?)
```

## Parameters

- `item` — An object containing the data you want to provide. You may specify `nil` for this parameter and register items and types later.

- `typeIdentifier` — A string that represents the UTI of the item. If `item` is not `nil`, this parameter must not be `nil`.

## Return Value

An item provider for the specified item.

## Discussion

Use this method to initialize an item provider for objects in your app. The item provider registers your object with the specified type. Subsequent requests for that same type return the specified `item`.

## See Also

### Creating an item provider

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Provides data-backed content from an existing file.
- [init(contentsOf:contentType:openInPlace:coordinated:visibility:)](<init(contentsof_contenttype_openinplace_coordinated_visibility_).md>) — Provides data-backed content from an existing file with the specified parameters.
- [- init](<init().md>) — Creates an empty item provider to which you can later register a data or file representation.
- [- initWithObject:](<init(object_).md>) — Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.
