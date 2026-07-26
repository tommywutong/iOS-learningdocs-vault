---
title: 'contains(pasteboardTypes:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/contains(pasteboardtypes:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/contains(pasteboardtypes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/contains%28pasteboardtypes%3A%29.json'
content_hash: 'sha256:97df1f629be19b62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# contains(pasteboardTypes:)

<sub>Instance Method</sub>

Returns whether the pasteboard holds data of the specified representation type.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func contains(pasteboardTypes: [String]) -> Bool
```

## Parameters

- `pasteboardTypes` — An array of strings. Each string should identify a representation of the pasteboard item that the pasteboard reader can handle. These string are frequently UTIs. See the class description for more information about pasteboard item types.

## Return Value

[true](../../swift/true.md) if the pasteboard item holds data of the indicated representation type, otherwise [false](../../swift/false.md).

## Discussion

This method works on the first item in the pasteboard. If there are other items, it ignores them. You can use this method when enabling or disabling the Paste menu command.

Starting in iOS 10, you can directly check which data types are present on a pasteboard by using the convenience methods described in Checking for data types on a pasteboard.

## See Also

### Determining types of pasteboard items

- [pasteboardTypes](types.md) — The types of the first item on the pasteboard.
- [- pasteboardTypesForItemSet:](<types(foritemset_).md>) — Returns an array of representation types for each specified pasteboard item.
- [- containsPasteboardTypes:inItemSet:](<contains(pasteboardtypes_initemset_).md>) — Returns whether the specified pasteboard items contain data of the given representation types.
- [- itemSetWithPasteboardTypes:](<itemset(withpasteboardtypes_).md>) — Returns an index set identifying pasteboard items having the specified representation types.
