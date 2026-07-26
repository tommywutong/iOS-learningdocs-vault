---
title: NSFileCoordinator.ReadingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/readingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/readingoptions.json'
content_hash: 'sha256:a0c4d8aa9dd327ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# NSFileCoordinator.ReadingOptions

<sub>Structure</sub>

Options to use when reading the contents or attributes of a file or directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReadingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSFileCoordinatorReadingWithoutChanges](readingoptions/withoutchanges.md)
- [NSFileCoordinatorReadingResolvesSymbolicLink](readingoptions/resolvessymboliclink.md)
- [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](readingoptions/immediatelyavailablemetadataonly.md) — Specify this constant if you want to read an item’s metadata without triggering a download.
- [NSFileCoordinatorReadingForUploading](readingoptions/foruploading.md) — Specify this content when reading an item for the purpose of uploading its contents.

### Initializers

- [init(rawValue:)](<readingoptions/init(rawvalue_).md>) — Instantiates a reading option using an unsigned integer.

## See Also

### Constants

- [WritingOptions](writingoptions.md) — Options to use when changing the contents or attributes of a file or directory.
