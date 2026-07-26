---
title: NSFileCoordinator.WritingOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfilecoordinator/writingoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsfilecoordinator/writingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilecoordinator/writingoptions.json'
content_hash: 'sha256:49715d3f5a7c10d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileCoordinator](../nsfilecoordinator.md)

# NSFileCoordinator.WritingOptions

<sub>Structure</sub>

Options to use when changing the contents or attributes of a file or directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WritingOptions
```

## Overview

You must specify only one constant at a time for a given write operation.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSFileCoordinatorWritingForDeleting](writingoptions/fordeleting.md)
- [NSFileCoordinatorWritingForMoving](writingoptions/formoving.md)
- [NSFileCoordinatorWritingForMerging](writingoptions/formerging.md)
- [NSFileCoordinatorWritingForReplacing](writingoptions/forreplacing.md)
- [NSFileCoordinatorWritingContentIndependentMetadataOnly](writingoptions/contentindependentmetadataonly.md) — Select this option when writing to change the file’s metadata only and not its contents.

### Initializers

- [init(rawValue:)](<writingoptions/init(rawvalue_).md>) — Instantiates a writing option using an unsigned integer.

## See Also

### Constants

- [ReadingOptions](readingoptions.md) — Options to use when reading the contents or attributes of a file or directory.
