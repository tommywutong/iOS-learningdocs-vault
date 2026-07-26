---
title: standardSort
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontcollectioncopyoptions/standardsort
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/standardsort'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncopyoptions/standardsort.json'
content_hash: 'sha256:59ffbc36ae02df16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontCollectionCopyOptions](../ctfontcollectioncopyoptions.md)

# standardSort

<sub>Type Property</sub>

Passing this option indicates that the return values should be sorted in standard UI order, suitable for display to the user. This is the same sorting behavior used by `NSFontPanel` and Font Book.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var standardSort: CTFontCollectionCopyOptions { get }
```

## See Also

### Constants

- [kCTFontCollectionCopyUnique](unique.md) — Passing this option indicates that duplicate values should be removed from the results.
