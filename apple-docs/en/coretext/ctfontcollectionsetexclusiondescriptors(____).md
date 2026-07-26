---
title: 'CTFontCollectionSetExclusionDescriptors(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcollectionsetexclusiondescriptors(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectionsetexclusiondescriptors(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectionsetexclusiondescriptors%28_%3A_%3A%29.json'
content_hash: 'sha256:2e043614a6e299a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionSetExclusionDescriptors(_:_:)

<sub>Function</sub>

Replaces the array of descriptors to exclude from the match.

<sub>macOS</sub>

```swift
func CTFontCollectionSetExclusionDescriptors(_ collection: CTMutableFontCollection, _ descriptors: CFArray?)
```

## Parameters

- `collection` — The font collection reference.

- `descriptors` — An array of [CTFontDescriptor](ctfontdescriptor.md) objects. This parameter can be `NULL`.

## See Also

### Excluding and Including Font Descriptors

- [CTFontCollectionCopyExclusionDescriptors](<ctfontcollectioncopyexclusiondescriptors(__).md>) — Retrieves the array of descriptors to exclude from the match.
- [CTFontCollectionCopyQueryDescriptors](<ctfontcollectioncopyquerydescriptors(__).md>) — Retrieves the array of descriptors for font matching.
- [CTFontCollectionSetQueryDescriptors](<ctfontcollectionsetquerydescriptors(____).md>) — Replaces the array of descriptors for font matching.
