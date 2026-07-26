---
title: 'init(capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/init%28capacity%3A%29.json'
content_hash: 'sha256:7bcc8e4c3d92f30f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# init(capacity:)

<sub>Initializer</sub>

Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(capacity numItems: Int)
```

## Parameters

- `numItems` — The initial capacity of the initialized dictionary.

## Return Value

An initialized mutable dictionary, which might be different than the original receiver.

## Discussion

Mutable dictionaries allocate additional memory as needed, so `numItems` simply establishes the object’s initial capacity.

This method is a designated initializer of `NSMutableDictionary`.

## See Also

### Creating and Initializing a Mutable Dictionary

- [- init](<init().md>) — Initializes a newly allocated mutable dictionary.
- [+ dictionaryWithSharedKeySet:](<init(sharedkeyset_).md>) — Creates a mutable dictionary which is optimized for dealing with a known set of keys.
