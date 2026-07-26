---
title: 'longLong(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsubiquitouskeyvaluestore/longlong(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/longlong(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/longlong%28forkey%3A%29.json'
content_hash: 'sha256:c1f823e711e1d1c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# longLong(forKey:)

<sub>Instance Method</sub>

Returns the 64-bit integer value associated with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func longLong(forKey aKey: String) -> Int64
```

## Parameters

- `aKey` — The key to retrieve from the iCloud key-value store.

## Return Value

The integer value associated with `aKey`, or `0` if the key isn’t present.

## Discussion

This method automatically coerces certain types to their equivalent long integer values. The Boolean value `true` becomes `1` and `false` becomes `0`. A floating-point number becomes the greatest integer that’s less than the stored number –– for example, `2.67` becomes `2`. A string that contains a numerical value contains the equivalent integer value — for example, “123” becomes `123`.

## See Also

### Getting values

- [- boolForKey:](<bool(forkey_).md>) — Returns the Boolean value associated with the specified key.
- [- doubleForKey:](<double(forkey_).md>) — Returns the double value associated with the specified key.
- [- stringForKey:](<string(forkey_).md>) — Returns the string associated with the specified key.
- [- dataForKey:](<data(forkey_).md>) — Returns the data object associated with the specified key.
- [- objectForKey:](<object(forkey_).md>) — Returns the object associated with the specified key.
- [- arrayForKey:](<array(forkey_).md>) — Returns the array associated with the specified key.
- [- dictionaryForKey:](<dictionary(forkey_).md>) — Returns the dictionary object associated with the specified key.
- [dictionaryRepresentation](dictionaryrepresentation.md) — A dictionary with all of the key-value pairs in the iCloud key-value store.
