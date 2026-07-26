---
title: 'objectIsForced(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/objectisforced(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/objectisforced(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/objectisforced%28forkey%3A%29.json'
content_hash: 'sha256:e0a1f991bf096dfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# objectIsForced(forKey:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether an administrator provided the value for the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectIsForced(forKey key: String) -> Bool
```

## Parameters

- `key` — The name of the key to check.

## Return Value

`true` if an administrator provides a value for the key, otherwise `false`.

## Discussion

Apps can’t change the value of managed keys, so use this method to determine if you can make changes to one of your app-specific keys. If a key is managed, disable any app-specific UI you use to change the value of that key.

## See Also

### Checking for managed keys

- [- objectIsForcedForKey:inDomain:](<objectisforced(forkey_indomain_).md>) — Returns a Boolean value that indicates whether an administrator provided the value for the key in the specified domain.
