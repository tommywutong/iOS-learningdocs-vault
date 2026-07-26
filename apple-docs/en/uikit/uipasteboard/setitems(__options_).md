---
title: 'setItems(_:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/setitems(_:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/setitems(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/setitems%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:e7f8166815578781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# setItems(_:options:)

<sub>Instance Method</sub>

Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setItems(_ items: [[String : Any]], options: [UIPasteboard.OptionsKey : Any] = [:])
```

## Parameters

- `items` — An array of items to add to the pasteboard.

- `options` — The privacy options to apply to all the items on the pasteboard. The available options are described in [OptionsKey](optionskey.md).

## See Also

### Getting and setting pasteboard items

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.
- [items](items.md) — The pasteboard items on the pasteboard.
- [- addItems:](<additems(__).md>) — Appends pasteboard items to the current contents of the pasteboard.
- [- dataForPasteboardType:](<data(forpasteboardtype_).md>) — Returns the data on the pasteboard for the given representation type.
- [- dataForPasteboardType:inItemSet:](<data(forpasteboardtype_initemset_).md>) — Returns the data objects in the indicated pasteboard items that have the given representation type.
- [- setData:forPasteboardType:](<setdata(__forpasteboardtype_).md>) — Puts data on the pasteboard for the specified representation type.
- [- valueForPasteboardType:](<value(forpasteboardtype_).md>) — Returns an object on the pasteboard for the given representation type.
- [- valuesForPasteboardType:inItemSet:](<values(forpasteboardtype_initemset_).md>) — Returns the objects on the indicated pasteboard items that have the given representation type.
- [- setValue:forPasteboardType:](<setvalue(__forpasteboardtype_).md>) — Puts an object on the pasteboard for the specified representation type.
