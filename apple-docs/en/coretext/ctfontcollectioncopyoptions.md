---
title: CTFontCollectionCopyOptions
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontcollectioncopyoptions
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcollectioncopyoptions.json'
content_hash: 'sha256:fe4407a6443431b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCollectionCopyOptions

<sub>Structure</sub>

Option bits for use with CTFontCollectionCopyFontAttribute(s).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTFontCollectionCopyOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCTFontCollectionCopyStandardSort](ctfontcollectioncopyoptions/standardsort.md) — Passing this option indicates that the return values should be sorted in standard UI order, suitable for display to the user. This is the same sorting behavior used by `NSFontPanel` and Font Book.
- [kCTFontCollectionCopyUnique](ctfontcollectioncopyoptions/unique.md) — Passing this option indicates that duplicate values should be removed from the results.

### Initializers

- [init(rawValue:)](<ctfontcollectioncopyoptions/init(rawvalue_).md>) — Creates a copy options structure with the specified raw value.

## See Also

### Constants

- [kCTFontCollectionRemoveDuplicatesOption](kctfontcollectionremoveduplicatesoption.md)
