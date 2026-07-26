---
title: 'double(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsubiquitouskeyvaluestore/double(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/double(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/double%28forkey%3A%29.json'
content_hash: 'sha256:ef21b462c06097f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# double(forKey:)

<sub>Instance Method</sub>

Returns the double value associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func double(forKey aKey: String) -> Double
```

## Parameters

- `aKey` — The key to retrieve from the iCloud key-value store.

## Return Value

The double value associated with `aKey`, or `0.0` if the key isn’t present.

## Discussion

This method automatically coerces certain types to their equivalent double values. The Boolean value `true` becomes `1.0` and `false` becomes `0.0`. An integer becomes the equivalent double –– for example, `2` becomes `2.0`. A string that contains a numerical value contains the equivalent double — for example, “123.4” becomes `123.4`.

## See Also

### Getting values

- [- boolForKey:](<bool(forkey_).md>) — Returns the Boolean value associated with the specified key.
- [- longLongForKey:](<longlong(forkey_).md>) — Returns the 64-bit integer value associated with the specified key.
- [- stringForKey:](<string(forkey_).md>) — Returns the string associated with the specified key.
- [- dataForKey:](<data(forkey_).md>) — Returns the data object associated with the specified key.
- [- objectForKey:](<object(forkey_).md>) — Returns the object associated with the specified key.
- [- arrayForKey:](<array(forkey_).md>) — Returns the array associated with the specified key.
- [- dictionaryForKey:](<dictionary(forkey_).md>) — Returns the dictionary object associated with the specified key.
- [dictionaryRepresentation](dictionaryrepresentation.md) — A dictionary with all of the key-value pairs in the iCloud key-value store.
