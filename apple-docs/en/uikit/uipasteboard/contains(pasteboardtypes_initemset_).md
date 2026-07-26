---
title: 'contains(pasteboardTypes:inItemSet:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/contains(pasteboardtypes:initemset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/contains(pasteboardtypes:initemset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/contains%28pasteboardtypes%3Ainitemset%3A%29.json'
content_hash: 'sha256:34ccba8292bd97d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# contains(pasteboardTypes:inItemSet:)

<sub>Instance Method</sub>

Returns whether the specified pasteboard items contain data of the given representation types.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func contains(pasteboardTypes: [String], inItemSet itemSet: IndexSet?) -> Bool
```

## Parameters

- `pasteboardTypes` — An array of strings, with each string identifying a representation type. Typically you use UTIs as pasteboard types.

- `itemSet` — An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in `nil` to request all pasteboard items.

## Return Value

[true](../../swift/true.md) if the pasteboard items identified by `itemSet` have data corresponding to the representation types specified by `pasteboardTypes`; otherwise, returns [false](../../swift/false.md).

## See Also

### Related Documentation

- [numberOfItems](numberofitems.md) — The number of items for the pasteboard.

### Determining types of pasteboard items

- [pasteboardTypes](types.md) — The types of the first item on the pasteboard.
- [- pasteboardTypesForItemSet:](<types(foritemset_).md>) — Returns an array of representation types for each specified pasteboard item.
- [- containsPasteboardTypes:](<contains(pasteboardtypes_).md>) — Returns whether the pasteboard holds data of the specified representation type.
- [- itemSetWithPasteboardTypes:](<itemset(withpasteboardtypes_).md>) — Returns an index set identifying pasteboard items having the specified representation types.
