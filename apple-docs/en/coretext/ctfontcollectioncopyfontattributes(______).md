---
title: 'CTFontCollectionCopyFontAttributes(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 10.7+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncopyfontattributes(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncopyfontattributes(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncopyfontattributes%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f022b6fddc90cc0d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCopyFontAttributes(_:_:_:)

<sub>Function</sub>

Retrieves an array of dictionaries containing font descriptor attribute values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCollectionCopyFontAttributes(_ collection: CTFontCollection, _ attributeNames: CFSet, _ options: CTFontCollectionCopyOptions) -> CFArray
```

## Parameters

- `collection` — The font collection reference.

- `attributeNames` — The attributes to retrieve for each descriptor in the collection.

- `options` — Options to alter the return value. With [kCTFontCollectionCopyDefaultOptions](ctfontcollectioncopyoptions/kctfontcollectioncopydefaultoptions.md), the values appear in the same order as the results from [CTFontCollectionCreateMatchingFontDescriptors](<ctfontcollectioncreatematchingfontdescriptors(__).md>). Setting [kCTFontCollectionCopyUnique](ctfontcollectioncopyoptions/unique.md) removes duplicate values. Setting [kCTFontCollectionCopyStandardSort](ctfontcollectioncopyoptions/standardsort.md) sorts the values in standard UI order.

## Return Value

An array that contains one [CFDictionary](../corefoundation/cfdictionary.md) value for each descriptor mapping the specified attribute names.

## See Also

### Get Font Descriptor Attributes

- [CTFontCollectionCopyFontAttribute](<ctfontcollectioncopyfontattribute(______).md>) — Retrieves an array of font descriptor attribute values.
