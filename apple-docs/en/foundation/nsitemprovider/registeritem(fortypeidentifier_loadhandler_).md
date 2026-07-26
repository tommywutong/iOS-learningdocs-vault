---
title: 'registerItem(forTypeIdentifier:loadHandler:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsitemprovider/registeritem(fortypeidentifier:loadhandler:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/registeritem(fortypeidentifier:loadhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/registeritem%28fortypeidentifier%3Aloadhandler%3A%29.json'
content_hash: 'sha256:54c8faf9fca9f39b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# registerItem(forTypeIdentifier:loadHandler:)

<sub>Instance Method</sub>

Lazily registers an item, according to the item provider type coercion policy.

> [!warning] Deprecated
> Use registerObjectOfClass:visibility:loadHandler: instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func registerItem(forTypeIdentifier typeIdentifier: String, loadHandler: @escaping NSItemProvider.LoadHandler)
```

## Parameters

- `typeIdentifier` — A string that represents the desired UTI.

- `loadHandler` — A block capable of returning the data item as the specified type. For information about implementing this block, see [LoadHandler](loadhandler.md).

## Discussion

Use this method to register blocks that can take the item provider’s file or data object and convert it to a specific data format. Your `loadHandler` block is executed when a client passes the same `typeIdentifier` string to the [- loadItemForTypeIdentifier:options:completionHandler:](<loaditem(fortypeidentifier_options_completionhandler_).md>) method. In the implementation of your block, coerce the data to the specified type and call the provided completion handler. You must call the completion handler, either with the requested data or with an error.

Item providers know how to coerce known types of objects, such as images or strings. Use this method to register blocks to coerce your custom data types.

## See Also

### Registering data

- [- registerDataRepresentationForTypeIdentifier:visibility:loadHandler:](<registerdatarepresentation(fortypeidentifier_visibility_loadhandler_).md>) — Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [registerDataRepresentation(for:visibility:loadHandler:)](<registerdatarepresentation(for_visibility_loadhandler_).md>) — Registers a data-backed representation for an item, specifiying item visibility and a load handler.
