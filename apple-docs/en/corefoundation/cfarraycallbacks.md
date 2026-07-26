---
title: CFArrayCallBacks
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarraycallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraycallbacks.json'
content_hash: 'sha256:3fee195ac22924b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayCallBacks

<sub>Structure</sub>

Structure containing the callbacks of a CFArray.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFArrayCallBacks
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfarraycallbacks/init().md>)
- [init(version:retain:release:copyDescription:equal:)](<cfarraycallbacks/init(version_retain_release_copydescription_equal_).md>)

### Instance Properties

- [copyDescription](cfarraycallbacks/copydescription.md) — The callback used to create a descriptive string representation of each value in the collection. If `NULL`, the collection will create a simple description of each value. See [CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md) for a description of this callback.
- [equal](cfarraycallbacks/equal.md) — The callback used to compare values in the array for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [CFArrayEqualCallBack](cfarrayequalcallback.md) for a description of this callback.
- [release](cfarraycallbacks/release.md) — The callback used to release values as they are removed from the collection. If `NULL`, values are not released. See [CFArrayReleaseCallBack](cfarrayreleasecallback.md) for a description of this callback.
- [retain](cfarraycallbacks/retain.md) — The callback used to retain each value as they are added to the collection. If `NULL`, values are not retained. See [CFArrayRetainCallBack](cfarrayretaincallback.md) for a description of this callback.
- [version](cfarraycallbacks/version.md) — The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.
