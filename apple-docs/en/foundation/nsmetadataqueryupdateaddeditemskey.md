---
title: NSMetadataQueryUpdateAddedItemsKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataqueryupdateaddeditemskey
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryupdateaddeditemskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryupdateaddeditemskey.json'
content_hash: 'sha256:859acac50add4290'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQueryUpdateAddedItemsKey

<sub>Global Variable</sub>

The key for retrieving an array of items added to the query result. By default, this array contains [NSMetadataItem](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSMetadataQueryUpdateAddedItemsKey: String
```

## See Also

### Constants

- [NSMetadataQueryUpdateChangedItemsKey](nsmetadataqueryupdatechangeditemskey.md) — The key for retrieving an array of items that have changed in the query result. By default, this array contains [NSMetadataItem](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.
- [NSMetadataQueryUpdateRemovedItemsKey](nsmetadataqueryupdateremoveditemskey.md) — The key for retrieving an array of items removed from the query result. By default, this array contains [NSMetadataItem](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.
