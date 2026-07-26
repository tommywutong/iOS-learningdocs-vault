---
title: 'init(sharedKeySet:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledictionary/init(sharedkeyset:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary/init(sharedkeyset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary/init%28sharedkeyset%3A%29.json'
content_hash: 'sha256:380b2a5a3bc6dcf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableDictionary](../nsmutabledictionary.md)

# init(sharedKeySet:)

<sub>Initializer</sub>

Creates a mutable dictionary which is optimized for dealing with a known set of keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(sharedKeySet keyset: Any)
```

## Parameters

- `keyset` — The `keyset`, created by the [NSDictionary](../nsdictionary.md) class method [+ sharedKeySetForKeys:](<../nsdictionary/sharedkeyset(forkeys_).md>). > [!important] Important > If `keyset` is `nil`, an exception is raised. If `keyset` is not an object returned by [+ sharedKeySetForKeys:](<../nsdictionary/sharedkeyset(forkeys_).md>), an exception is raised.

## Return Value

A new mutable dictionary optimized for a known set of keys.

## Discussion

Keys that are not in the key set can still be set in the dictionary, but that usage is not optimal.

## See Also

### Creating and Initializing a Mutable Dictionary

- [- initWithCapacity:](<init(capacity_).md>) — Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [- init](<init().md>) — Initializes a newly allocated mutable dictionary.
