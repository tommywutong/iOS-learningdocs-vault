---
title: 'CTFontCollectionCreateMutableCopy(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatemutablecopy(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatemutablecopy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatemutablecopy%28_%3A%29.json'
content_hash: 'sha256:8c84a19f32bf60e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateMutableCopy(_:)

<sub>Function</sub>

Creates a mutable copy of the original collection.

<sub>macOS</sub>

```swift
func CTFontCollectionCreateMutableCopy(_ original: CTFontCollection) -> CTMutableFontCollection
```

## Parameters

- `original` — The original font collection reference.

## Return Value

A mutable copy of the original font collection.

## See Also

### Creating Font Collections

- [CTFontCollectionCreateFromAvailableFonts](<ctfontcollectioncreatefromavailablefonts(__).md>) — Returns a new font collection containing all available fonts.
- [CTFontCollectionCreateWithFontDescriptors](<ctfontcollectioncreatewithfontdescriptors(____).md>) — Returns a new font collection based on the given array of font descriptors.
- [CTFontCollectionCreateCopyWithFontDescriptors](<ctfontcollectioncreatecopywithfontdescriptors(______).md>) — Returns a copy of the original collection augmented with the given new font descriptors.
