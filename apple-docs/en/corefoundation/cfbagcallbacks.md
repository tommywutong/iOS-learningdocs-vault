---
title: CFBagCallBacks
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbagcallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcallbacks.json'
content_hash: 'sha256:d9c3e82ad8c863d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagCallBacks

<sub>Structure</sub>

This structure contains the callbacks used to retain, release, describe, and compare the values of a CFBag object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFBagCallBacks
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfbagcallbacks/init().md>)
- [init(version:retain:release:copyDescription:equal:hash:)](<cfbagcallbacks/init(version_retain_release_copydescription_equal_hash_).md>)

### Instance Properties

- [copyDescription](cfbagcallbacks/copydescription.md) — The callback used to create a descriptive string representation of each value in the collection. If `NULL`, the collection will create a simple description of each value. See [CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md) for a description of this callback.
- [equal](cfbagcallbacks/equal.md) — The callback used to compare values in the collection for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [CFBagEqualCallBack](cfbagequalcallback.md) for a description of this callback.
- [hash](cfbagcallbacks/hash.md) — The callback used to compute a hash code for values in a collection. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [CFBagHashCallBack](cfbaghashcallback.md) for a description of this callback.
- [release](cfbagcallbacks/release.md) — The callback used to release values as they are removed from the collection. If `NULL`, values are not released. See [CFBagReleaseCallBack](cfbagreleasecallback.md) for a description of this callback.
- [retain](cfbagcallbacks/retain.md) — The callback used to retain each value as they are added to the collection. If `NULL`, values are not retained. See [CFBagRetainCallBack](cfbagretaincallback.md) for a descriptions of this function’s parameters.
- [version](cfbagcallbacks/version.md) — The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.
