---
title: NSHashEnumerator
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashenumerator
source_url: 'https://developer.apple.com/documentation/foundation/nshashenumerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashenumerator.json'
content_hash: 'sha256:9932b529cf3220ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSHashEnumerator

<sub>Structure</sub>

Allows successive elements of a hash table to be returned each time this structure is passed to [NSNextHashEnumeratorItem](<nsnexthashenumeratoritem(__).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSHashEnumerator
```

## Overview

The fields of `NSHashEnumerator` are private.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<nshashenumerator/init().md>)

## See Also

### Data Types

- [NSHashTableCallBacks](nshashtablecallbacks.md) — Defines a structure that contains the function pointers used to configure behavior of `NSHashTable` with respect to elements within a hash table.
- [NSHashTableOptions](nshashtableoptions.md) — Components in a bit-field to specify the behavior of elements in an [NSHashTable](nshashtable.md) object.
