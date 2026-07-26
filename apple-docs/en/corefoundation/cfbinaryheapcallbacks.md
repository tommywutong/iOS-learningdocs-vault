---
title: CFBinaryHeapCallBacks
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbinaryheapcallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbinaryheapcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbinaryheapcallbacks.json'
content_hash: 'sha256:3f9f0fe479a80c60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBinaryHeapCallBacks

<sub>Structure</sub>

Structure containing the callbacks for values for a `CFBinaryHeap` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFBinaryHeapCallBacks
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cfbinaryheapcallbacks/init().md>)
- [init(version:retain:release:copyDescription:compare:)](<cfbinaryheapcallbacks/init(version_retain_release_copydescription_compare_).md>)

### Instance Properties

- [compare](cfbinaryheapcallbacks/compare.md) — The callback used to compare values in the binary heap in some operations. This field cannot be `NULL`.
- [copyDescription](cfbinaryheapcallbacks/copydescription.md) — Callback function used to get a description of a value in a binary heap.
- [release](cfbinaryheapcallbacks/release.md) — Callback function used to release a value before it is removed from a binary heap.
- [retain](cfbinaryheapcallbacks/retain.md) — Callback function used to retain a value being added to a binary heap.
- [version](cfbinaryheapcallbacks/version.md) — The version number of the structure type being passed in as a parameter to the `CFBinaryHeap` creation functions. This structure is version `0`.

## See Also

### Data Types

- [CFBinaryHeapCompareContext](cfbinaryheapcomparecontext.md) — Not used.
