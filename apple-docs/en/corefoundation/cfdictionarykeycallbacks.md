---
title: CFDictionaryKeyCallBacks
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionarykeycallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarykeycallbacks.json'
content_hash: 'sha256:5171c3ee7255a391'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryKeyCallBacks

<sub>Structure</sub>

This structure contains the callbacks used to retain, release, describe, and compare the keys in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFDictionaryKeyCallBacks
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfdictionarykeycallbacks/init().md>)
- [init(version:retain:release:copyDescription:equal:hash:)](<cfdictionarykeycallbacks/init(version_retain_release_copydescription_equal_hash_).md>)

### Instance Properties

- [copyDescription](cfdictionarykeycallbacks/copydescription.md) — The callback used to create a descriptive string representation of each key in the dictionary. If `NULL`, the collection will create a simple description of each key. See [CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md) for a description of this callback.
- [equal](cfdictionarykeycallbacks/equal.md) — The callback used to compare keys in the dictionary for equality. If `NULL`, the collection will use pointer equality to compare keys in the collection. See [CFDictionaryEqualCallBack](cfdictionaryequalcallback.md) for a description of this callback.
- [hash](cfdictionarykeycallbacks/hash.md) — The callback used to compute a hash code for keys as they are used to access, add, or remove values in the dictionary. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [CFDictionaryHashCallBack](cfdictionaryhashcallback.md) for a description of this callback.
- [release](cfdictionarykeycallbacks/release.md) — The callback used to release keys as they are removed from the dictionary. If `NULL`, keys are not released. See [CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md) for a description of this callback.
- [retain](cfdictionarykeycallbacks/retain.md) — The callback used to retain each key as they are added to the collection. This callback returns the value to use as the key in the dictionary, which is usually the value parameter passed to this callback, but may be a different value if a different value should be used as the key. If `NULL`, keys are not retained. See [CFDictionaryRetainCallBack](cfdictionaryretaincallback.md) for a descriptions of this function’s parameters.
- [version](cfdictionarykeycallbacks/version.md) — The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## See Also

### Data Types

- [CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md) — This structure contains the callbacks used to retain, release, describe, and compare the values in a dictionary.
