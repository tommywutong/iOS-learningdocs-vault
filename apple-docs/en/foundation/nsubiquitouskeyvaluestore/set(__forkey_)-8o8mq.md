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
doc_path: '/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-8o8mq'
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-8o8mq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/set%28_%3Aforkey%3A%29-8o8mq.json'
content_hash: 'sha256:93179795d13c762f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# set(_:forKey:)

<sub>Instance Method</sub>

Sets the value of the specified key to a Boolean value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ value: Bool, forKey aKey: String)
```

## Parameters

- `value` — The Boolean value to save to the iCloud key-value store.

- `aKey` — The key to associate with the value.

## Discussion

This method places the Boolean value in an [NSNumber](../nsnumber.md) type before writing the key and value to the store.

## See Also

### Setting values

- [- setDouble:forKey:](<set(__forkey_)-1xml0.md>) — Sets the value of the specified key to a double value.
- [- setLongLong:forKey:](<set(__forkey_)-7tt20.md>) — Sets the value of the specified key to a 64-bit integer value.
- [- setString:forKey:](<set(__forkey_)-2rlp.md>) — Sets the value of the specified key to a string value.
- [- setData:forKey:](<set(__forkey_)-3ga7z.md>) — Sets the value of the specified key to a data object.
- [- setObject:forKey:](<set(__forkey_)-9e3de.md>) — Sets the value of the specified key to a property list object.
- [- setArray:forKey:](<set(__forkey_)-40a8f.md>) — Sets the value of the specified key to an array of property list objects.
- [- setDictionary:forKey:](<set(__forkey_)-9vmlm.md>) — Sets the value of the specified key to a dictionary of property list objects.
