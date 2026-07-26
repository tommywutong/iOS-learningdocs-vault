---
title: NSMapTableValueCallBacks
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptablevaluecallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablevaluecallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablevaluecallbacks.json'
content_hash: 'sha256:2a807a087fa6ed39'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapTableValueCallBacks

<sub>Structure</sub>

The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSMapTableValueCallBacks
```

## Overview

All functions must know the types of things in the map table to be able to operate on them. Sets of predefined call backs are described in [NSMapTable](nsmaptable.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<nsmaptablevaluecallbacks/init().md>)
- [init(retain:release:describe:)](<nsmaptablevaluecallbacks/init(retain_release_describe_).md>)

### Instance Properties

- [describe](nsmaptablevaluecallbacks/describe.md) — Points to the function that produces an autoreleased NSString * describing the given element. If `NULL`, then the map table produces a generic string description.
- [release](nsmaptablevaluecallbacks/release.md) — Points to the function that decrements a reference count for the given element, and if the reference count becomes zero, frees the given element. If `NULL`, then nothing is done for reference counting or releasing.
- [retain](nsmaptablevaluecallbacks/retain.md) — Points to the function that increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

## See Also

### Data Types

- [NSMapEnumerator](nsmapenumerator.md) — Allows successive elements of a map table to be returned each time this structure is passed to [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>).
- [NSMapTable](legacy-nsmaptable.md) — The opaque data type used by the functions described in Managing Map Tables.
- [NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.
- [NSMapTableOptions](nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
