---
title: NSMapTableKeyCallBacks
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptablekeycallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptablekeycallbacks.json'
content_hash: 'sha256:7d60bf4e005ccc79'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapTableKeyCallBacks

<sub>Structure</sub>

The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSMapTableKeyCallBacks
```

## Overview

All functions must know the types of things in the map table to be able to operate on them. Sets of predefined call backs are described in [NSMapTable](nsmaptable.md).

Two predefined values to use for `notAKeyMarker` are [NSNotAnIntMapKey](nsnotanintmapkey.md) and [NSNotAPointerMapKey](nsnotapointermapkey.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<nsmaptablekeycallbacks/init().md>)
- [init(hash:isEqual:retain:release:describe:notAKeyMarker:)](<nsmaptablekeycallbacks/init(hash_isequal_retain_release_describe_notakeymarker_).md>)

### Instance Properties

- [describe](nsmaptablekeycallbacks/describe.md) — Points to the function which produces an autoreleased NSString * describing the given element. If `NULL`, then the map table produces a generic string description.
- [hash](nsmaptablekeycallbacks/hash.md) — Points to the function which must produce hash code for key elements of the map table. If `NULL`, the pointer value is used as the hash code. Second parameter is the element for which hash code should be produced.
- [isEqual](nsmaptablekeycallbacks/isequal.md) — Points to the function which compares second and third parameters. If `NULL`, then == is used for comparison.
- [notAKeyMarker](nsmaptablekeycallbacks/notakeymarker.md) — No key put in map table can be this value. An exception is raised if attempt is made to use this value as a key
- [release](nsmaptablekeycallbacks/release.md) — Points to the function which decrements a reference count for the given element, and if the reference count becomes zero, frees the given element. If `NULL`, then nothing is done for reference counting or releasing.
- [retain](nsmaptablekeycallbacks/retain.md) — Points to the function which increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

## See Also

### Data Types

- [NSMapEnumerator](nsmapenumerator.md) — Allows successive elements of a map table to be returned each time this structure is passed to [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>).
- [NSMapTable](legacy-nsmaptable.md) — The opaque data type used by the functions described in Managing Map Tables.
- [NSMapTableOptions](nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
- [NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.
