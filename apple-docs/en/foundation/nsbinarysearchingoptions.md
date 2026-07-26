---
title: NSBinarySearchingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbinarysearchingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsbinarysearchingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbinarysearchingoptions.json'
content_hash: 'sha256:9dca78392e0653c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSBinarySearchingOptions

<sub>Structure</sub>

Options for searches and insertions using [- indexOfObject:inSortedRange:options:usingComparator:](<nsarray/index(of_insortedrange_options_usingcomparator_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSBinarySearchingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [NSBinarySearchingFirstEqual](nsbinarysearchingoptions/firstequal.md) — Specifies that the search should return the first object in the range that is equal to the given object.
- [NSBinarySearchingLastEqual](nsbinarysearchingoptions/lastequal.md) — Specifies that the search should return the last object in the range that is equal to the given object.
- [NSBinarySearchingInsertionIndex](nsbinarysearchingoptions/insertionindex.md) — Returns the index at which you should insert the object in order to maintain a sorted array.

### Initializers

- [init(rawValue:)](<nsbinarysearchingoptions/init(rawvalue_).md>)
