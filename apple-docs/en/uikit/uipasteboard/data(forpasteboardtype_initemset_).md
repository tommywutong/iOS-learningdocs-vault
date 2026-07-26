---
title: 'data(forPasteboardType:inItemSet:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/data(forpasteboardtype:initemset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/data(forpasteboardtype:initemset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/data%28forpasteboardtype%3Ainitemset%3A%29.json'
content_hash: 'sha256:02672fae969680a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# data(forPasteboardType:inItemSet:)

<sub>Instance Method</sub>

Returns the data objects in the indicated pasteboard items that have the given representation type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func data(forPasteboardType pasteboardType: String, inItemSet itemSet: IndexSet?) -> [Data]?
```

## Parameters

- `pasteboardType` — A string identifying a representation type. Typically this is a UTI.

- `itemSet` — An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in `nil` to request all pasteboard items.

## Return Value

An array of [NSData](../../foundation/nsdata.md) objects or, if a requested pasteboard item has no data of the the type indicated by `pasteboardType`, a [NSNull](../../foundation/nsnull.md) object.

## See Also

### Getting and setting pasteboard items

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.
- [items](items.md) — The pasteboard items on the pasteboard.
- [- addItems:](<additems(__).md>) — Appends pasteboard items to the current contents of the pasteboard.
- [- setItems:options:](<setitems(__options_).md>) — Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [- dataForPasteboardType:](<data(forpasteboardtype_).md>) — Returns the data on the pasteboard for the given representation type.
- [- setData:forPasteboardType:](<setdata(__forpasteboardtype_).md>) — Puts data on the pasteboard for the specified representation type.
- [- valueForPasteboardType:](<value(forpasteboardtype_).md>) — Returns an object on the pasteboard for the given representation type.
- [- valuesForPasteboardType:inItemSet:](<values(forpasteboardtype_initemset_).md>) — Returns the objects on the indicated pasteboard items that have the given representation type.
- [- setValue:forPasteboardType:](<setvalue(__forpasteboardtype_).md>) — Puts an object on the pasteboard for the specified representation type.
