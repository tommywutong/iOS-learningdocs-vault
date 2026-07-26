---
title: preferredPresentationStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/preferredpresentationstyle-swift.property.json'
content_hash: 'sha256:b393b9eb9be748d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# preferredPresentationStyle

<sub>Instance Property</sub>

The preferred style for presenting the item provider’s data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredPresentationStyle: NSItemProvider.PreferredPresentationStyle { get set }
```

## Discussion

The default preferred presentation style is `unspecified`.

## See Also

### Configuring the provider

- [preferredPresentationSize](preferredpresentationsize.md) — The ideal presentation size of the item.
- [PreferredPresentationStyle](preferredpresentationstyle-swift.enum.md) — The presentation styles that determine how a view shows an item provider’s data.
- [suggestedName](suggestedname.md) — The filename to use when writing the provided data to a file on disk.
- [teamData](teamdata.md) — The collection of data an app uses to hold private team information during drag and drop.
