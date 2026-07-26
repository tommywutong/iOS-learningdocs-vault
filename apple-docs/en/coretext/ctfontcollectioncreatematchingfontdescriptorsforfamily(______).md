---
title: 'CTFontCollectionCreateMatchingFontDescriptorsForFamily(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorsforfamily(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorsforfamily(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorsforfamily%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5c9b0e958de64260'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateMatchingFontDescriptorsForFamily(_:_:_:)

<sub>Function</sub>

Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.

<sub>macOS</sub>

```swift
func CTFontCollectionCreateMatchingFontDescriptorsForFamily(_ collection: CTFontCollection, _ familyName: CFString, _ options: CFDictionary?) -> CFArray?
```

## Parameters

- `collection` — The font collection reference.

- `familyName` — The font family name.

- `options` — The options dictionary.

## Return Value

An array of [CTFontDescriptor](ctfontdescriptor.md) objects that match the specified family in the collection, or `NULL` if there are none.

## See Also

### Getting Font Descriptors

- [CTFontCollectionCreateMatchingFontDescriptors](<ctfontcollectioncreatematchingfontdescriptors(__).md>) — Returns an array of font descriptors matching the collection.
- [CTFontCollectionCreateMatchingFontDescriptorsWithOptions](<ctfontcollectioncreatematchingfontdescriptorswithoptions(____).md>) — Creates an array of font descriptors that match the specified collection.
- [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback](<ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(______).md>) — Returns the array of matching font descriptors sorted with the callback function.
- [CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md) — The collection sorting callback type.
