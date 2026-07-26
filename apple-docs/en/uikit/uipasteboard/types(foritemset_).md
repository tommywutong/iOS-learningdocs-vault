---
title: 'types(forItemSet:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/types(foritemset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/types(foritemset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/types%28foritemset%3A%29.json'
content_hash: 'sha256:f3a9c4fb735bb9b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# types(forItemSet:)

<sub>Instance Method</sub>

Returns an array of representation types for each specified pasteboard item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func types(forItemSet itemSet: IndexSet?) -> [[String]]?
```

## Parameters

- `itemSet` — An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in `nil` to request all pasteboard items.

## Return Value

An array of arrays, with each inner array holding the representation types for a particular pasteboard item.

## See Also

### Related Documentation

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.

### Determining types of pasteboard items

- [pasteboardTypes](types.md) — The types of the first item on the pasteboard.
- [- containsPasteboardTypes:](<contains(pasteboardtypes_).md>) — Returns whether the pasteboard holds data of the specified representation type.
- [- containsPasteboardTypes:inItemSet:](<contains(pasteboardtypes_initemset_).md>) — Returns whether the specified pasteboard items contain data of the given representation types.
- [- itemSetWithPasteboardTypes:](<itemset(withpasteboardtypes_).md>) — Returns an index set identifying pasteboard items having the specified representation types.
