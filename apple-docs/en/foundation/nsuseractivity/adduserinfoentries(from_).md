---
title: 'addUserInfoEntries(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivity/adduserinfoentries(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/adduserinfoentries(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/adduserinfoentries%28from%3A%29.json'
content_hash: 'sha256:343d0301ae4d27c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# addUserInfoEntries(from:)

<sub>Instance Method</sub>

Adds the contents of the specified dictionary to the user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addUserInfoEntries(from otherDictionary: [AnyHashable : Any])
```

## Parameters

- `otherDictionary` — The dictionary containing entries to be added.

## Discussion

Use this method to add the keys from `otherDictionary` into the dictionary in the [userInfo](userinfo.md) property. If the same key is in both dictionaries, the value of the key is set to the value in the `otherDictionary` parameter.

It’s recommended that you keep the [userInfo](userinfo.md) dictionary as small as possible. The larger the dictionary, the longer it takes to deliver that payload and resume the activity.

## See Also

### Specifying activity-related data

- [userInfo](userinfo.md) — A dictionary containing app-specific state information needed to continue an activity on another device.
- [requiredUserInfoKeys](requireduserinfokeys.md) — A set of keys that represent the minimal information about the activity that should be stored for later restoration.
