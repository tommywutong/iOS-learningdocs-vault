---
title: NSMapEnumerator
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmapenumerator
source_url: 'https://developer.apple.com/documentation/foundation/nsmapenumerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmapenumerator.json'
content_hash: 'sha256:9cedbac9ee55d1e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapEnumerator

<sub>Structure</sub>

Allows successive elements of a map table to be returned each time this structure is passed to [NSNextMapEnumeratorPair](<nsnextmapenumeratorpair(______).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSMapEnumerator
```

## Overview

The fields of `NSMapEnumerator` are private.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init()](<nsmapenumerator/init().md>)

## See Also

### Data Types

- [NSMapTable](legacy-nsmaptable.md) — The opaque data type used by the functions described in Managing Map Tables.
- [NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.
- [NSMapTableOptions](nsmaptableoptions.md) — Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
- [NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md) — The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.
