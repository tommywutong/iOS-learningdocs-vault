---
title: 'init(contentsOf:contentType:openInPlace:coordinated:visibility:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemprovider/init(contentsof:contenttype:openinplace:coordinated:visibility:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/init(contentsof:contenttype:openinplace:coordinated:visibility:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/init%28contentsof%3Acontenttype%3Aopeninplace%3Acoordinated%3Avisibility%3A%29.json'
content_hash: 'sha256:1f80cecff107d719'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# init(contentsOf:contentType:openInPlace:coordinated:visibility:)

<sub>Initializer</sub>

Provides data-backed content from an existing file with the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(contentsOf fileURL: URL, contentType: UTType?, openInPlace: Bool = false, coordinated: Bool = false, visibility: NSItemProviderRepresentationVisibility = .all)
```

## Parameters

- `fileURL` — The URL of the file to use for the item provider’s data.

- `contentType` — The content type of the specified file.

- `openInPlace` — `true` if the system opens the file in place.

- `coordinated` — `true` if the returned file must be accessed using [NSFileCoordinator](../nsfilecoordinator.md).

- `visibility` — The [NSItemProviderRepresentationVisibility](../nsitemproviderrepresentationvisibility.md) setting the system uses to identify which processes can see this content.

## Discussion

If [NSItemProviderFileOptionOpenInPlace](../nsitemproviderfileoptions/openinplace.md) is set to `false`, the system copies the file provided before the load handler returns.

## See Also

### Creating an item provider

- [- initWithContentsOfURL:](<init(contentsof_).md>) — Provides data-backed content from an existing file.
- [- initWithItem:typeIdentifier:](<init(item_typeidentifier_).md>) — Creates an item provider with an object, according to the item provider type coercion policy. _(deprecated)_
- [- init](<init().md>) — Creates an empty item provider to which you can later register a data or file representation.
- [- initWithObject:](<init(object_).md>) — Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.
