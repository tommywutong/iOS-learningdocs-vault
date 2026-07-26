---
title: 'CTFontCollectionCreateMatchingFontDescriptorsWithOptions(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorswithoptions(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorswithoptions%28_%3A_%3A%29.json'
content_hash: 'sha256:5470a3b550788b4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateMatchingFontDescriptorsWithOptions(_:_:)

<sub>Function</sub>

Creates an array of font descriptors that match the specified collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCollectionCreateMatchingFontDescriptorsWithOptions(_ collection: CTFontCollection, _ options: CFDictionary?) -> CFArray?
```

## Parameters

- `collection` — The font collection reference.

- `options` — The options dictionary. Passing in `NULL` returns the same results as calling [CTFontCollectionCreateMatchingFontDescriptors](<ctfontcollectioncreatematchingfontdescriptors(__).md>), which uses the options specified during the collection’s creation.

## Return Value

An array of [CTFontDescriptor](ctfontdescriptor.md) objects that match the collection definition, or `NULL` if there are none.

## See Also

### Getting Font Descriptors

- [CTFontCollectionCreateMatchingFontDescriptors](<ctfontcollectioncreatematchingfontdescriptors(__).md>) — Returns an array of font descriptors matching the collection.
- [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback](<ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(______).md>) — Returns the array of matching font descriptors sorted with the callback function.
- [CTFontCollectionCreateMatchingFontDescriptorsForFamily](<ctfontcollectioncreatematchingfontdescriptorsforfamily(______).md>) — Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md) — The collection sorting callback type.
