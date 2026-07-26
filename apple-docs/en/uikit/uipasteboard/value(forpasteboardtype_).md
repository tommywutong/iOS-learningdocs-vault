---
title: 'value(forPasteboardType:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/value(forpasteboardtype:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/value(forpasteboardtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/value%28forpasteboardtype%3A%29.json'
content_hash: 'sha256:8847e9fcb3f778ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# value(forPasteboardType:)

<sub>Instance Method</sub>

Returns an object on the pasteboard for the given representation type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func value(forPasteboardType pasteboardType: String) -> Any?
```

## Parameters

- `pasteboardType` — A string identifying a representation type of a pasteboard item.

## Return Value

An object that is an instance of the appropriate class based on `pasteboardType` or an [NSData](../../foundation/nsdata.md) object containing “raw” data.

## Discussion

This method attempts to return an object that is of a class type appropriate to the representation type, which typically is a UTI. For example, if the representation type is `kUTTypePlainText` (`public.plain-text`), the method returns an [NSString](../../foundation/nsstring.md) object. If the method can’t determine the class type from the representation type, it returns the object as a generic object, such as an [NSString](../../foundation/nsstring.md), [NSArray](../../foundation/nsarray.md), [NSDictionary](../../foundation/nsdictionary.md), [NSDate](../../foundation/nsdate.md), [NSNumber](../../foundation/nsnumber.md), [NSURL](../../foundation/nsurl.md), [UIImage](../uiimage.md), or [NSData](../../foundation/nsdata.md) object. This method works on the first item in the pasteboard. If there are other items, it ignores them.

## See Also

### Getting and setting pasteboard items

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.
- [items](items.md) — The pasteboard items on the pasteboard.
- [- addItems:](<additems(__).md>) — Appends pasteboard items to the current contents of the pasteboard.
- [- setItems:options:](<setitems(__options_).md>) — Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [- dataForPasteboardType:](<data(forpasteboardtype_).md>) — Returns the data on the pasteboard for the given representation type.
- [- dataForPasteboardType:inItemSet:](<data(forpasteboardtype_initemset_).md>) — Returns the data objects in the indicated pasteboard items that have the given representation type.
- [- setData:forPasteboardType:](<setdata(__forpasteboardtype_).md>) — Puts data on the pasteboard for the specified representation type.
- [- valuesForPasteboardType:inItemSet:](<values(forpasteboardtype_initemset_).md>) — Returns the objects on the indicated pasteboard items that have the given representation type.
- [- setValue:forPasteboardType:](<setvalue(__forpasteboardtype_).md>) — Puts an object on the pasteboard for the specified representation type.
