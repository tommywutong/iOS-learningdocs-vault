---
title: 'init(contentsOf:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/init(contentsof:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/init(contentsof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/init%28contentsof%3A%29.json'
content_hash: 'sha256:08c75a0ed8c692ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# init(contentsOf:)

<sub>Initializer</sub>

Provides data-backed content from an existing file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(contentsOf fileURL: URL!)
```

## Parameters

- `fileURL` — The URL of the file to use for the item provider’s data. The item provider uses the filename extension to determine the universal type identifier for the associated data.

## Return Value

An item provider for the specified file, or `nil` if an error occurs.

## Discussion

The system uses the URL’s filename extension to select an appropriate universal type identifier. If the system can’t determine a specific universal type identifier based on the filename extension, it assigns the `public.data` universal type identifier for the file.

## See Also

### Related Documentation

- [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)

### Creating an item provider

- [init(contentsOf:contentType:openInPlace:coordinated:visibility:)](<init(contentsof_contenttype_openinplace_coordinated_visibility_).md>) — Provides data-backed content from an existing file with the specified parameters.
- [- initWithItem:typeIdentifier:](<init(item_typeidentifier_).md>) — Creates an item provider with an object, according to the item provider type coercion policy. _(deprecated)_
- [- init](<init().md>) — Creates an empty item provider to which you can later register a data or file representation.
- [- initWithObject:](<init(object_).md>) — Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.
