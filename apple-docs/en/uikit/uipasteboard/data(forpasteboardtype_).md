---
title: 'data(forPasteboardType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/data(forpasteboardtype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/data(forpasteboardtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/data%28forpasteboardtype%3A%29.json'
content_hash: 'sha256:d66865d163f8a990'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# data(forPasteboardType:)

<sub>Instance Method</sub>

Returns the data on the pasteboard for the given representation type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func data(forPasteboardType pasteboardType: String) -> Data?
```

## Parameters

- `pasteboardType` — A string identifying a representation type of a pasteboard item.

## Return Value

A data object or `nil` if there is no data in the pasteboard of the given type.

## Discussion

The returned object often holds raw (binary) data, such as image data. This method works on the first item in the pasteboard. If there are other items, it ignores them.

## See Also

### Getting and setting pasteboard items

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.
- [items](items.md) — The pasteboard items on the pasteboard.
- [- addItems:](<additems(__).md>) — Appends pasteboard items to the current contents of the pasteboard.
- [- setItems:options:](<setitems(__options_).md>) — Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [- dataForPasteboardType:inItemSet:](<data(forpasteboardtype_initemset_).md>) — Returns the data objects in the indicated pasteboard items that have the given representation type.
- [- setData:forPasteboardType:](<setdata(__forpasteboardtype_).md>) — Puts data on the pasteboard for the specified representation type.
- [- valueForPasteboardType:](<value(forpasteboardtype_).md>) — Returns an object on the pasteboard for the given representation type.
- [- valuesForPasteboardType:inItemSet:](<values(forpasteboardtype_initemset_).md>) — Returns the objects on the indicated pasteboard items that have the given representation type.
- [- setValue:forPasteboardType:](<setvalue(__forpasteboardtype_).md>) — Puts an object on the pasteboard for the specified representation type.
