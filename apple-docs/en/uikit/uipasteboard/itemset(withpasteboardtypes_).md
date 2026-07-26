---
title: 'itemSet(withPasteboardTypes:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/itemset(withpasteboardtypes:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/itemset(withpasteboardtypes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/itemset%28withpasteboardtypes%3A%29.json'
content_hash: 'sha256:a8ad71a851135bc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# itemSet(withPasteboardTypes:)

<sub>Instance Method</sub>

Returns an index set identifying pasteboard items having the specified representation types.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func itemSet(withPasteboardTypes pasteboardTypes: [String]) -> IndexSet?
```

## Parameters

- `pasteboardTypes` — An array of strings, with each string identifying a representation type. Typically you use UTIs as pasteboard types.

## Return Value

An index set with each integer positionally identifying a pasteboard item that has one of the representation types specified in `pasteboardTypes`.

## Discussion

You can pass the index set returned in this method in a call to [- dataForPasteboardType:inItemSet:](<data(forpasteboardtype_initemset_).md>) or [- valuesForPasteboardType:inItemSet:](<values(forpasteboardtype_initemset_).md>) to get the data in the indicated pasteboard items.

## See Also

### Related Documentation

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.

### Determining types of pasteboard items

- [pasteboardTypes](types.md) — The types of the first item on the pasteboard.
- [- pasteboardTypesForItemSet:](<types(foritemset_).md>) — Returns an array of representation types for each specified pasteboard item.
- [- containsPasteboardTypes:](<contains(pasteboardtypes_).md>) — Returns whether the pasteboard holds data of the specified representation type.
- [- containsPasteboardTypes:inItemSet:](<contains(pasteboardtypes_initemset_).md>) — Returns whether the specified pasteboard items contain data of the given representation types.
