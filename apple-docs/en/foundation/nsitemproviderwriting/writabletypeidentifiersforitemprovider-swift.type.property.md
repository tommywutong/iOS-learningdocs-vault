---
title: writableTypeIdentifiersForItemProvider
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.type.property
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.type.property.json'
content_hash: 'sha256:e6ed4527e524839a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProviderWriting](../nsitemproviderwriting.md)

# writableTypeIdentifiersForItemProvider

<sub>Type Property</sub>

An array of UTI strings representing the types of data that can be loaded for an item provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var writableTypeIdentifiersForItemProvider: [String] { get }
```

## Discussion

Provide uniform type identifiers (UTIs) in order from highest fidelity to lowest. If your app employs a native data representation, place that first in the array.

Implement this version of the property to offer a minimal list of UTIs that _all_ resulting item provider instances can support. For example, using this version of the property for an [NSURL](../nsurl.md) object, your implementation should return the `public.url` UTI but not `public.file-url`.

Use the class version of this property when you do not initialize an item provider with an object, thereby deferring the underlying object’s instantiation until the destination app needs it.

## See Also

### Getting the writable type identifiers

- [writableTypeIdentifiersForItemProvider](writabletypeidentifiersforitemprovider-swift.property.md) — An array of UTI strings representing the types of data that can be loaded for an item provider.
