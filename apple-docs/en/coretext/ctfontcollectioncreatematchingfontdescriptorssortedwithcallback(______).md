---
title: 'CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorssortedwithcallback(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncreatematchingfontdescriptorssortedwithcallback%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d64bab1a24431120'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_:_:_:)

<sub>Function</sub>

Returns the array of matching font descriptors sorted with the callback function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(_ collection: CTFontCollection, _ sortCallback: CTFontCollectionSortDescriptorsCallback?, _ refCon: UnsafeMutableRawPointer?) -> CFArray?
```

## Parameters

- `collection` — The collection reference.

- `sortCallback` — The sorting callback function that defines the sort order.

- `refCon` — Pointer to client data define context for the callback.

## Return Value

An array of font descriptors matching the criteria of the collection sorted by the results of the sorting callback function.

## See Also

### Getting Font Descriptors

- [CTFontCollectionCreateMatchingFontDescriptors](<ctfontcollectioncreatematchingfontdescriptors(__).md>) — Returns an array of font descriptors matching the collection.
- [CTFontCollectionCreateMatchingFontDescriptorsWithOptions](<ctfontcollectioncreatematchingfontdescriptorswithoptions(____).md>) — Creates an array of font descriptors that match the specified collection.
- [CTFontCollectionCreateMatchingFontDescriptorsForFamily](<ctfontcollectioncreatematchingfontdescriptorsforfamily(______).md>) — Retrieves an array of font descriptors that match the specified family, one descriptor for each style in the collection.
- [CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md) — The collection sorting callback type.
