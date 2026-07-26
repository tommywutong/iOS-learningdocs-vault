---
title: types
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/types
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/types.json'
content_hash: 'sha256:dea9104883d190b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# types

<sub>Instance Property</sub>

The types of the first item on the pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var types: [String] { get }
```

## Return Value

An array of strings indicating the representation types of the first item on the pasteboard.

## Discussion

A type is frequently, but not necessarily, a UTI (Uniform Type Identifier). It identifies a representation of the data on the pasteboard. For example, a pasteboard item could hold image data under `public.png` and `public.tiff` representations. Apps can define their own types for custom data such as `com.mycompany.myapp.mytype`; however, in this case, only those apps that know of the type could understand the data written to the pasteboard.

With this method, you can determine if the pasteboard holds data of a particular representation type by a line of code such as this:

```objc
BOOL pngOnPasteboard = [[pasteboard pasteboardTypes] containsObject:@"public.png"];
```

Starting in iOS 10, you can directly check which data types are present on a pasteboard by using the convenience methods described in Checking for data types on a pasteboard.

## See Also

### Determining types of pasteboard items

- [- pasteboardTypesForItemSet:](<types(foritemset_).md>) — Returns an array of representation types for each specified pasteboard item.
- [- containsPasteboardTypes:](<contains(pasteboardtypes_).md>) — Returns whether the pasteboard holds data of the specified representation type.
- [- containsPasteboardTypes:inItemSet:](<contains(pasteboardtypes_initemset_).md>) — Returns whether the specified pasteboard items contain data of the given representation types.
- [- itemSetWithPasteboardTypes:](<itemset(withpasteboardtypes_).md>) — Returns an index set identifying pasteboard items having the specified representation types.
