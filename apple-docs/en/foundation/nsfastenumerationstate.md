---
title: NSFastEnumerationState
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfastenumerationstate
source_url: 'https://developer.apple.com/documentation/foundation/nsfastenumerationstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfastenumerationstate.json'
content_hash: 'sha256:c00b26703a785b7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSFastEnumerationState

<sub>Structure</sub>

This defines the structure used as contextual information in the [NSFastEnumeration](nsfastenumeration.md) protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSFastEnumerationState
```

## Overview

For more information, see [- countByEnumeratingWithState:objects:count:](<nsfastenumeration/countbyenumerating(with_objects_count_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<nsfastenumerationstate/init().md>)
- [init(state:itemsPtr:mutationsPtr:extra:)](<nsfastenumerationstate/init(state_itemsptr_mutationsptr_extra_).md>)

### Instance Properties

- [extra](nsfastenumerationstate/extra.md) — A C array that you can use to hold returned values.
- [itemsPtr](nsfastenumerationstate/itemsptr.md) — A C array of objects.
- [mutationsPtr](nsfastenumerationstate/mutationsptr.md) — Arbitrary state information used to detect whether the collection has been mutated.
- [state](nsfastenumerationstate/state.md) — Arbitrary state information used by the iterator. Typically this is set to `0` at the beginning of the iteration.
