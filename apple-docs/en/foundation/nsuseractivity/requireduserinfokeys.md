---
title: requiredUserInfoKeys
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/requireduserinfokeys
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/requireduserinfokeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/requireduserinfokeys.json'
content_hash: 'sha256:fc91902c5444329b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# requiredUserInfoKeys

<sub>Instance Property</sub>

A set of keys that represent the minimal information about the activity that should be stored for later restoration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requiredUserInfoKeys: Set<String>? { get set }
```

## Discussion

The keys come from the [userInfo](userinfo.md) property.

## See Also

### Specifying activity-related data

- [userInfo](userinfo.md) — A dictionary containing app-specific state information needed to continue an activity on another device.
- [- addUserInfoEntriesFromDictionary:](<adduserinfoentries(from_).md>) — Adds the contents of the specified dictionary to the user info dictionary.
