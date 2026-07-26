---
title: 'CTFontCollectionSetQueryDescriptors(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectionsetquerydescriptors(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectionsetquerydescriptors(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectionsetquerydescriptors%28_%3A_%3A%29.json'
content_hash: 'sha256:2d599a53a78bec88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionSetQueryDescriptors(_:_:)

<sub>Function</sub>

Replaces the array of descriptors for font matching.

<sub>macOS</sub>

```swift
func CTFontCollectionSetQueryDescriptors(_ collection: CTMutableFontCollection, _ descriptors: CFArray?)
```

## Parameters

- `collection` — The font collection reference.

- `descriptors` — An array of [CTFontDescriptor](ctfontdescriptor.md) objects. Passing in `NULL` represents an empty collection, which sets the matching descriptors to `NULL`.

## See Also

### Excluding and Including Font Descriptors

- [CTFontCollectionCopyExclusionDescriptors](<ctfontcollectioncopyexclusiondescriptors(__).md>) — Retrieves the array of descriptors to exclude from the match.
- [CTFontCollectionCopyQueryDescriptors](<ctfontcollectioncopyquerydescriptors(__).md>) — Retrieves the array of descriptors for font matching.
- [CTFontCollectionSetExclusionDescriptors](<ctfontcollectionsetexclusiondescriptors(____).md>) — Replaces the array of descriptors to exclude from the match.
