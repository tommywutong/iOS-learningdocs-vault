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
doc_path: '/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-3ga7z'
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-3ga7z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/set%28_%3Aforkey%3A%29-3ga7z.json'
content_hash: 'sha256:6bd42befc2825c3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# set(_:forKey:)

<sub>Instance Method</sub>

Sets the value of the specified key to a data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func set(_ aData: Data?, forKey aKey: String)
```

## Parameters

- `aData` — The data object to save to the iCloud key-value store.

- `aKey` — The key to associate with the value.

## Discussion

To store types that aren’t property list objects, archive them to an [NSData](../nsdata.md) object first and add that object to the store using this method. Exercise caution when saving custom objects to iCloud. Instances of your app on a person’s other devices must also be able to extract the objects and use them. Design your objects to be portable, and design new versions of your app to support previous versions of your custom types.

## See Also

### Setting values

- [- setBool:forKey:](<set(__forkey_)-8o8mq.md>) — Sets the value of the specified key to a Boolean value.
- [- setDouble:forKey:](<set(__forkey_)-1xml0.md>) — Sets the value of the specified key to a double value.
- [- setLongLong:forKey:](<set(__forkey_)-7tt20.md>) — Sets the value of the specified key to a 64-bit integer value.
- [- setString:forKey:](<set(__forkey_)-2rlp.md>) — Sets the value of the specified key to a string value.
- [- setObject:forKey:](<set(__forkey_)-9e3de.md>) — Sets the value of the specified key to a property list object.
- [- setArray:forKey:](<set(__forkey_)-40a8f.md>) — Sets the value of the specified key to an array of property list objects.
- [- setDictionary:forKey:](<set(__forkey_)-9vmlm.md>) — Sets the value of the specified key to a dictionary of property list objects.
