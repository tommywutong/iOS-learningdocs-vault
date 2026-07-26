---
title: 'CTFontCollectionCopyExclusionDescriptors(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectioncopyexclusiondescriptors(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncopyexclusiondescriptors(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncopyexclusiondescriptors%28_%3A%29.json'
content_hash: 'sha256:cbd10ce407a41fd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCopyExclusionDescriptors(_:)

<sub>Function</sub>

Retrieves the array of descriptors to exclude from the match.

<sub>macOS</sub>

```swift
func CTFontCollectionCopyExclusionDescriptors(_ collection: CTFontCollection) -> CFArray?
```

## Parameters

- `collection` — The font collection reference.

## Return Value

A retained reference to the array of descriptors for querying (matching) the system font database.

## See Also

### Excluding and Including Font Descriptors

- [CTFontCollectionCopyQueryDescriptors](<ctfontcollectioncopyquerydescriptors(__).md>) — Retrieves the array of descriptors for font matching.
- [CTFontCollectionSetExclusionDescriptors](<ctfontcollectionsetexclusiondescriptors(____).md>) — Replaces the array of descriptors to exclude from the match.
- [CTFontCollectionSetQueryDescriptors](<ctfontcollectionsetquerydescriptors(____).md>) — Replaces the array of descriptors for font matching.
