---
title: items
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragdropsession/items
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession/items.json'
content_hash: 'sha256:f334289a801742cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragDropSession](../uidragdropsession.md)

# items

<sub>Instance Property</sub>

An array of drag items in the drag session or drop session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var items: [UIDragItem] { get }
```

## Discussion

The drag item’s [NSItemProvider](../../foundation/nsitemprovider.md) object doesn’t load the data for the item until the drop interaction happens. However, before the interaction happens, you can get the item’s registered type identifiers and metadata. The data is available to you only in the drop interaction delegate’s [- dropInteraction:performDrop:](<../uidropinteractiondelegate/dropinteraction(__performdrop_).md>) method.

## See Also

### Checking for drag items

- [- canLoadObjectsOfClass:](<canloadobjects(ofclass_).md>) — Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.
- [- hasItemsConformingToTypeIdentifiers:](<hasitemsconforming(totypeidentifiers_).md>) — Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.
