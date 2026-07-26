---
title: preferredPresentationSize
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/preferredpresentationsize
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/preferredpresentationsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/preferredpresentationsize.json'
content_hash: 'sha256:f7658721df8d777a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# preferredPresentationSize

<sub>Instance Property</sub>

The ideal presentation size of the item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredPresentationSize: CGSize { get set }
```

<sub>macOS</sub>

```swift
var preferredPresentationSize: NSSize { get }
```

## Discussion

When displaying the item, the value in this property represents the ideal size at which to display the item. The size in this property may differ from the size in the [sourceFrame](sourceframe.md) rectangle. For images, video, and other content with a natural size, the item automatically derives the size from that content. If the value in this property is [NSZeroSize](../nszerosize.md), use the size specified in the [sourceFrame](sourceframe.md) rectangle.

## See Also

### Configuring the provider

- [preferredPresentationStyle](preferredpresentationstyle-swift.property.md) — The preferred style for presenting the item provider’s data.
- [PreferredPresentationStyle](preferredpresentationstyle-swift.enum.md) — The presentation styles that determine how a view shows an item provider’s data.
- [suggestedName](suggestedname.md) — The filename to use when writing the provided data to a file on disk.
- [teamData](teamdata.md) — The collection of data an app uses to hold private team information during drag and drop.
