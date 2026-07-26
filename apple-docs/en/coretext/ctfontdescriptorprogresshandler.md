---
title: CTFontDescriptorProgressHandler
framework: Core Text
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontdescriptorprogresshandler
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorprogresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorprogresshandler.json'
content_hash: 'sha256:9b34be2ae28dd01c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorProgressHandler

<sub>Type Alias</sub>

The progress callback type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CTFontDescriptorProgressHandler = (CTFontDescriptorMatchingState, CFDictionary) -> Bool
```

## Discussion

Use this callback type with [CTFontDescriptorMatchFontDescriptorsWithProgressHandler](<ctfontdescriptormatchfontdescriptorswithprogresshandler(______).md>).

## See Also

### Data Types

- [ATSFontRef](atsfontref.md)
- [CTFontCollectionSortDescriptorsCallback](ctfontcollectionsortdescriptorscallback.md) — The collection sorting callback type.
