---
title: dictionaryRepresentation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsubiquitouskeyvaluestore/dictionaryrepresentation
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/dictionaryrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/dictionaryrepresentation.json'
content_hash: 'sha256:37cdf72d41bf574b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# dictionaryRepresentation

<sub>Instance Property</sub>

A dictionary with all of the key-value pairs in the iCloud key-value store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dictionaryRepresentation: [String : Any] { get }
```

## Discussion

Getting this property retrieves the in-memory copy of the keys and values. If changes to the keys and values are pending, the system fetches those changes from iCloud and updates the dictionary before returning it. To ensure the dictionary contains all recent changes, call [- synchronize](<synchronize().md>) shortly before accessing this property. All of the values in the dictionary are property list object types.

## See Also

### Getting values

- [- boolForKey:](<bool(forkey_).md>) — Returns the Boolean value associated with the specified key.
- [- doubleForKey:](<double(forkey_).md>) — Returns the double value associated with the specified key.
- [- longLongForKey:](<longlong(forkey_).md>) — Returns the 64-bit integer value associated with the specified key.
- [- stringForKey:](<string(forkey_).md>) — Returns the string associated with the specified key.
- [- dataForKey:](<data(forkey_).md>) — Returns the data object associated with the specified key.
- [- objectForKey:](<object(forkey_).md>) — Returns the object associated with the specified key.
- [- arrayForKey:](<array(forkey_).md>) — Returns the array associated with the specified key.
- [- dictionaryForKey:](<dictionary(forkey_).md>) — Returns the dictionary object associated with the specified key.
