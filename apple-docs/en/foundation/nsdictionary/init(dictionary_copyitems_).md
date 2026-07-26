---
title: 'init(dictionary:copyItems:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdictionary/init(dictionary:copyitems:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/init(dictionary:copyitems:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/init%28dictionary%3Acopyitems%3A%29.json'
content_hash: 'sha256:fb4626cde1bed9c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# init(dictionary:copyItems:)

<sub>Initializer</sub>

Initializes a newly allocated dictionary using the objects contained in another given dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(dictionary otherDictionary: [AnyHashable : Any], copyItems flag: Bool)
```

## Parameters

- `otherDictionary` — A dictionary containing the keys and values with which to initialize the new dictionary.

- `flag` — If [true](../../swift/true.md), each object in `otherDictionary` receives a [copyWithZone:](../../objectivec/nsobject-swift.class/copywithzone_.md) message to create a copy of the object—objects must conform to the `NSCopying` protocol. In a managed memory environment, this is instead of the `retain` message the object would otherwise receive. The object copy is then added to the returned dictionary. If [false](../../swift/false.md), then in a managed memory environment each object in `otherDictionary` simply receives a `retain` message when it is added to the returned dictionary.

## Return Value

An initialized object—which might be different than the original receiver—containing the keys and values found in `otherDictionary`.

## Discussion

After an immutable dictionary has been initialized in this way, it cannot be modified.

The [- copyWithZone:](<../nscopying/copy(with_).md>) method performs a shallow copy. If you have a collection of arbitrary depth, passing [true](../../swift/true.md) for the `flag` parameter will perform an immutable copy of the first level below the surface. If you pass [false](../../swift/false.md) the mutability of the first level is unaffected. In either case, the mutability of all deeper levels is unaffected.

## See Also

### Creating a Dictionary from Another Dictionary

- [- initWithDictionary:](<init(dictionary_)-9fw1u.md>) — Initializes a newly allocated dictionary by placing in it the keys and values contained in another given dictionary.
- [init(dictionaryLiteral:)](<init(dictionaryliteral_).md>) — Initializes a newly allocated dictionary from the given key-value pairs.
