---
title: 'CTFontCollectionCreateMatchingFontDescriptors(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatematchingfontdescriptors(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptors(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatematchingfontdescriptors%28_%3A%29.json'
content_hash: 'sha256:939b4a89ed9f3df4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateMatchingFontDescriptors(_:)

<sub>Function</sub>

Returns an array of font descriptors matching the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCollectionCreateMatchingFontDescriptors(_ collection: CTFontCollection) -> CFArray?
```

## Parameters

- `collection` — The font collection reference.

## Return Value

A retained reference to an array of normalized font descriptors matching the collection definition.

## See Also

### Getting Font Descriptors

- [CTFontCollectionCreateMatchingFontDescriptorsWithOptions](<ctfontcollectioncreatematchingfontdescriptorswithoptions(____).md>) — Creates an array of font descriptors that match the specified collection.
- [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback](<ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(______).md>) — Returns the array of matching font descriptors sorted with the callback function.
- [CTFontCollectionCreateMatchingFontDescriptorsForFamily](<ctfontcollectioncreatematchingfontdescriptorsforfamily(______).md>) — Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md) — The collection sorting callback type.
