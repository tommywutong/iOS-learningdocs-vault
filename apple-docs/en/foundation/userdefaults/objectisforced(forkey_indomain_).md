---
title: 'objectIsForced(forKey:inDomain:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/objectisforced(forkey:indomain:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/objectisforced(forkey:indomain:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/objectisforced%28forkey%3Aindomain%3A%29.json'
content_hash: 'sha256:4d825c6c855a7749'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# objectIsForced(forKey:inDomain:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether an administrator provided the value for the key in the specified domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectIsForced(forKey key: String, inDomain domain: String) -> Bool
```

## Parameters

- `key` — The name of the key to check.

- `domain` — The domain that contains the key.

## Return Value

`true` if an administrator provides a value for the key, otherwise `false`.

## Discussion

Apps can’t change the value of managed keys, so use this method to determine if you can make changes to a key in a specific domain. For example, you might use this method to check for overrides of settings belonging to a shared app group. If a key is managed, disable any app-specific UI you use to change the value of that key.

## See Also

### Checking for managed keys

- [- objectIsForcedForKey:](<objectisforced(forkey_).md>) — Returns a Boolean value that indicates whether an administrator provided the value for the specified key.
