---
title: 'init(dictionary:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(dictionary:)-9fw1u'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(dictionary:)-9fw1u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28dictionary%3A%29-9fw1u.json'
content_hash: 'sha256:ce1306fcad282808'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(dictionary:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(dictionary otherDictionary: [AnyHashable : Any])
```

## Parameters

- `otherDictionary` — A dictionary containing the keys and values with which to initialize the new dictionary.

## Return Value

An initialized dictionary—which might be different than the original receiver—containing the keys and values found in `otherDictionary`.

## See Also

### Creating a Dictionary from Another Dictionary

- [- initWithDictionary:copyItems:](<init(dictionary_copyitems_).md>) — Initializes a newly allocated dictionary using the objects contained in another given dictionary.
- [init(dictionaryLiteral:)](<init(dictionaryliteral_).md>) — Initializes a newly allocated dictionary from the given key-value pairs.
