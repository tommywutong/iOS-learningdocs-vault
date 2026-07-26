---
title: writableTypeIdentifiersForItemProvider
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.property.json'
content_hash: 'sha256:2bdf13a56e01b2fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProviderWriting](../nsitemproviderwriting.md)

# writableTypeIdentifiersForItemProvider

<sub>Instance Property</sub>

An array of UTI strings representing the types of data that can be loaded for an item provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional var writableTypeIdentifiersForItemProvider: [String] { get }
```

## Discussion

Provide uniform type identifiers (UTIs) in order from highest fidelity to lowest. If your app employs a native data representation, place that first in the array.

Use the instance version of this property when you initialize an item provider with an object. As possible, implement this property to provide an extended array of UTIs based on the object. For example, for an [NSURL](../nsurl.md) object, your implementation could offer the `public.file-url` UTI, in addition to the `public.url` UTI, if your implementation detects that the stored URL uses the `file://` scheme.

## See Also

### Getting the writable type identifiers

- [writableTypeIdentifiersForItemProvider](writabletypeidentifiersforitemprovider-swift.type.property.md) — An array of UTI strings representing the types of data that can be loaded for an item provider.
