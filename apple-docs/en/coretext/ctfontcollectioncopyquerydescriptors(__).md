---
title: 'CTFontCollectionCopyQueryDescriptors(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncopyquerydescriptors(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncopyquerydescriptors(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncopyquerydescriptors%28_%3A%29.json'
content_hash: 'sha256:2b2613c14cdd35f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCopyQueryDescriptors(_:)

<sub>Function</sub>

Retrieves the array of descriptors for font matching.

<sub>macOS</sub>

```swift
func CTFontCollectionCopyQueryDescriptors(_ collection: CTFontCollection) -> CFArray?
```

## Parameters

- `collection` — The font collection reference.

## Return Value

A retained reference to the array of descriptors for querying (matching) the system font database. The return value is undefined if you create the collection with [CTFontCollectionCreateFromAvailableFonts](<ctfontcollectioncreatefromavailablefonts(__).md>).

## See Also

### Excluding and Including Font Descriptors

- [CTFontCollectionCopyExclusionDescriptors](<ctfontcollectioncopyexclusiondescriptors(__).md>) — Retrieves the array of descriptors to exclude from the match.
- [CTFontCollectionSetExclusionDescriptors](<ctfontcollectionsetexclusiondescriptors(____).md>) — Replaces the array of descriptors to exclude from the match.
- [CTFontCollectionSetQueryDescriptors](<ctfontcollectionsetquerydescriptors(____).md>) — Replaces the array of descriptors for font matching.
