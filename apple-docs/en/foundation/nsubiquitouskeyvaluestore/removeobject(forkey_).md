---
title: 'removeObject(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsubiquitouskeyvaluestore/removeobject(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/removeobject(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitouskeyvaluestore/removeobject%28forkey%3A%29.json'
content_hash: 'sha256:d7e169aa4d0e6b87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUbiquitousKeyValueStore](../nsubiquitouskeyvaluestore.md)

# removeObject(forKey:)

<sub>Instance Method</sub>

Removes the value for the specified key from the iCloud key-value store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObject(forKey aKey: String)
```

## Parameters

- `aKey` — The key with the value you want to remove.

## Discussion

This method removes the specified key and value from the in-memory version of the store’s data. The next time the system synchronizes the data, it removes the key from the on-disk storage and iCloud server. If the key is not in the key-value store, this method does nothing.
