---
title: CTFontCollectionSortDescriptorsCallback
framework: Core Text
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontcollectionsortdescriptorscallback
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectionsortdescriptorscallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectionsortdescriptorscallback.json'
content_hash: 'sha256:b7de3e57dddbdac0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionSortDescriptorsCallback

<sub>Type Alias</sub>

The collection sorting callback type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CTFontCollectionSortDescriptorsCallback = (CTFontDescriptor, CTFontDescriptor, UnsafeMutableRawPointer) -> CFComparisonResult
```

## Parameters

- `first` — The first descriptor.

- `second` — The second descriptor.

- `refCon` — A pointer to contextual data from the client.

## Return Value

The matching font descriptors of a collection in sorted order.

## See Also

### Getting Font Descriptors

- [CTFontCollectionCreateMatchingFontDescriptors](<ctfontcollectioncreatematchingfontdescriptors(__).md>) — Returns an array of font descriptors matching the collection.
- [CTFontCollectionCreateMatchingFontDescriptorsWithOptions](<ctfontcollectioncreatematchingfontdescriptorswithoptions(____).md>) — Creates an array of font descriptors that match the specified collection.
- [CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback](<ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(______).md>) — Returns the array of matching font descriptors sorted with the callback function.
- [CTFontCollectionCreateMatchingFontDescriptorsForFamily](<ctfontcollectioncreatematchingfontdescriptorsforfamily(______).md>) — Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
