---
title: suggestedName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/suggestedname
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/suggestedname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/suggestedname.json'
content_hash: 'sha256:38555c511a9d3f17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# suggestedName

<sub>Instance Property</sub>

The filename to use when writing the provided data to a file on disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var suggestedName: String? { get set }
```

## Discussion

Setting this property is recommended when providing [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169) or text data from an item provider.

## See Also

### Configuring the provider

- [preferredPresentationSize](preferredpresentationsize.md) — The ideal presentation size of the item.
- [preferredPresentationStyle](preferredpresentationstyle-swift.property.md) — The preferred style for presenting the item provider’s data.
- [PreferredPresentationStyle](preferredpresentationstyle-swift.enum.md) — The presentation styles that determine how a view shows an item provider’s data.
- [teamData](teamdata.md) — The collection of data an app uses to hold private team information during drag and drop.
