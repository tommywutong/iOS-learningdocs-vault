---
title: 'init(dictionaryLiteral:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(dictionaryliteral:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(dictionaryliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28dictionaryliteral%3A%29.json'
content_hash: 'sha256:6a6a49a830a8db09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(dictionaryLiteral:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary from the given key-value pairs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
required convenience init(dictionaryLiteral elements: (Any, Any)...)
```

## Parameters

- `elements` — A variadic array of two-member tuples, where the first member is a key and the second is its corresponding value.

## See Also

### Creating a Dictionary from Another Dictionary

- [- initWithDictionary:](<init(dictionary_)-9fw1u.md>) — Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [- initWithDictionary:copyItems:](<init(dictionary_copyitems_).md>) — Initializes a newly allocated dictionary using the objects contained in another given dictionary.
