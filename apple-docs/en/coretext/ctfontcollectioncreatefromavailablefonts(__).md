---
title: 'CTFontCollectionCreateFromAvailableFonts(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatefromavailablefonts(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatefromavailablefonts(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatefromavailablefonts%28_%3A%29.json'
content_hash: 'sha256:19bf32f9190544e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateFromAvailableFonts(_:)

<sub>Function</sub>

Returns a new font collection containing all available fonts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCollectionCreateFromAvailableFonts(_ options: CFDictionary?) -> CTFontCollection
```

## Parameters

- `options` — The options dictionary. For possible values, see Constants.

## Return Value

A new collection containing all fonts available to the current application.

## See Also

### Creating Font Collections

- [CTFontCollectionCreateWithFontDescriptors](<ctfontcollectioncreatewithfontdescriptors(____).md>) — Returns a new font collection based on the given array of font descriptors.
- [CTFontCollectionCreateCopyWithFontDescriptors](<ctfontcollectioncreatecopywithfontdescriptors(______).md>) — Returns a copy of the original collection augmented with the given new font descriptors.
- [CTFontCollectionCreateMutableCopy](<ctfontcollectioncreatemutablecopy(__).md>) — Creates a mutable copy of the original collection.
