---
title: 'setData(_:forPasteboardType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/setdata(_:forpasteboardtype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/setdata(_:forpasteboardtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/setdata%28_%3Aforpasteboardtype%3A%29.json'
content_hash: 'sha256:39e419afc5c98a26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# setData(_:forPasteboardType:)

<sub>Instance Method</sub>

Puts data on the pasteboard for the specified representation type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setData(_ data: Data, forPasteboardType pasteboardType: String)
```

## Parameters

- `data` — The data object to be written to the pasteboard.

- `pasteboardType` — A string identifying the representation type of the pasteboard item. This is typically a UTI.

## Discussion

Use this method to put raw data on the pasteboard. For example, you could archive a graph of model objects and pass the resulting [NSData](../../foundation/nsdata.md) object to a related app via a pasteboard using a custom pasteboard type. (To put objects—such as [NSString](../../foundation/nsstring.md), [NSArray](../../foundation/nsarray.md), [NSDictionary](../../foundation/nsdictionary.md), [NSDate](../../foundation/nsdate.md), [NSNumber](../../foundation/nsnumber.md), [UIImage](../uiimage.md), or [NSURL](../../foundation/nsurl.md) objects—on the pasteboard, use the [- setValue:forPasteboardType:](<setvalue(__forpasteboardtype_).md>) method.) This method writes data for the first item in the pasteboard. Calling this method replaces any items currently in the pasteboard.

## See Also

### Getting and setting pasteboard items

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.
- [items](items.md) — The pasteboard items on the pasteboard.
- [- addItems:](<additems(__).md>) — Appends pasteboard items to the current contents of the pasteboard.
- [- setItems:options:](<setitems(__options_).md>) — Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [- dataForPasteboardType:](<data(forpasteboardtype_).md>) — Returns the data on the pasteboard for the given representation type.
- [- dataForPasteboardType:inItemSet:](<data(forpasteboardtype_initemset_).md>) — Returns the data objects in the indicated pasteboard items that have the given representation type.
- [- valueForPasteboardType:](<value(forpasteboardtype_).md>) — Returns an object on the pasteboard for the given representation type.
- [- valuesForPasteboardType:inItemSet:](<values(forpasteboardtype_initemset_).md>) — Returns the objects on the indicated pasteboard items that have the given representation type.
- [- setValue:forPasteboardType:](<setvalue(__forpasteboardtype_).md>) — Puts an object on the pasteboard for the specified representation type.
