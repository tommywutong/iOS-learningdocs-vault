---
title: numberOfItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/numberofitems
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/numberofitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/numberofitems.json'
content_hash: 'sha256:07fe5b39482d33c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# numberOfItems

<sub>Instance Property</sub>

The number of items for the pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var numberOfItems: Int { get }
```

## See Also

### Getting and setting pasteboard items

- [items](items.md) — The pasteboard items on the pasteboard.
- [- addItems:](<additems(__).md>) — Appends pasteboard items to the current contents of the pasteboard.
- [- setItems:options:](<setitems(__options_).md>) — Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [- dataForPasteboardType:](<data(forpasteboardtype_).md>) — Returns the data on the pasteboard for the given representation type.
- [- dataForPasteboardType:inItemSet:](<data(forpasteboardtype_initemset_).md>) — Returns the data objects in the indicated pasteboard items that have the given representation type.
- [- setData:forPasteboardType:](<setdata(__forpasteboardtype_).md>) — Puts data on the pasteboard for the specified representation type.
- [- valueForPasteboardType:](<value(forpasteboardtype_).md>) — Returns an object on the pasteboard for the given representation type.
- [- valuesForPasteboardType:inItemSet:](<values(forpasteboardtype_initemset_).md>) — Returns the objects on the indicated pasteboard items that have the given representation type.
- [- setValue:forPasteboardType:](<setvalue(__forpasteboardtype_).md>) — Puts an object on the pasteboard for the specified representation type.
