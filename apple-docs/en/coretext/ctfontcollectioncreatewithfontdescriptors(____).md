---
title: 'CTFontCollectionCreateWithFontDescriptors(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatewithfontdescriptors(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatewithfontdescriptors(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatewithfontdescriptors%28_%3A_%3A%29.json'
content_hash: 'sha256:10fdd6dd437f3b6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateWithFontDescriptors(_:_:)

<sub>Function</sub>

Returns a new font collection based on the given array of font descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCollectionCreateWithFontDescriptors(_ queryDescriptors: CFArray?, _ options: CFDictionary?) -> CTFontCollection
```

## Parameters

- `queryDescriptors` — An array of font descriptors.

- `options` — The options dictionary. For possible values, see Constants.

## Return Value

A new font collection based on the provided font descriptors.

## Discussion

The contents of the returned collection are defined by matching the provided descriptors against all available font descriptors.

## See Also

### Creating Font Collections

- [CTFontCollectionCreateFromAvailableFonts](<ctfontcollectioncreatefromavailablefonts(__).md>) — Returns a new font collection containing all available fonts.
- [CTFontCollectionCreateCopyWithFontDescriptors](<ctfontcollectioncreatecopywithfontdescriptors(______).md>) — Returns a copy of the original collection augmented with the given new font descriptors.
- [CTFontCollectionCreateMutableCopy](<ctfontcollectioncreatemutablecopy(__).md>) — Creates a mutable copy of the original collection.
