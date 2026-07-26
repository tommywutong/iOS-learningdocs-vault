---
title: NSHashTableCallBacks
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtablecallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nshashtablecallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtablecallbacks.json'
content_hash: 'sha256:74f220b9e71f4f2d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashTableCallBacks

<sub>Structure</sub>

Defines a structure that contains the function pointers used to configure behavior of `NSHashTable` with respect to elements within a hash table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSHashTableCallBacks
```

## Overview

All functions must know the types of things in the hash table to be able to operate on them. Sets of predefined call backs are described in [NSHashTable](nshashtable.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<nshashtablecallbacks/init().md>)
- [init(hash:isEqual:retain:release:describe:)](<nshashtablecallbacks/init(hash_isequal_retain_release_describe_).md>)

### Instance Properties

- [describe](nshashtablecallbacks/describe.md) — Points to the function that produces an autoreleased NSString * describing the given element. If `NULL`, then the hash table produces a generic string description.
- [hash](nshashtablecallbacks/hash.md) — Points to the function that must produce hash code for elements of the hash table. If `NULL`, the pointer value is used as the hash code. Second parameter is the element for which hash code should be produced.
- [isEqual](nshashtablecallbacks/isequal.md) — Points to the function that compares second and third parameters. If `NULL`, then == is used for comparison.
- [release](nshashtablecallbacks/release.md) — Points to the function that decrements a reference count for the given element, and if the reference count becomes 0, frees the given element. If `NULL`, then nothing is done for reference counting or releasing.
- [retain](nshashtablecallbacks/retain.md) — Points to the function that increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

## See Also

### Data Types

- [NSHashEnumerator](nshashenumerator.md) — Allows successive elements of a hash table to be returned each time this structure is passed to [NSNextHashEnumeratorItem](<nsnexthashenumeratoritem(__).md>).
- [NSHashTableOptions](nshashtableoptions.md) — Components in a bit-field to specify the behavior of elements in an [NSHashTable](nshashtable.md) object.
