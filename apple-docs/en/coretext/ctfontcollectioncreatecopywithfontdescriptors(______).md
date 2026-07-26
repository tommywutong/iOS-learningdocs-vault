---
title: 'CTFontCollectionCreateCopyWithFontDescriptors(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatecopywithfontdescriptors(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatecopywithfontdescriptors(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatecopywithfontdescriptors%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8db7aa1a84d5cc4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateCopyWithFontDescriptors(_:_:_:)

<sub>Function</sub>

Returns a copy of the original collection augmented with the given new font descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCollectionCreateCopyWithFontDescriptors(_ original: CTFontCollection, _ queryDescriptors: CFArray?, _ options: CFDictionary?) -> CTFontCollection
```

## Parameters

- `original` — The original font collection reference.

- `queryDescriptors` — An array of font descriptors to augment those of the original collection.

- `options` — The options dictionary. For possible values, see Constants.

## Return Value

A copy of the original font collection augmented by the new font descriptors and options.

## Discussion

The new font descriptors are merged with the existing descriptors to create a single set.

## See Also

### Creating Font Collections

- [CTFontCollectionCreateFromAvailableFonts](<ctfontcollectioncreatefromavailablefonts(__).md>) — Returns a new font collection containing all available fonts.
- [CTFontCollectionCreateWithFontDescriptors](<ctfontcollectioncreatewithfontdescriptors(____).md>) — Returns a new font collection based on the given array of font descriptors.
- [CTFontCollectionCreateMutableCopy](<ctfontcollectioncreatemutablecopy(__).md>) — Creates a mutable copy of the original collection.
