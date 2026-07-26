---
title: CFDictionaryValueCallBacks
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionaryvaluecallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryvaluecallbacks.json'
content_hash: 'sha256:7f039cf4c3e9caf3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionaryValueCallBacks

<sub>Structure</sub>

This structure contains the callbacks used to retain, release, describe, and compare the values in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFDictionaryValueCallBacks
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfdictionaryvaluecallbacks/init().md>)
- [init(version:retain:release:copyDescription:equal:)](<cfdictionaryvaluecallbacks/init(version_retain_release_copydescription_equal_).md>)

### Instance Properties

- [copyDescription](cfdictionaryvaluecallbacks/copydescription.md) — The callback used to create a descriptive string representation of each value in the dictionary. If `NULL`, the collection will create a simple description of each value. See [CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md) for a description of this callback.
- [equal](cfdictionaryvaluecallbacks/equal.md) — The callback used to compare values in the dictionary for equality. If `NULL`, the collection will use pointer equality to compare values in the collection. See [CFDictionaryEqualCallBack](cfdictionaryequalcallback.md) for a description of this callback.
- [release](cfdictionaryvaluecallbacks/release.md) — The callback used to release values as they are removed from the dictionary. If `NULL`, values are not released. See [CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md) for a description of this callback.
- [retain](cfdictionaryvaluecallbacks/retain.md) — The callback used to retain each value as they are added to the collection. This callback returns the value to use as the value in the dictionary, which is usually the value parameter passed to this callback, but may be a different value if a different value should be used as the value. If `NULL`, values are not retained. See [CFDictionaryRetainCallBack](cfdictionaryretaincallback.md) for a descriptions of this function’s parameters.
- [version](cfdictionaryvaluecallbacks/version.md) — The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## See Also

### Data Types

- [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) — This structure contains the callbacks used to retain, release, describe, and compare the keys in a dictionary.
