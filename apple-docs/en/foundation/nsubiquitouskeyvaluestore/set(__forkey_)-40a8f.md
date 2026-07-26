---
title: 'set(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-40a8f'
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-40a8f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/set%28_%3Aforkey%3A%29-40a8f.json'
content_hash: 'sha256:41eb8d4707e7ed9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# set(_:forKey:)

<sub>Instance Method</sub>

Sets the value of the specified key to an array of property list objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ anArray: [Any]?, forKey aKey: String)
```

## Parameters

- `anArray` — The array object to save in the iCloud key-value store. The array must contain only property list types.

- `aKey` — The key to associate with the value.

## See Also

### Setting values

- [- setBool:forKey:](<set(__forkey_)-8o8mq.md>) — Sets the value of the specified key to a Boolean value.
- [- setDouble:forKey:](<set(__forkey_)-1xml0.md>) — Sets the value of the specified key to a double value.
- [- setLongLong:forKey:](<set(__forkey_)-7tt20.md>) — Sets the value of the specified key to a 64-bit integer value.
- [- setString:forKey:](<set(__forkey_)-2rlp.md>) — Sets the value of the specified key to a string value.
- [- setData:forKey:](<set(__forkey_)-3ga7z.md>) — Sets the value of the specified key to a data object.
- [- setObject:forKey:](<set(__forkey_)-9e3de.md>) — Sets the value of the specified key to a property list object.
- [- setDictionary:forKey:](<set(__forkey_)-9vmlm.md>) — Sets the value of the specified key to a dictionary of property list objects.
